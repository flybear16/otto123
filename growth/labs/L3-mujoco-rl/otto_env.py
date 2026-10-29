"""OTTO 桌面机器人 · MuJoCo 仿真环境（gymnasium）

与实物对齐：ESP32-S3 + PCA9685 + 4 腿舵机 + 2 臂舵机
执行器为 position 类型（ctrl = 目标角度/弧度），与 PCA9685 驱动舵机位置语义一致

实测（2026-10-30，本机 16 核 CPU 无 GPU）：
  - 随机动作 29,677 步/秒
  - 随机策略 20 回合平均回报 = -9.479（几乎立刻摔倒）
"""
import mujoco
import numpy as np
import gymnasium as gym
from gymnasium import spaces


class OttoWalkEnv(gym.Env):
    """让 OTTO 向前走。观察 12 维，动作 4 维（4 个腿关节目标角）。"""

    metadata = {"render_modes": []}

    def __init__(self, model_path="otto_model.xml", episode_len=400):
        super().__init__()
        self.model = mujoco.MjModel.from_xml_path(model_path)
        self.data = mujoco.MjData(self.model)
        self.episode_len = episode_len
        self.act_low = self.model.actuator_ctrlrange[:, 0].copy()
        self.act_high = self.model.actuator_ctrlrange[:, 1].copy()
        self.observation_space = spaces.Box(-np.inf, np.inf, shape=(12,), dtype=np.float32)
        self.action_space = spaces.Box(
            self.act_low[:4].astype(np.float32), self.act_high[:4].astype(np.float32)
        )
        self.init_qpos = self.data.qpos.ravel().copy()

    def _obs(self):
        d = self.data
        quat = d.qpos[3:7]
        pitch = 2 * np.arctan2(quat[1], quat[0])
        roll = 2 * np.arctan2(quat[2], quat[0])
        return np.array(
            [
                d.qpos[2],          # 躯干高度
                pitch,              # 俯仰角
                roll,               # 横滚角
                d.qvel[0],          # 前进速度
                *d.qpos[7:11],      # 4 个腿关节角
                *d.qvel[6:10],      # 4 个腿关节角速度
            ],
            dtype=np.float32,
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        mujoco.mj_resetData(self.model, self.data)
        self.data.qpos[:] = self.init_qpos
        self.data.qpos[2] += self.np_random.uniform(-0.005, 0.005)
        mujoco.mj_forward(self.model, self.data)
        self.steps = 0
        return self._obs(), {}

    def step(self, action):
        a = np.clip(action, self.act_low[:4], self.act_high[:4]).astype(np.float64)
        self.data.ctrl[:4] = a
        self.data.ctrl[4:] = 0.0
        mujoco.mj_step(self.model, self.data)
        self.steps += 1

        d = self.data
        vx = d.qvel[0]
        alive = d.qpos[2] > 0.055
        # 奖励 = 前进速度 + 存活 - 能耗 - 姿态惩罚；摔倒直接给 -1
        reward = 1.5 * vx + 0.6 * alive - 0.002 * float(np.sum(np.square(a))) - 0.5 * abs(d.qpos[4])
        if not alive:
            reward = -1.0

        terminated = not alive
        truncated = self.steps >= self.episode_len
        info = {"x": float(d.qpos[0]), "vx": float(vx), "alive": alive}
        return self._obs(), reward, terminated, truncated, info


if __name__ == "__main__":
    import time

    env = OttoWalkEnv()
    env.reset(seed=0)
    t0 = time.time()
    N = 5000
    for _ in range(N):
        _, _, term, trunc, _ = env.step(env.action_space.sample())
        if term or trunc:
            env.reset()
    dt = time.time() - t0
    print(f"{N} 步用时 {dt:.2f}s -> {N/dt:,.0f} 步/秒")
