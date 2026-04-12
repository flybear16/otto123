# PROJECT KNOWLEDGE BASE

**Generated:** 2026-04-12
**Commit:** ab2c25d
**Branch:** main

## OVERVIEW

OTTO 123 是面向中小学生的开源机器人创客教育项目，基于 OTTO Robot 开源硬件 + AI 语音交互。Docsify 静态文档站，三大商业模式：学校社团课、晚托班、C 端周末班。源码在独立仓库。

## STRUCTURE

```
otto123/
├── needs/              # 1. 需求（用户画像、竞品分析）
├── solution/           # 2. 解决方案（愿景、产品、里程碑）
├── business/           # 3. 商业模式（school/ daycare/ weekend/）
├── growth/            # 4. 增长（运营手册、课程体系）
├── barriers/          # 5. 壁垒（核心价值主张）
├── yitang/            # 一堂课程学习资料
├── system/            # 技术架构（固件、后端、协议）
├── prototype/         # 原型设计
├── _media/            # 静态资源（logo、PWA manifest）
├── _archive/prd/      # PRD 存档
└── README.md          # 项目入口
```

## WHERE TO LOOK

| 任务     | 位置                       | 说明        |
| ------ | ------------------------ | --------- |
| 了解项目   | `README.md`              | 项目整体介绍    |
| 项目概述   | `needs/` `solution/`     | 需求分析、解决方案 |
| 学校社团课  | `business/school/`       | 完整分析文档    |
| 晚托班方案  | `business/daycare/`      | 晚托班商业模式   |
| C 端周末班  | `business/weekend/`      | 周末/假期班方案  |
| 运营 SOP  | `growth/`                | 运营手册、课程体系 |
| 一堂课程   | `yitang/`                | 一堂五步法学习资料 |
| 技术架构   | `system/`                | 固件/后端/前端/协议 |
| 原型      | `prototype/`             | 产品原型演示     |
| PRD 文档 | `_archive/prd/compound/` | 产品需求文档    |

## CODE MAP

无源码目录（代码在独立仓库）。文档站基于 Docsify。

| 组件     | 位置          | 说明          |
| ------- | ----------- | ----------- |
| 侧边栏导航  | `_sidebar.md` | 文档目录树       |
| 顶部导航   | `_navbar.md` | 9个主链接       |
| 封面页    | `_coverpage.md` | 文档站封面       |
| Docsify | `index.html` | 主题色 #42b983  |
| PWA     | `_media/manifest.json` | 应用图标、主题色  |

## CONVENTIONS

* 文档使用中文编写
* 目录采用编号前缀：`01-`, `02-`, `03-` 等
* 商业模式文档在 `business/` 目录下
* 图片资源统一放在 `_media/` 目录
* 文档头部包含：版本号、创建日期、作者
* `_sidebar.md` 链接必须用绝对路径（以 `/` 开头）

## ANTI-PATTERNS (THIS PROJECT)

* 无需代码 lint/format 配置（纯文档项目）
* 无需 CI/CD 配置（静态文档站，无 GitHub Actions）
* 无需测试框架（文档项目）
* 禁止在侧边栏链接中使用相对路径

## UNIQUE STYLES

* 采用 Docsify 风格构建静态文档站
* 使用中文标题和内容
* 商业模式文档包含财务模型、谈判策略、执行 SOP
* 五步法框架：needs → solution → business → growth → barriers
* 单元模型和 ROI 方法论体系（L1-L6）

## COMMANDS

```bash
# 本地预览文档站
docsify serve .

# 截图脚本（有语法错误，第19行需修复）
./screenshot_pages.sh
```

## NOTES

* 固件代码在独立仓库，不在此文档站
* 静态网站托管于 GitHub Pages（无自动化部署）
* `.nojekyll` 文件存在，用于跳过 Jekyll 处理
* `screenshot_pages.sh` 有语法错误（line 19: 字符串后有多余 `n`）
* Claude AI 配置在 `.claude/` 目录（rules/ skills/ commands/）
