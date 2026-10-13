# 正式提示词

你是一名资深产品经理与 AI 协作工作流架构师。

请基于以下背景，生成一份“需求分析工作流”。

## 背景

当前已经有产品经理能力体系：

```text
10-knowledge-base/patterns/product-manager-capability-system.md
```

能力体系推荐优先建设需求分析能力，因为需求分析是 PRD、功能规划和验收标准的上游能力。

当前也已经有产品经理总入口工作流：

```text
04-workflows/product-manager/product-manager-workflow.md
```

现在需要生成一个细分工作流：

```text
04-workflows/product-manager/requirement-analysis-workflow.md
```

## 任务目标

输出一份可复用的产品经理需求分析工作流。

## 输出结构

请按照以下结构输出：

```md
# 需求分析工作流

## 目的

## 适用场景

## 输入要求

## 执行步骤

## 输出结果

## 质量检查

## 常见分支

## 使用注意事项
```

## 内容要求

1. 默认使用中文。
2. 符合 `05-standards/workflow-standard.md`。
3. Workflow 描述方法，不直接替代 prompt。
4. 明确需求分析和 PRD 的边界。
5. 每个关键步骤要说明输入、处理动作和产出。
6. 明确输出保存路径。
7. 支持模糊想法、已有需求、用户反馈、会议纪要等不同输入。
8. 明确事实、AI 推断、待确认信息必须分开。
9. 产物要能作为 PRD、功能规划和验收标准的上游输入。

## 质量标准

- 结构完整。
- 可执行。
- 可复用。
- 与当前目录体系一致。
- 能降低用户从想法到需求分析的使用成本。
