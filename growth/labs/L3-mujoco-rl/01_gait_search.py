"""Tier A · 手写步态 + 参数寻优（不依赖任何 RL，0.5 秒出结果）

教学定位：先让学生相信"计算机能帮我们找到最优动作"，再引入"机器自己学"。
本脚本做的是最朴素也最有效的优化：网格搜索。

实测（2026-10-30）：240 组参数、0.5 秒跑完，最优组合位移 +31.8cm。

运行：python 01_gait_search.py
"""
import itertools
import json
import time

import mujoco
import numpy as np

MODEL = "otto_model.xml"


def simulate(params, model, duration=6.0):
    """跑一段固定时长的仿真，返回 (fitness, 位移cm, 是否站稳, 存活秒数)。"""
    A, B, freq, phase = params
    data = mujoco.MjData(model)
    mujoco.mj_resetData(model, data)
    dt = model.opt.timestep
    steps = int(duration / dt)
    x0 = data.qpos[0]
    alive_time = 0.0

    for i in range(steps):
        t = i * dt
        s_l, c_l = np.sin(2 * np.pi * freq * t), np.cos(2 * np.pi * freq * t)
        s_r = np.sin(2 * np.pi * freq * t + phase)
        c_r = np.cos(2 * np.pi * freq * t + phase)
        data.ctrl[:] = [A * s_l, B * max(0, c_l), A * s_r, B * max(0, c_r), 0, 0]
        mujoco.mj_step(model, data)
        if data.qpos[2] > 0.055:
            alive_time += dt
        else:
            break

    distance = (data.qpos[0] - x0) * 100
    upright = data.qpos[2] > 0.055
    fitness = distance + (30 if upright else 0) + alive_time * 0.01
    return fitness, distance, upright, alive_time


def main():
    model = mujoco.MjModel.from_xml_path(MODEL)
    grid = list(
        itertools.product(
            [0.15, 0.25, 0.35, 0.45],           # 髋摆幅 A
            [0.20, 0.40, 0.60, 0.80],           # 膝弯曲 B
            [0.8, 1.2, 1.6, 2.0, 2.5],          # 步频 freq
            [np.pi, np.pi * 0.75, np.pi * 1.25],  # 左右相位差
        )
    )

    t0 = time.time()
    results = []
    for params in grid:
        fitness, dist, upright, alive = simulate(params, model)
        results.append((fitness, params, dist, upright, alive))
    results.sort(reverse=True, key=lambda r: r[0])

    print(f"网格搜索 {len(grid)} 组参数，用时 {time.time() - t0:.1f} 秒\n")
    print("Top 5:")
    for fitness, params, dist, upright, alive in results[:5]:
        print(
            f"  A={params[0]:.2f} B={params[1]:.2f} freq={params[2]:.1f} "
            f"phase={params[3]:.2f} -> 位移 {dist:+.1f}cm 站稳={upright} "
            f"存活 {alive:.1f}s fitness={fitness:.1f}"
        )

    best = results[0]
    print(f"\n最优 fitness = {best[0]:.1f}，位移 {best[2]:+.1f}cm")
    cfg = {"A": best[1][0], "B": best[1][1], "freq": best[1][2], "phase": float(best[1][3])}
    with open("best_gait.json", "w") as f:
        json.dump(cfg, f, indent=2)
    print("已保存 best_gait.json")


if __name__ == "__main__":
    main()
