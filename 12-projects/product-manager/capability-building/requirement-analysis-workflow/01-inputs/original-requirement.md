# 原始需求

## 用户原始描述

```text
请使用 12-projects/product-manager/capability-building/product-manager-capability-system 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。我需要按照当前项目规划的下一步继续做
```

## 背景

`product-manager-capability-system` 已完成产品经理能力体系规划，并明确推荐下一步：

```text
优先启动需求分析工作流项目。
```

原因：

```text
需求分析是 PRD、功能规划和验收标准的上游能力。
```

## 目标

创建并完成一个需求分析工作流建设项目，输出一份可沉淀到全局目录的产品经理需求分析工作流。

## 已知事实

- 产品经理能力体系已经沉淀到：

```text
10-knowledge-base/patterns/product-manager-capability-system.md
```

- 产品经理总入口工作流已经存在：

```text
04-workflows/product-manager/product-manager-workflow.md
```

- 产品经理工作流目录目前还没有需求分析细分工作流。
- 能力体系明确需求分析属于第一阶段优先建设能力。

## 原始材料

主要参考：

```text
10-knowledge-base/patterns/product-manager-capability-system.md
04-workflows/product-manager/product-manager-workflow.md
05-standards/workflow-standard.md
```

## 约束条件

- 输出应是 workflow，不是 prompt。
- 工作流必须符合 `05-standards/workflow-standard.md`。
- 工作流要能指导后续真实产品任务进行需求分析。
- 不要一次性生成 PRD、验收标准或其他能力。
- 正文默认使用中文。

## AI 推断

- 本项目应沉淀到：

```text
04-workflows/product-manager/requirement-analysis-workflow.md
```

- 后续还可能需要建设：

```text
06-templates/product-manager/requirement-analysis-template.md
11-evaluations/output-scorecards/requirement-analysis-scorecard.md
```

但本项目优先完成 workflow。

## 待确认信息

- 是否本次同步生成需求分析模板。
- 是否本次同步生成需求分析评分表。
- 需求分析是否偏通用产品经理，还是偏 AI 产品经理。

## 推荐项目归属

推荐角色：

```text
product-manager
```

推荐项目名：

```text
requirement-analysis-workflow
```

推荐路径：

```text
12-projects/product-manager/capability-building/requirement-analysis-workflow/
```

## 推荐后续流程

```text
04-workflows/common/input-analysis-workflow.md
-> 06-templates/meta/prompt-generator.md
-> 06-templates/meta/output-reviewer.md
-> 04-workflows/common/asset-promotion-workflow.md
```
