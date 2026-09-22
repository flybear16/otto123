# TODO.md

**v6.0.0 重启方案 approved（2026-09-22）** —— 归档期结束。

## 当前状态

- 归档期：2026-06-11 ~ 2026-09-21（**102 天**）
- v6 启动：2026-09-22 起
- 参谋（canmou / 分析）已通知，24h 内 re-enable 相关 cron

## v6 三大核心

- **Layer 1 决策层**：**Laya**（开源 System-1 模型，32.8ms 决策，Apache-2.0）
- **Layer 2 工具层**：**Needle**（14MB 端侧工具调用模型，离线运行）
- **Layer 3 内容层**：**OpenMAIC**（AI 互动课堂）+ **DeepTutor**（个人学习追踪）

## 下一步（v6 30 天最小验证）

- [ ] 写 `docs/v6-plan.md`（v6 完整方案）
- [ ] 把 OpenMAIC / DeepTutor / Needle / Laya 调研存到 `materials/`
- [ ] 在 Otto 现有硬件上跑通三层架构 demo
- [ ] 验证 1 个教学场景（学生问数学题 → Laya 判紧急 → Needle 调舵机 → OpenMAIC 生成讲解）

---

_最后更新: 2026-09-22_