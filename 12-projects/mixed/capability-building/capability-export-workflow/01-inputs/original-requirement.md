# 原始需求

## 用户想法

用户希望把当前 WorkflowProject 中已经产出的某个角色能力拆分出去，形成专门给产品、开发或 UI 使用的独立能力包。

## 背景

当前 WorkflowProject 已经沉淀了大量角色能力，尤其是产品经理能力。

这些能力现在散落在：

```text
04-workflows/
06-templates/
10-knowledge-base/
11-evaluations/
12-projects/
```

如果后续要给某个角色单独使用，不能要求对方理解整个 WorkflowProject，也不应该直接复制整个项目。

## 目标

建设一个通用的能力导出工作流，用于把当前项目内稳定能力整理成独立能力包。

## 预期沉淀

```text
14-exports/
04-workflows/common/capability-export-workflow.md
06-templates/common/capability-export-template.md
11-evaluations/output-scorecards/capability-export-scorecard.md
```

## 本轮继续需求

用户希望使用本项目继续执行第一次真实导出：

```text
我想要导出产品经理能力工作流
```

本轮导出目标：

```text
14-exports/product-manager-kit/
```

本轮要求：

- 按项目流程更新 input、analysis、prompt、output、review 和 lessons。
- 使用已经沉淀的能力导出工作流。
- 导出产品经理能力工作流和相关支撑文件。
