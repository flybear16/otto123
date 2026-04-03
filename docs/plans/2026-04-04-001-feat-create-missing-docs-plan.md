---
title: "feat: Create missing documentation files"
type: feat
status: active
date: 2026-04-04
---

# feat: Create Missing Documentation Files

## Overview

OTTO 123 文档库存在 10 个被引用但尚未创建的文件，分布在三个目录。需要按照现有文档的风格和深度，创建这些缺失文件，并取消 `_sidebar.md` 和各 README 中的 HTML 注释以恢复链接。

## Problem Frame

文档库中 `operations/README.md`、`docs/01-项目概述/README.md`、`_sidebar.md` 引用了不存在的文件，导致用户点击后出现 404。需要补齐内容，使文档体系完整可用。

## Requirements Trace

- R1. 创建 `operations/` 目录下 5 个运营手册文件
- R2. 创建 `docs/01-项目概述/` 目录下 4 个项目文档
- R3. 创建 `business/daycare/05-finance.md` 财务模型
- R4. 取消各文件中的 HTML 注释，恢复文档链接
- R5. 新文档风格与现有文档保持一致

## Scope Boundaries

- 仅创建被现有 README/sidebar 引用的缺失文件
- 不创建 `business/daycare/README.md` 中引用的 06-08 文件（这些尚未在 sidebar 中出现）
- 不修改已有文档内容（除取消注释外）

## Context & Research

### Relevant Code and Patterns

- **运营手册风格**：参考 `business/school/05-operations.md` — 使用树状流程图、检查清单、模板等格式
- **财务模型风格**：参考 `business/school/06-finance.md` 和 `business/weekend/05-finance.md` — 收入/成本表格 + 利润计算 + 规模化预测
- **项目概述风格**：参考 `docs/01-项目概述/01-愿景与使命.md` — 标题 + 分节 + 表格/列表 + 分隔线
- **竞品分析风格**：参考 `business/competitor-analysis.md` — 竞品清单表格 + 多维对比矩阵 + SWOT
- **PRD 上下文**：`docs/compound/2026-04-03-otto-robot-prd-final.md` — 33 项需求定义了产品全貌

### Content Sourcing

- 运营手册内容应与 PRD 中的非功能性需求（性能、安全、通信架构）保持一致
- 用户画像基于 PRD 1.1 核心用户表（学生/教师/机构管理者/家长）
- 竞品分析可复用 `business/competitor-analysis.md` 中的数据，侧重项目层面总结
- 里程碑参考 PRD 的三期规划（机构内部赛 → 机构间联赛 → 线上社区）

## Key Technical Decisions

- **晚托班财务模型**：参考 school/06-finance（单校模型 + 规模化预测 + 定价策略）和 weekend/05-finance（收入预测 + 成本结构 + 盈利优化）的结构，结合 daycare 的合作模式（自营/植入/加盟）
- **运营手册文件**：不使用 `##` 一级标题（与 README 保持一致），使用 `###` 子标题，因为 school/05-operations.md 也是如此

## Implementation Units

- [ ] **Unit 1: docs/01-项目概述 文档（4个文件）**

**Goal:** 创建项目概述目录下缺失的 4 个文档

**Requirements:** R2, R5

**Dependencies:** None

**Files:**
- Create: `docs/01-项目概述/02-目标用户画像.md`
- Create: `docs/01-项目概述/03-核心价值主张.md`
- Create: `docs/01-项目概述/04-竞品分析.md`
- Create: `docs/01-项目概述/05-项目里程碑.md`

**Approach:**
- `02-目标用户画像.md`：基于 PRD 1.1 核心用户表扩展，每个角色包含画像描述、核心诉求、使用场景、痛点分析
- `03-核心价值主张.md`：从愿景与使命中提取，围绕"低成本+AI+开源"差异化定位，使用价值主张画布格式
- `04-竞品分析.md`：浓缩 `business/competitor-analysis.md` 为项目层面的竞品概览，含直接竞品/间接竞品对比表和 OTTO 差异化总结
- `05-项目里程碑.md`：基于 PRD 三期规划 + 愿景使命中的短期/中期/长期目标，按时间线排列

