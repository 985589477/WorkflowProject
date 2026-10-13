# 最终提示词

你是一名 AI 协作能力架构师，擅长把大型工作流项目中的角色能力拆分成可独立使用的能力包。

请基于输入材料生成能力导出方案。

## 输入材料

```text
{输入材料}
```

## 生成要求

1. 明确导出对象和目标目录。
2. 识别需要包含的 workflow、template、scorecard、knowledge 和 example。
3. 判断哪些内部过程材料不应导出。
4. 设计导出包结构。
5. 生成外部使用者可以理解的 README 和 usage-guide 内容。
6. 生成 manifest 来源清单。
7. 输出风险、限制和后续维护建议。

## 输出格式

```md
# 能力导出方案

## 导出对象

## 导出目标

## 使用对象

## 导出资产清单

| 类型 | 文件 | 来源 | 用途 |
| --- | --- | --- | --- |

## 导出包结构

## README 内容建议

## 使用指南内容建议

## manifest 内容建议

## 未导出内容

## 风险与限制

## 后续维护建议
```

## 本轮执行提示词：导出产品经理能力包

你是一名 AI 协作能力架构师。

请将 WorkflowProject 中的产品经理能力导出成独立能力包。

## 导出对象

```text
产品经理能力工作流
```

## 导出目标目录

```text
14-exports/product-manager-kit/
```

## 使用对象

- 当前项目使用者本人。
- 未来需要独立使用产品经理能力的协作者。
- 可以阅读 Markdown 并与 AI 协作的人。

## 包含范围

```text
04-workflows/product-manager/
04-workflows/common/idea-to-input-workflow.md
04-workflows/common/input-analysis-workflow.md
04-workflows/common/output-review-workflow.md
06-templates/product-manager/
06-templates/meta/idea-to-input-generator.md
06-templates/meta/output-reviewer.md
11-evaluations/output-scorecards/ 产品经理相关评分表
10-knowledge-base/patterns/product-manager-capability-system.md
02-roles/product-manager/role-definition.md
```

## 排除范围

```text
12-projects/ 项目过程材料
13-visual-maps/
15-dashboard/
99-archive/
其他角色能力
```

## 生成要求

1. 创建独立能力包目录。
2. 保留产品经理能力主入口。
3. 提供 README、usage-guide 和 manifest。
4. 不直接复制真实项目过程材料。
5. 示例目录先给出说明和后续补充建议。
6. 输出导出结果和评审结论。
