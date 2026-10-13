# 原始需求

## 用户原始描述

```text
我想要通过刚刚的idea-to-input-generator重新做一遍product-mamager-workflow
```

## 背景

用户已经完成了一版 `product-manager-workflow` 项目，并在后续使用中发现一个新的关键问题：

```text
生成 input 本身也有成本。
```

因此，项目新增了：

```text
04-workflows/common/idea-to-input-workflow.md
06-templates/meta/idea-to-input-generator.md
```

现在用户希望用这个新能力重新跑一遍产品经理工作流项目，验证“模糊想法 -> 标准 input -> 后续输出”的链路是否真的可用。

## 目标

用 `idea-to-input-generator` 作为前置步骤，重新生成一版产品经理通用工作流。

本项目不仅要产出工作流，还要验证：

1. 用户只给一句模糊描述时，是否能稳定生成标准 input。
2. 标准 input 是否能继续支撑输入分析、正式提示词和最终输出。
3. 新生成的产品经理工作流是否比上一版更清楚地覆盖“想法转输入”阶段。
4. 当前框架是否需要继续优化项目入口。

## 已知事实

- 用户已经有一个上一版项目：

```text
12-projects/product-manager/capability-building/product-manager-workflow/
```

- 上一版已沉淀全局产品经理工作流：

```text
04-workflows/product-manager/product-manager-workflow.md
```

- 当前新增了想法转输入能力：

```text
04-workflows/common/idea-to-input-workflow.md
06-templates/meta/idea-to-input-generator.md
```

- 用户希望“重新做一遍”，不是单纯修改文字，而是验证新的前置链路。

## 原始材料

本次原始材料主要是用户的一句话描述，以及当前项目已有资产：

```text
我想要通过刚刚的idea-to-input-generator重新做一遍product-mamager-workflow
```

可参考资产：

```text
04-workflows/common/idea-to-input-workflow.md
06-templates/meta/idea-to-input-generator.md
04-workflows/product-manager/product-manager-workflow.md
12-projects/product-manager/capability-building/product-manager-workflow/
```

## 约束条件

- 正文默认使用中文。
- 必须明确区分用户事实、AI 推断和待确认信息。
- 本次应从 `idea-to-input-generator` 开始，而不是跳过 input 直接产出 workflow。
- 不应破坏上一版项目记录。
- 如需沉淀到全局，应先评审再更新。

## AI 推断

- `product-mamager-workflow` 应为 `product-manager-workflow` 的输入拼写错误。
- 用户希望验证的是“项目入口能力”，也就是从模糊描述到标准 input 的稳定性。
- 新版产品经理工作流应显式加入“想法转输入”作为前置步骤。
- 本项目适合新建为独立项目，避免覆盖上一版验证记录。

## 待确认信息

- 是否最终覆盖全局 `04-workflows/product-manager/product-manager-workflow.md`。
- 是否需要把本次项目沉淀为案例。
- 后续是否要继续用一个真实 PRD 项目验证新版产品经理工作流。

## 推荐项目归属

推荐角色：

```text
product-manager
```

推荐项目名：

```text
product-manager-workflow
```

推荐项目路径：

```text
12-projects/product-manager/capability-building/product-manager-workflow/
```

## 推荐后续流程

```text
04-workflows/common/idea-to-input-workflow.md
-> 04-workflows/common/input-analysis-workflow.md
-> 06-templates/meta/prompt-generator.md
-> 06-templates/meta/output-reviewer.md
-> 04-workflows/common/asset-promotion-workflow.md
```
