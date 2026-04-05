---
date: 2026-04-05
topic: system-architecture
version: v1.0
---

# 技术架构

> 基于 [PRD 终稿](/_archive/prd/compound/2026-04-03-otto-robot-prd-final.md)（33 条需求）拆解的系统分析文档，参考 [xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) 和 [aipen](https://github.com/flybear16/aipen) 两个项目的设计经验。

## 架构分层

| 层级 | 说明 | 详细文档 |
|------|------|----------|
| **系统总览** | 四层架构、技术栈选型、数据流全景 | [01-系统架构总览](/system/01-系统架构总览.md) |
| **固件层** | ESP32-S3 + PSRAM + ES8311、FreeRTOS 任务、离线唤醒、I2C 扩展 | [02-固件架构设计](/system/02-固件架构设计.md) |
| **后端服务** | AI 语音引擎、业务 API、管理后台、推送队列、内容审计 | [03-后端服务架构](/system/03-后端服务架构.md) |
| **前端客户端** | Blockly 编程、3D 预览、竞赛平台、多端适配 | [04-前端与客户端架构](/system/04-前端与客户端架构.md) |
| **通信协议** | MQTT 控制通道、WebSocket 媒体通道、消息格式定义 | [05-通信协议设计](/system/05-通信协议设计.md) |
| **数据模型** | 核心实体关系、RBAC 权限、对话记录、推送队列 | [06-数据模型设计](/system/06-数据模型设计.md) |
| **安全架构** | 传输/存储加密、JWT 认证、内容审计、儿童隐私保护 | [07-安全架构设计](/system/07-安全架构设计.md) |
| **部署运维** | Docker Compose 部署、教室网络方案、监控告警、OTA 分批 | [08-部署与运维架构](/system/08-部署与运维架构.md) |

## 参考项目

| 项目 | 借鉴内容 |
|------|----------|
| [xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) | WebSocket/MQTT 协议、ASR→LLM→TTS 音频管道、MCP 能力扩展、Docker 部署架构 |
| [aipen / 小橙AI](https://github.com/flybear16/aipen) | FastAPI 后端分层、AI 提供商抽象模式、设备激活码绑定流程、JWT + SM2 认证、标准响应格式 |
