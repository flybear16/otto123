"""03_analyze.py · 跑一遍步态并出图（无需显卡，matplotlib Agg 后端）

实测（2026-10-30）：400 帧轨迹图生成耗时 < 1 秒，PNG 约 38 KB。

注意：无头服务器上 MuJoCo 离屏渲染可能全黑（EGL/OSMesa 都不通），
所以课程统一用"数据图"代替"视频"——这也正是数据思维的第一步。

运行：python 03_analyze.py
"""
import matplotlib

matplotlib.use("Agg")  # 无显示器环境必须先设后端
import matplotlib.pyplot as plt
import numpy as np

from otto_env import OttoWalkEnv


def run_gait(A=0.15, B=0.80, freq=1.6, phase=2.36, steps=400):
    env = OttoWalkEnv()
    env.reset(seed=7)
    xs, zs, alive = [], [], []
    for i in range(steps):
        t = i * env.model.opt.timestep
        action = np.array(
            [
                A * np.sin(2 * np.pi * freq * t),
                B * max(0, np.cos(2 * np.pi * freq * t)),
                A * np.sin(2 * np.pi * freq * t + phase),
                B * max(0, np.cos(2 * np.pi * freq * t + phase)),
            ]
        )
        _, _, term, trunc, _ = env.step(action)
        xs.append(env.data.qpos[0] * 100)
        zs.append(env.data.qpos[2] * 100)
        alive.append(env.data.qpos[2] > 0.055)
        if term or trunc:
            break
    return np.array(xs), np.array(zs), np.array(alive)


def main():
    xs, zs, alive = run_gait()

    fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))
    axes[0].plot(xs, color="#2a6fb0")
    axes[0].set_title("Forward distance x (cm)")
    axes[0].set_xlabel("step")
    axes[0].grid(alpha=0.3)

    axes[1].plot(zs, color="#e08b1a")
    axes[1].axhline(5.5, ls="--", c="r", lw=1, label="fall threshold")
    axes[1].set_title("Torso height z (cm)")
    axes[1].set_xlabel("step")
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    axes[2].plot(alive.astype(int), color="#3a9d5d")
    axes[2].set_title("Upright (1/0)")
    axes[2].set_xlabel("step")
    axes[2].set_yticks([0, 1])
    axes[2].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("trajectory.png", dpi=110)
    print(
        f"simulated {len(xs)} steps | total displacement {xs[-1] - xs[0]:+.1f}cm | "
        f"upright for {alive.sum() / 400:.2f}s"
    )
    print("saved trajectory.png")


if __name__ == "__main__":
    main()
