# 原始需求

## 用户原始描述

```text
请使用 12-projects/product-manager/capability-building/product-manager-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。我现在想要做一个作为产品经理后续的能力细分的项目，而不是单纯的通过一个文档输出，需要一个体系，作为产品经理的体系
```

## 背景

当前已经完成产品经理通用工作流，并沉淀到：

```text
04-workflows/product-manager/product-manager-workflow.md
```

用户现在希望继续往下建设产品经理角色，但不是简单再生成某个单独文档，而是规划一个可以持续扩展的“产品经理能力体系”。

## 目标

构建一套产品经理能力细分体系，用来回答：

1. 产品经理角色后续应该拆成哪些能力模块。
2. 每个能力模块可以对应哪些 workflow、template、example 和 evaluation。
3. 哪些能力应该优先建设，哪些可以后置。
4. 后续每个能力如何作为独立项目推进。
5. 如何避免只堆文档，而是形成可持续扩展的体系。

## 已知事实

- 已有产品经理通用工作流。
- 用户已经理解项目可以通过 `12-projects/` 跑真实项目，再沉淀到全局目录。
- 用户不希望只得到一个单点文档输出。
- 用户希望形成“产品经理体系”。

## 原始材料

可参考：

```text
04-workflows/product-manager/product-manager-workflow.md
12-projects/product-manager/capability-building/product-manager-workflow/
06-templates/meta/idea-to-input-generator.md
04-workflows/common/idea-to-input-workflow.md
```

## 约束条件

- 输出应是体系规划，不是单篇工作流。
- 体系要能指导后续项目拆分。
- 默认使用中文。
- 不要一次性把所有细分文档都写完。
- 要明确优先级和建设顺序。
- 要能进入后续全局沉淀，例如知识库、工作流目录或角色目录。

## AI 推断

- 用户需要的是“产品经理角色能力地图”。
- 这个能力地图应包含能力模块、产物类型、后续项目建议和沉淀位置。
- 本项目可以作为产品经理体系建设的上层规划项目。
- 最终产物适合沉淀到 `10-knowledge-base/` 或 `02-roles/product-manager/`，也可能补充 `04-workflows/product-manager/README.md`。

## 待确认信息

- 用户更偏向互联网产品经理、AI 产品经理、工具型产品经理，还是通用产品经理。
- 是否要纳入团队协作能力，例如和 UI、开发、运营的协作。
- 是否要为每个能力模块后续生成独立 workflow。

## 推荐项目归属

推荐角色：

```text
product-manager
```

推荐项目名：

```text
product-manager-capability-system
```

推荐路径：

```text
12-projects/product-manager/capability-building/product-manager-capability-system/
```

## 推荐后续流程

```text
04-workflows/product-manager/product-manager-workflow.md
-> 04-workflows/common/input-analysis-workflow.md
-> 06-templates/meta/prompt-generator.md
-> 06-templates/meta/output-reviewer.md
-> 04-workflows/common/asset-promotion-workflow.md
```
