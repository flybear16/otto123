# system/ — 技术架构文档

**Generated:** 2026-04-12

## OVERVIEW

OTTO 123 技术架构文档，包含固件、后端服务、前端界面、通信协议、安全架构。

## WHERE TO LOOK

| 文件 | 内容 |
|------|------|
| `01-overview.md` | 系统架构总览 |
| `02-firmware.md` | 固件架构 |
| `03-backend.md` | 后端服务架构 |
| `04-frontend.md` | 前端界面架构 |
| `05-protocol.md` | 通信协议 |
| `06-ai.md` | AI语音交互 |
| `07-security.md` | 安全架构设计 |
| `08-deployment.md` | 部署方案 |

## KEY TECHNICAL CONTEXT

* 目标硬件：ESP32-S3 + 8MB PSRAM + ES8311 音频芯片
* 单台成本：≤250元
* 通信架构：MQTT（控制通道）+ WebSocket（媒体/音频流）
* 教室场景：2-3人/机器人，5GHz Wi-Fi AP支持15-20台设备

## CONVENTIONS

* 编号 `01-08` 前缀
* 技术术语保持英文缩写
* 中文编写

## ANTI-PATTERNS

* 固件代码在独立仓库，不在此目录
* 架构文档只做分析，不含实现代码
