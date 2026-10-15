# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 不只是一次性执行任务，还能在协作中不断复盘、沉淀和改进规则。

当前已经完成：

- 第一阶段开发前治理链路。
- 第二阶段开发过程治理链路。
- 第三阶段长期维护中的 ADR、依赖技术债、环境配置、发布回滚治理。

下一步需要解决：AI 协作中出现误判、越界、漏测、文档遗漏、发布异常时，如何把问题沉淀为后续规则。

## 本次建设目标

创建“AI 协作复盘工作流”，用于：

1. 整理复盘事实。
2. 分类 AI 协作问题。
3. 分析根因。
4. 判断是否需要沉淀。
5. 生成具体改进动作。
6. 指定需要更新的文件或规则。
7. 定义后续验证方式。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/ai-collaboration-retrospective-workflow.md
06-templates/developer/ai-collaboration-retrospective-template.md
11-evaluations/output-scorecards/ai-collaboration-retrospective-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/ai-collaboration-retrospective-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 复盘必须基于事实证据。
- 改进动作必须具体可执行。