**Patterns to follow:**
- `docs/01-项目概述/01-愿景与使命.md` — 标题层级、分隔线、引用格式
- `docs/compound/2026-04-03-otto-robot-prd-final.md` — 数据来源

**Verification:**
- 4 个文件均可在 Docsify 中正常渲染
- 内容与 PRD 数据一致，无矛盾

- [ ] **Unit 2: business/daycare/05-finance.md**

**Goal:** 创建晚托班财务模型文档

**Requirements:** R3, R5

**Dependencies:** None

**Files:**
- Create: `business/daycare/05-finance.md`

**Approach:**
- 结构对标 `business/school/06-finance.md`（单校模型 → 规模化 → 定价策略）
- 结合晚托班三种合作模式（自营/植入/加盟），分别给出财务模型
- 关键数据：参考 school 定价 ¥1,280/学期，晚托班场景可能不同需调整
- 包含：收入端、成本端、利润计算、规模化预测、盈亏平衡分析

**Patterns to follow:**
- `business/school/06-finance.md` — 表格格式、利润计算代码块
- `business/weekend/05-finance.md` — 盈利优化路径结构
- `business/daycare/02-models.md` — 三种合作模式细节

**Verification:**
- 财务数据内部自洽（收入-成本=利润）
- 与 daycare 其他文档数据一致

- [ ] **Unit 3: operations/ 运营手册（5个文件）**

**Goal:** 创建运营手册目录下缺失的 5 个文件

**Requirements:** R1, R5

**Dependencies:** None

**Files:**
- Create: `operations/startup.md`
- Create: `operations/daily.md`
- Create: `operations/teachers.md`
- Create: `operations/parents.md`
- Create: `operations/safety.md`

**Approach:**
- `startup.md`（开业筹备）：从 0 到 1 的开店指南，参考 school/05-operations 的 Week 1-7 流程，扩展为完整开业清单（选址、装修、设备采购、人员招聘、资质办理、试运营）
- `daily.md`（日常运营）：每日 SOP 检查表，参考 school/05-operations 的日常运营节奏，按课前/课中/课后/收尾组织，附教学日志模板
- `teachers.md`（师资管理）：招聘标准、培训体系、考核指标、晋升路径
- `parents.md`（家长服务）：沟通标准、工具使用、投诉处理、满意度调查
- `safety.md`（安全管理）：安全制度、应急预案、保险要求、事故处理流程

**Patterns to follow:**
- `business/school/05-operations.md` — 树状流程图、检查清单格式
- `operations/README.md` — 关键指标表、章节导航结构
- PRD 4.3 安全与隐私 — 数据安全要求

**Verification:**
- 5 个文件均可在 Docsify 中正常渲染
- operations/README.md 的链接可正常跳转

- [ ] **Unit 4: 恢复文档链接**

**Goal:** 取消 HTML 注释，恢复所有被注释掉的文档链接

**Requirements:** R4

**Dependencies:** Unit 1, Unit 2, Unit 3

**Files:**
- Modify: `docs/01-项目概述/README.md` — 取消 02-05 文件链接的注释
- Modify: `_sidebar.md` — 取消 `business/daycare/05-finance.md` 链接的注释
- Modify: `operations/README.md` — 取消 5 个运营手册链接的注释

**Approach:**
- 移除 `<!-- -->` 注释标记，恢复原始 Markdown 链接
- 验证所有链接指向的文件存在

**Verification:**
- `docsify serve .` 本地预览所有链接可正常跳转
- 无 404 链接

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| 新文档内容与 PRD 数据不一致 | 以 PRD 为唯一数据来源，交叉引用 |
| 晚托班财务数据缺乏参考 | 基于 school/weekend 已有模型合理推算 |
| 文档风格不统一 | 严格对标已有文档的格式模板 |

## Documentation / Operational Notes

- 创建完成后需更新 `docs/plans/` 中的 plan 状态为 completed
- 如有需要可同步更新 CLAUDE.md 中的目录结构描述
