# 从这里开始

导出对象：产品经理能力包
导出时间：2026-10-13

## 这个包能做什么

- 把模糊产品想法整理成可执行需求。
- 生成需求分析、PRD、用户故事和验收标准。
- 拆分功能范围、判断优先级、规划版本和路线图。
- 整理用户反馈、分析竞品、评估需求变更。
- 辅助产品策略判断、需求池管理和版本复盘。

## 什么时候使用这个包

当用户输入包含以下意图时，优先使用本能力包：

- 产品想法梳理。
- 需求分析。
- PRD 生成。
- 功能范围拆分。
- 用户故事。
- 验收标准。
- 用户反馈整理。
- 竞品分析。
- 优先级判断。
- 版本规划。
- 产品策略判断。
- 需求池管理。
- 产品路线图。
- 需求变更评估。
- 版本复盘。

## 一句话启动

在新项目或新 AI 对话里，直接复制下面这句话：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/README.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。我的任务是：{写下你的任务}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 更短版本

如果只是快速启动，可以说：

```text
请使用 product-manager-kit 处理我的任务：{写下你的任务}
```

## 外部自动读取配置

如果希望用户不输入“请使用 product-manager-kit”，可以在新项目根目录放置默认读取文件，例如：

```text
AI-WORKFLOW-RULES.md
```

并在文件里写入：

```text
你是当前项目的 AI 工作流调度器。

当用户输入任务时，请先判断是否属于产品经理能力范围。

如果用户输入包含以下意图之一，请自动调用 product-manager-kit：
- 产品想法梳理
- 需求分析
- PRD 生成
- 功能范围拆分
- 用户故事
- 验收标准
- 用户反馈整理
- 竞品分析
- 优先级判断
- 版本规划
- 产品策略判断
- 需求池管理
- 产品路线图
- 需求变更评估
- 版本复盘

触发 product-manager-kit 后，请先阅读：
1. product-manager-kit/START-HERE.md
2. product-manager-kit/README.md
3. product-manager-kit/usage-guide.md
4. product-manager-kit/workflows/product-manager/product-manager-workflow.md

执行前请先说明：
- 你判断这是哪一类产品任务。
- 你将使用哪个 workflow。
- 你将参考哪个 template。
- 你将使用哪个 scorecard 检查结果。

如果用户输入不属于产品经理任务，请不要强行调用 product-manager-kit，应继续判断是否需要其他能力包。
如果无法判断任务类型，请先向用户确认。
```

配置完成后，用户可以直接输入：

```text
我想做一个 AI 提示词模板管理工具，帮我梳理一下需求。
```

AI 应自动判断这是产品需求类任务，并进入 `product-manager-kit`。

## 执行顺序

1. 先判断任务类型。
2. 再选择对应 workflow。
3. 再选择对应 template。
4. 产出结果后使用对应 scorecard 检查。
5. 如果信息不足，先列出待确认问题。

## 外部项目输出目录策略

当本能力包在其他项目中使用，并且用户要求把结果保存为文件时，必须先判断当前项目是否已有统一文档目录。

优先级如下：

1. 如果用户明确指定输出目录，使用用户指定目录。
2. 如果项目已有统一文档目录，优先使用该目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 如果项目已有明确的产品文档目录，优先使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有任何合适目录，再在项目根目录创建 `docs/`。

不要在外部项目中默认创建或使用 WorkflowProject 内部目录，例如：

```text
04-outputs/
12-projects/
```

如果只是对话中直接输出结果，不需要创建文件。

## 输出确认格式

每次执行前，先输出：

```text
任务判断：{任务类型}
调用能力包：product-manager-kit
使用工作流：{workflow}
使用模板：{template}
检查标准：{scorecard}
保存位置：{对话直接输出 / 用户指定目录 / 已有文档目录 / docs/}
```

## 使用原则

- 不确定做什么时，先走总入口。
- 已经明确任务时，直接指定对应工作流。
- 生成结果后，用对应评分表检查。
- 不需要理解原 WorkflowProject。
