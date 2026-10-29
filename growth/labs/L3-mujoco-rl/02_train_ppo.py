"""Tier B · PPO 强化学习：让机器自己学走路

教学定位：学生亲眼看到"奖励函数怎么写，机器人就往哪走"。

实测（2026-10-30，本机 16 核 CPU 无 GPU）：
  - 训练速度 3,528 步/秒（40 万步 = 1.9 分钟）
  - 40 万步结果：学会站稳（回报 -9.5 -> 216），但位移仅 1.5cm
  - 结论：学会"不摔倒"很快，学会"往前走"需要更多步数与更好的奖励设计
  - 这正是本课要讲的核心：RL 不是魔法，是"目标定义 + 试错"的工程

运行：python 02_train_ppo.py [总步数]
"""
import sys
import time

import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

from otto_env import OttoWalkEnv


class Reporter(BaseCallback):
    def __init__(self):
        super().__init__()
        self.t0 = time.time()

    def _on_step(self):
        if self.n_calls % 25000 == 0:
            elapsed = time.time() - self.t0
            buffer = [
                b.get("r")
                for b in list(self.model.ep_info_buffer)
                if isinstance(b, dict) and "r" in b
            ]
            mean_rew = float(np.mean(buffer[-20:])) if buffer else 0.0
            print(
                f"  [{self.n_calls:>7} 步 | {elapsed / 60:5.1f} 分钟] "
                f"最近20回合平均回报 = {mean_rew:.2f}",
                flush=True,
            )
        return True


def evaluate(model, episodes=20):
    env = OttoWalkEnv()
    rewards, distances = [], []
    for i in range(episodes):
        obs, _ = env.reset(seed=1000 + i)
        x0 = env.data.qpos[0]
        done, total = False, 0.0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, term, trunc, _ = env.step(action)
            total += reward
            done = term or trunc
        rewards.append(total)
        distances.append((env.data.qpos[0] - x0) * 100)
    positive = [d for d in distances if d > 0]
    return (
        float(np.mean(rewards)),
        float(np.mean(distances)),
        float(np.mean(positive)) if positive else 0.0,
        float(max(distances)),
    )


def main():
    total_steps = int(sys.argv[1]) if len(sys.argv) > 1 else 400000

    env = OttoWalkEnv()

    # 基线：随机策略能拿多少分（用来证明"训练确实有用"）
    np.random.seed(0)
    baseline = []
    for k in range(20):
        obs, _ = env.reset(seed=k)
        done, total = False, 0.0
        while not done:
            obs, reward, term, trunc, _ = env.step(env.action_space.sample())
            total += reward
            done = term or trunc
        baseline.append(total)
    print(f"[基线] 随机策略 20 回合平均回报 = {np.mean(baseline):.3f}", flush=True)

    model = PPO(
        "MlpPolicy",
        env,
        verbose=0,
        n_steps=1024,
        batch_size=256,
        learning_rate=3e-4,
        gamma=0.99,
        gae_lambda=0.95,
        seed=0,
        policy_kwargs=dict(net_arch=[64, 64]),
        device="cpu",
    )

    t0 = time.time()
    model.learn(total_timesteps=total_steps, callback=Reporter())
    elapsed = time.time() - t0
    print(f"[PPO] {total_steps} 步用时 {elapsed / 60:.1f} 分钟 -> {total_steps / elapsed:,.0f} 步/秒")

    mean_rew, mean_dist, pos_dist, max_dist = evaluate(model)
    print(
        f"[评估] 平均回报 {mean_rew:.2f} | 平均位移 {mean_dist:.1f}cm | "
        f"正向回合均值 {pos_dist:.1f}cm | 最远 {max_dist:.1f}cm"
    )

    model.save("otto_ppo")
    print("已保存 otto_ppo.zip")


if __name__ == "__main__":
    main()
