# 能力导出工作流建设项目

状态: completed
角色: mixed
项目类型: capability-building
创建日期: 2026-10-13

## 目标

建设 WorkflowProject 的能力导出工作流。

本项目负责把当前项目中已经沉淀稳定的角色能力或专项能力，整理成可以脱离 WorkflowProject 独立使用的能力包。

## 项目职责

这个项目负责定义“如何导出能力包”，不是直接导出某一个具体能力包。

后续导出产品经理、开发、UI 或测试能力时，使用本项目沉淀出的通用工作流。

## 角色

- WorkflowProject 架构师。
- AI 协作能力架构师。
- 输出质量评审专家。

## 输入材料

- 当前 WorkflowProject 的目录结构。
- 已沉淀的产品经理能力体系。
- 用户关于角色能力拆分和外部使用的需求。

## 使用的工作流

- `04-workflows/common/asset-promotion-workflow.md`

## 使用的模板

- `06-templates/meta/output-reviewer.md`

## 当前状态

已完成第一版，并已完成第一次真实导出验证准备。

本项目已新增 `14-exports/` 导出区，并沉淀能力导出工作流、模板和评分表。

已导出：

```text
14-exports/product-manager-kit/
```

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

然后对 AI 说：

```text
请继续推进这个项目，并先说明当前状态、推荐下一步和会使用哪些文件。
```

## 进度记录

关键执行节点记录到：

```text
00-progress/progress-log.md
```

## 沉淀与提升

已提升：

```text
14-exports/README.md
04-workflows/common/capability-export-workflow.md
06-templates/common/capability-export-template.md
11-evaluations/output-scorecards/capability-export-scorecard.md
```
