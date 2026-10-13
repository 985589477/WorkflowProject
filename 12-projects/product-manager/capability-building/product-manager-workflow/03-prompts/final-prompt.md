# 正式提示词

你是一名资深产品经理工作流架构师，同时熟悉 AI 协作文档工程。

请基于以下背景，重新生成一份“产品经理通用工作流 v2”。

## 背景

WorkflowProject 已经有一版产品经理通用工作流，但用户发现一个关键问题：

```text
很多真实项目一开始没有标准 input，只有模糊想法。
```

因此项目新增了：

```text
04-workflows/common/idea-to-input-workflow.md
06-templates/meta/idea-to-input-generator.md
```

现在需要重新生成产品经理工作流，把“想法转输入”作为产品经理任务的正式前置步骤。

## 用户原始描述

```text
我想要通过刚刚的idea-to-input-generator重新做一遍product-mamager-workflow
```

## 本次任务

生成一份新版产品经理通用工作流，用于指导后续产品类任务从模糊想法开始，逐步形成标准输入、输入分析、正式提示词、产品输出、评审和沉淀。

## 输出结构

请按照以下结构输出：

```md
# 产品经理通用工作流

## 目的

## 适用场景

## 输入来源

## 执行步骤

## 输出结果

## 质量检查

## 常见分支

## 使用注意事项
```

## 必须体现的变化

1. 增加“第 0 步：想法转输入”。
2. 明确 `idea-to-input-generator` 的使用场景。
3. 明确标准 input 应保存到 `01-inputs/original-requirement.md`。
4. 明确后续再进入 `input-analysis-workflow`。
5. 说明事实、AI 推断、待确认信息必须分开。
6. 保持与当前目录体系一致。
7. 默认使用中文。

## 质量标准

输出必须：

- 结构完整。
- 可以直接沉淀到 `04-workflows/product-manager/product-manager-workflow.md`。
- 能降低用户准备 input 的成本。
- 能指导后续真实产品项目。
- 不把 workflow 写成 prompt。
