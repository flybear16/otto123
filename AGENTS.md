# PROJECT KNOWLEDGE BASE

**Generated:** 2026-04-02 23:16:25
**Commit:** 40a9455
**Branch:** main

## OVERVIEW

OTTO 123 是一个面向中小学生的开源机器人创客教育项目，基于 OTTO Robot 开源硬件平台，结合 AI 语音交互技术，打造完整的创客教育解决方案。项目以 Markdown 文档为主，包含三大商业模式：学校社团课、晚托班特色项目、C端周末/假期班。

## STRUCTURE

```
otto123/
├── overview/                # 项目概述、愿景、用户画像
├── product/                 # 产品文档
├── business/                # 商业分析文档
│   ├── school/              # 学校社团课详情
│   ├── weekend/             # C端周末班详情
│   └── daycare/             # 晚托班详情
├── operations/              # 运营文档
├── src/                     # 源代码占位（独立仓库）
├── _archive/prd/            # PRD 开发过程存档
├── _media/                  # 静态资源（logo等）
└── README.md               # 项目入口
```

## WHERE TO LOOK

| 任务 | 位置 | 说明 |
|------|------|------|
| 了解项目 | `README.md` | 项目整体介绍 |
| 项目概述 | `overview/` | 愿景、用户画像、价值主张 |
| 学校社团课 | `business/school/` | 完整分析文档 |
| 晚托班方案 | `business/daycare/` | 晚托班商业模式 |
| C端周末班 | `business/weekend/` | 周末/假期班方案 |
| 运营SOP | `operations/` | 运营手册 |
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
