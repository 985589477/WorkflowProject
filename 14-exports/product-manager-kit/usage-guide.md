# 使用指南

导出时间：2026-10-13

## 最快启动

在新项目或新 AI 对话里复制：

```text
请只参考 product-manager-kit/ 下的文件工作。请先阅读 product-manager-kit/README.md、product-manager-kit/usage-guide.md 和 product-manager-kit/workflows/product-manager/product-manager-workflow.md。我的产品想法是：{写下你的想法}。请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard，然后继续产出结果。
```

## 第一步：判断你现在要做什么

如果你不确定，使用：

```text
workflows/product-manager/product-manager-workflow.md
```

它会帮你判断应该进入哪个细分工作流。

## 第二步：选择对应工作流

| 你想做什么 | 使用文件 |
| --- | --- |
| 把想法整理成标准输入 | `workflows/common/idea-to-input-workflow.md` |
| 分析需求 | `workflows/product-manager/requirement-analysis-workflow.md` |
| 写 PRD | `workflows/product-manager/prd-generation-workflow.md` |
| 写验收标准 | `workflows/product-manager/acceptance-criteria-workflow.md` |
| 拆功能范围 | `workflows/product-manager/feature-planning-workflow.md` |
| 写用户故事 | `workflows/product-manager/user-story-workflow.md` |
| 整理用户反馈 | `workflows/product-manager/user-feedback-workflow.md` |
| 分析竞品 | `workflows/product-manager/competitor-analysis-workflow.md` |
| 判断优先级 | `workflows/product-manager/priority-decision-workflow.md` |
| 规划版本 | `workflows/product-manager/version-planning-workflow.md` |
| 判断方向是否值得做 | `workflows/product-manager/product-strategy-workflow.md` |
| 管理需求池 | `workflows/product-manager/requirement-pool-workflow.md` |
| 做产品路线图 | `workflows/product-manager/product-roadmap-workflow.md` |
| 评估需求变更 | `workflows/product-manager/requirement-change-evaluation-workflow.md` |
| 做版本复盘 | `workflows/product-manager/version-retrospective-workflow.md` |

## 第三步：使用模板生成结果

每个产品经理工作流通常对应一个模板：

```text
templates/product-manager/
```

例如：

```text
prd-generation-workflow.md
-> prd-template.md
-> prd-scorecard.md
```

## 第四步：用评分表检查结果

生成结果后，到：

```text
scorecards/
```

选择对应评分表检查输出是否合格。

## 第五步：决定是否保存文件

如果只是让 AI 在对话里输出结果，不需要创建文件。

如果你希望把结果保存到当前项目，请按下面顺序选择输出位置：

1. 用户明确指定输出目录时，使用用户指定目录。
2. 当前项目已有统一文档目录时，使用已有目录，例如 `docs/`、`documents/`、`产品文档/`、`需求文档/`。
3. 当前项目已有产品文档目录时，使用该目录，例如 `docs/product/`、`docs/prd/`、`product-docs/`。
4. 如果没有合适目录，再在项目根目录创建 `docs/`。

不要把 WorkflowProject 内部目录习惯带到外部项目，不要默认创建：

```text
04-outputs/
12-projects/
```

## 推荐执行方式

对 AI 说：

```text
请先阅读以下文件：
1. workflows/product-manager/product-manager-workflow.md
2. knowledge/product-manager-capability-system.md

我的任务是：{你的任务}

请先判断任务类型，再说明会使用哪个 workflow、template 和 scorecard。
```

## 导出时间管理

本能力包不使用版本号。

判断是否是最新包时，只看：

```text
导出时间
```

导出时间记录在：

```text
START-HERE.md
README.md
manifest.md
```

## 不建议的用法

- 不要一上来让 AI 直接写 PRD，除非你已经有清晰需求分析。
- 不要把用户反馈直接变成版本规划，应先整理反馈和判断优先级。
- 不要在需求变更时直接修改 PRD，应先做变更评估。
- 不要把复盘写成泛泛总结，应对比原计划和实际结果。
