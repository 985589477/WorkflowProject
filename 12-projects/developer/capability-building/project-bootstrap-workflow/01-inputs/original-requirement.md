# 原始需求

## 背景

developer-kit 的开发治理能力体系已完成第一版。

下一步需要建设第一条可执行工作流：

```text
project-bootstrap-workflow
```

该工作流用于新项目启动时，让 AI 检查并补齐项目基础开发治理规范，避免项目从一开始就缺少结构、文档、AI 协作规则和质量标准。

## 核心目标

当用户在一个新项目中使用 Codex 或 Cursor 时，希望 AI 能主动判断：

- 当前项目是否有清晰的项目说明。
- 是否有 AI 协作规则。
- 是否有开发规范。
- 是否有文档目录。
- 是否有架构目录。
- 是否有测试和构建命令。
- 是否有环境变量说明。
- 是否有模块结构说明。
- 是否需要创建 `AGENTS.md`、`.cursor/rules/`、`docs/` 等协作文件。

## 期望输出

本项目需要产出：

- 新项目启动治理工作流。
- 新项目启动模板。
- 新项目启动评分表。

并沉淀到全局目录：

```text
04-workflows/developer/
06-templates/developer/
11-evaluations/output-scorecards/
```
