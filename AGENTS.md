# PROJECT KNOWLEDGE BASE

**Generated:** 2026-04-04 02:15:00
**Commit:** 24f922a
**Branch:** main

## OVERVIEW

OTTO 123 是一个面向中小学生的开源机器人创客教育项目，基于 OTTO Robot 开源硬件平台，结合 AI 语音交互技术，打造完整的创客教育解决方案。项目以 Markdown 文档为主，包含三大商业模式：学校社团课、晚托班特色项目、C端周末/假期班。

## STRUCTURE

```
otto123/（一堂五步法）
├── needs/                   # 1. 需求（用户画像、竞品分析、机会预判）
├── solution/                # 2. 解决方案（愿景、产品、里程碑）
├── business/                # 3. 商业模式（school/ daycare/ weekend/）
├── growth/                  # 4. 增长（运营手册、课程体系）
├── barriers/                # 5. 壁垒（核心价值主张）
├── yitang/                  # 一堂课程学习资料
├── src/                     # 源代码占位（独立仓库）
├── _archive/prd/            # PRD 开发过程存档
├── _media/                  # 静态资源（logo等）
└── README.md               # 项目入口
```

## WHERE TO LOOK

| 任务 | 位置 | 说明 |
|------|------|------|
| 了解项目 | `README.md` | 项目整体介绍 |
| 项目概述 | `needs/` `solution/` | 需求分析、解决方案 |
| 学校社团课 | `business/school/` | 完整分析文档 |
| 晚托班方案 | `business/daycare/` | 晚托班商业模式 |
| C端周末班 | `business/weekend/` | 周末/假期班方案 |
| 运营SOP | `growth/` | 运营手册、课程体系 |
| 一堂课程 | `yitang/` | 一堂五步法学习资料 |
| PRD 文档 | `_archive/prd/compound/` | 产品需求文档 |

## CONVENTIONS

- 文档使用中文编写
- 目录采用编号前缀：`01-`, `02-`, `03-` 等
- 商业模式文档在 `business/` 目录下
- 图片资源放在 `_media/` 目录

## ANTI-PATTERNS (THIS PROJECT)

- 无需代码lint/format配置（纯文档项目）
- 无需CI/CD配置（静态文档站）
- 无需测试框架（文档项目）

## UNIQUE STYLES

- 采用 GitBook/Docsify 风格构建静态文档站
- 使用中文标题和内容
- 文档包含版本号、创建日期、作者信息
- 商业模式文档包含财务模型、谈判策略、执行SOP

## COMMANDS

```bash
# 本地预览文档站（如使用 docsify 等）
docsify serve .

# 或其他文档工具
```

## NOTES

- 项目以商业文档为主，非代码项目
- 无源码目录（固件代码在独立仓库）
- 静态网站托管于 GitHub Pages
