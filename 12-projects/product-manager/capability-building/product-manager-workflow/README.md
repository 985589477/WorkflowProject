# 产品经理任务总入口项目

状态: draft
角色: product-manager
项目类型: capability-building
创建日期: 2026-10-12

## 项目职责

这个项目负责生成并验证“产品经理任务总入口工作流”。

它承担的职责不是输出某个具体 PRD，而是定义后续所有产品经理任务如何从一句想法开始，进入标准 input、输入分析、正式提示词、输出、评审和沉淀。

## 何时使用

当你有一个具体产品任务，但还不确定应该走需求分析、PRD、功能规划还是验收标准时，先使用这个项目沉淀出的全局工作流。

典型场景：

- 我有一个产品想法，不知道怎么整理。
- 我想生成 PRD，但还没有标准输入。
- 我想让 AI 帮我判断这个产品任务下一步该走哪个能力。
- 我想启动一个产品经理项目，但不知道应该调用哪个细分 workflow。

## 目标

通过 `idea-to-input-generator` 从用户一句模糊描述开始，重新生成产品经理通用工作流，并验证“模糊想法 -> 标准 input -> 后续输出”的完整链路。

## 关键产物

- 项目输出：`04-outputs/product-manager-workflow-v2-output.md`
- 全局沉淀：`04-workflows/product-manager/product-manager-workflow.md`
- 作用定位：产品经理任务总入口 / 能力调度入口

## 和能力体系的关系

`product-manager-workflow` 负责执行时调度。

`product-manager-capability-system` 负责规划产品经理能力版图。

简单判断：

```text
我要开始一个具体产品任务 -> 用 product-manager-workflow
我要决定产品经理体系下一步建设什么 -> 用 product-manager-capability-system
```

## 角色

主要角色：

- AI 协作需求澄清与输入整理专家。
- 产品经理工作流架构师。
- 输出质量评审专家。

## 输入材料

输入来自用户原始描述：

```text
我想要通过刚刚的idea-to-input-generator重新做一遍product-mamager-workflow
```

已通过 `idea-to-input-generator` 整理为：

```text
01-inputs/original-requirement.md
```

## 使用的工作流

- `04-workflows/common/idea-to-input-workflow.md`
- `04-workflows/common/input-analysis-workflow.md`
- `04-workflows/common/asset-promotion-workflow.md`

## 使用的模板

- `06-templates/meta/idea-to-input-generator.md`
- `06-templates/meta/prompt-generator.md`
- `06-templates/meta/output-reviewer.md`

## 当前状态

已完成。

本项目完成了：

- 从用户一句话生成标准 input。
- 基于标准 input 完成输入分析。
- 生成正式提示词。
- 生成产品经理工作流 v2。
- 完成输出评审。
- 将 v2 提升到全局产品经理工作流。

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

已将本项目输出提升到：

```text
04-workflows/product-manager/product-manager-workflow.md
```

本项目后续可整理为“想法转输入”案例。
