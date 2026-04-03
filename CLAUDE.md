# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OTTO 123 是面向中小学生的开源机器人创客教育项目，基于 OTTO Robot 开源硬件平台 + AI 语音交互技术。项目以 Markdown 文档为主（Docsify 静态站点），非代码项目——固件代码在独立仓库。

## Commands

```bash
# 本地预览文档站
docsify serve .
```

无 build/lint/test 命令——纯文档项目，无需 CI/CD。

## Architecture

### 文档体系（docs/）

编号前缀目录为核心文档流，PRD 开发流程存放在 docs/ 子目录中：

```
docs/
├── 01-项目概述/ ~ 07-附录/   # 正式文档（编号排序）
├── brainstorm/                # 头脑风暴记录
├── ideation/                  # 创意点子
├── plan/                      # PRD 结构评审
├── work/                      # 文档打磨
├── review/                    # 多角色评审
└── compound/                  # 最终 PRD（2026-04-03-otto-robot-prd-final.md）
```

最终 PRD 定义了 33 项需求（语音交互、Web配置、硬件DIY、动作编程、竞赛平台、权限管理、多用户共享、设备管理），是产品开发的核心参考文档。

### 业务文档（business/）

三种商业模式各自独立目录：`school/`（学校社团）、`daycare/`（晚托班）、`weekend/`（C端周末班）。

### 侧边栏与导航

- `_sidebar.md` — Docsify 侧边栏配置
- `_navbar.md` — 顶部导航栏
- `index.html` — Docsify 主题、插件、搜索配置（主题色 `#42b983`）

## Conventions

- 所有文档使用中文
- 目录采用编号前缀排序：`01-`, `02-` 等
- 图片资源统一放在 `_media/` 目录
- PRD 流程：ideation → brainstorm → plan → work → review → compound
- 文档包含版本号、创建日期、作者信息

## Custom Commands

| 命令 | 用途 |
|------|------|
| `/gitup` | git stage/add/commit/push 一波流 |
| `/openspec:proposal` | 创建 OpenSpec 提案 |
| `/openspec:apply` | 实施 OpenSpec 变更 |
| `/openspec:archive` | 归档已部署的 OpenSpec |

## Key Technical Context (PRD)

产品目标硬件：ESP32-S3 + 8MB PSRAM + ES8311 音频芯片，单台成本 ≤250 元。通信架构：MQTT（控制通道）+ WebSocket（媒体/音频流）。教室场景：2-3 人/机器人，独立 5GHz Wi-Fi AP 支持 15-20 台设备。
