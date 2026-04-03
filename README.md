# OTTO 123 项目

> 🚀 **让每个孩子都能创造自己的机器人**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

## 项目简介

OTTO 123 是一个面向中小学生的开源机器人创客教育项目，基于 [OTTO Robot](https://oshwhub.com/txp666/ottorobot) 开源硬件平台，结合 AI 语音交互技术，打造完整的创客教育解决方案。

### 核心理念

```
开源 · 动手 · 创造 · 分享

我们相信：
• 每个孩子都有创造的潜能
• 最好的学习是动手实践
• 开源让教育更公平
• 分享让知识更有价值
```

## 项目结构

```
otto123/
├── 📁 overview/               # 项目概述、愿景、用户画像
├── 📁 product/                # 产品方案
├── 📁 business/                # 商业模式
│   ├── school/                 # 学校社团课
│   ├── daycare/                # 晚托班合作
│   └── weekend/                # C端周末班
├── 📁 operations/              # 运营手册
├── 📁 _archive/prd/            # PRD 开发过程存档
├── 📁 src/                     # 源代码（独立仓库）
├── 📁 _media/                  # Docsify 静态资源（logo、favicon）
└── 📄 README.md                # 本文件
```

## 三大商业模式

### 1️⃣ 学校社团课合作
与中小学合作，开设课后机器人社团。

- **目标客户**: 小学3-6年级、初中7-8年级
- **合作模式**: 联合运营（学校出场地，我方出课程和师资）
- **定价**: ¥1,280-1,580/学期（16课时）
- **优势**: 零场地成本、批量获客、品牌背书

👉 [查看详细方案](/business/school/学校社团课合作方案.md)

### 2️⃣ 晚托班特色项目
与晚托机构合作，植入OTTO机器人特色课程。

- **目标客户**: 双职工家庭小学生
- **合作模式**: 课程植入（按学生或课时收费）
- **定价**: ¥300-500/月/人（每周2次课）
- **优势**: 轻资产、快启动、可复制

👉 [查看详细方案](/business/daycare/晚托班特色项目方案.md)

### 3️⃣ C端周末/假期班
直接面向家长招生，开设周末班和假期集训营。

- **目标客户**: 对科技教育感兴趣的家庭
- **产品形态**: 体验课、学期班、竞赛集训营
- **定价**: ¥80-150/课时
- **优势**: 利润高、品牌直营、用户粘性

👉 [查看详细方案](/business/weekend/C端周末假期班方案.md)

## 快速开始

### 对于教育者

1. **了解项目**: 阅读 [项目概述](/overview/)
2. **选择模式**: 根据资源情况选择适合的商业模式
3. **采购设备**: 联系硬件供应商获取OTTO套件
4. **启动运营**: 按照 [运营手册](/operations/) 执行

### 对于开发者

```bash
# 克隆项目
git clone https://github.com/yourusername/otto123.git
cd otto123

# 查看固件代码
cd src/firmware

# 查看课程资源
cd src/curriculum
```

### 对于合作伙伴

- **学校/机构合作**: 联系项目负责人获取合作方案
- **硬件供应**: 查看 [硬件规格](/product/)
- **课程授权**: 了解 [授权合作模式](/business/)

## 项目状态

| 模块 | 状态 | 完成度 |
|------|------|--------|
| 项目概述与定位 | ✅ 已完成 | 100% |
| 产品方案设计 | ✅ 已完成 | 100% |
| 学校社团课方案 | ✅ 已完成 | 100% |
| 晚托班合作方案 | ✅ 已完成 | 100% |
| C端周末班方案 | 📝 进行中 | 80% |
| 运营手册SOP | ✅ 已完成 | 100% |
| 财务模型 | ✅ 已完成 | 100% |
| BD谈判策略 | ✅ 已完成 | 100% |
| 课程资源开发 | 🔄 持续迭代 | 60% |
| 硬件固件优化 | 🔄 持续迭代 | 70% |

## 核心团队

| 角色 | 负责人 | 职责 |
|------|--------|------|
| 🎯 总指挥 | main | 统筹全局、战略决策 |
| ✍️ 内容创作 | creator | 课程开发、文案写作 |
| 🔬 参谋 | canmou | 分析建议、方案设计 |
| 📋 运营官 | yunying | 数据分析、运营策略 |
| 🧑‍💻 开发助理 | dev | 技术架构、代码开发 |
| 🧬 进化官 | jinhua | 知识管理、持续改进 |

## 贡献指南

我们欢迎各种形式的贡献：

- 🐛 **问题反馈**: 提交 Issue 描述你遇到的问题
- 💡 **功能建议**: 提出新想法和改进建议
- 📝 **文档改进**: 完善文档、修正错误
- 🔧 **代码贡献**: 提交 Pull Request
- 🎨 **资源分享**: 分享你的课程案例和教学经验

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)

## 开源协议

本项目采用 [MIT License](./LICENSE) 开源协议。

```
Copyright (c) 2026 OTTO 123 Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 致谢

- [OTTO Robot 开源项目](https://oshwhub.com/txp666/ottorobot) - 硬件设计基础
- [小智 AI 语音平台](https://xiaozhi.me) - AI 语音交互能力
- [立创开源硬件平台](https://oshwhub.com) - 硬件生态支持

## 联系我们

- 📧 邮箱: contact@otto123.edu
- 💬 微信: otto123_official
- 🌐 官网: https://otto123.github.io

---

> **让创造触手可及，让教育回归本质。**
>
> *OTTO 123 项目团队*
