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

### 文档体系

```
overview/          # 项目概述（愿景、用户画像、价值主张、竞品分析、里程碑）
product/           # 产品方案
business/          # 商业模式（school/ daycare/ weekend/）+ 市场分析文件
operations/        # 运营手册（开业、日常、师资、家长、安全）
src/               # 源代码占位（固件/课程/工具，独立仓库）
_archive/prd/      # PRD 开发过程存档（brainstorm/ compound/ ideation/ plan/ review/ work/ plans/）
_media/            # Docsify 静态资源（logo、favicon、PWA manifest）
```

最终 PRD 位于 `_archive/prd/compound/2026-04-03-otto-robot-prd-final.md`，定义了 33 项需求。

### 侧边栏与导航

- `_sidebar.md` — Docsify 侧边栏配置
- `_navbar.md` — 顶部导航栏
- `index.html` — Docsify 主题、插件、搜索配置（主题色 `#42b983`）

**关键规则：`_sidebar.md` 中所有链接必须使用绝对路径（以 `/` 开头）**，否则在子目录页面中会解析错误（如 `operations/startup.md` 会被解析为 `operations/operations/startup.md`）。

### Docsify 插件配置

`index.html` 中已加载的插件：
- 搜索（search）、复制代码（copy-code）、分页（pagination）、Emoji、外部脚本、图片缩放
- **Mermaid**：`mermaid@10` + `docsify-mermaid@2`，用于渲染 PRD 中的流程图

### PWA 与图标

- `_media/manifest.json` — PWA manifest
- favicon: `favicon.ico`，PNG 图标: `logo-32.png`、`logo-180.png`、`logo-192.png`

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

## Key Technical Context (PRD)

产品目标硬件：ESP32-S3 + 8MB PSRAM + ES8311 音频芯片，单台成本 ≤250 元。通信架构：MQTT（控制通道）+ WebSocket（媒体/音频流）。教室场景：2-3 人/机器人，独立 5GHz Wi-Fi AP 支持 15-20 台设备。
