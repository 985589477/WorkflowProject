# WorkflowProject 框架启动项目

状态: reviewed
角色: mixed
项目类型: capability-building
创建日期: 2026-10-12

## 目标

将 WorkflowProject 当前项目本身作为第一个真实项目，验证“从原始需求到框架输出、评审、复盘、沉淀”的完整工作流程。

## 角色

本项目属于跨角色任务，主要使用以下 AI 协作角色：

- AI 文档工程师
- AI 工作流架构师
- AI 提示词体系设计师
- AI 项目治理顾问

## 输入材料

输入来自用户围绕 WorkflowProject 的连续需求澄清：

- 希望构建一个类似工作流的文档项目。
- 希望通过文档输出可提供给 AI 的输入输出标准提示词文档。
- 希望支持产品经理、程序员、UI 设计等多角色。
- 希望不仅有流程，还要有项目管控规范。
- 希望生成 XMind 思维导图辅助理解。
- 希望把当前 WorkflowProject 框架本身作为第一个项目。

## 使用的工作流

本项目使用并验证了以下通用工作流：

- `04-workflows/common/input-analysis-workflow.md`
- `04-workflows/common/template-generation-workflow.md`
- `04-workflows/common/prompt-generation-workflow.md`
- `04-workflows/common/output-review-workflow.md`
- `04-workflows/common/example-extraction-workflow.md`
- `04-workflows/common/template-iteration-workflow.md`

## 使用的模板

本项目产生并使用了以下 meta 模板能力：

- `06-templates/meta/template-generator.md`
- `06-templates/meta/prompt-generator.md`
- `06-templates/meta/output-reviewer.md`
- `06-templates/meta/example-extractor.md`
- `06-templates/meta/template-optimizer.md`

## 当前状态

当前项目已完成第一轮框架搭建和自检。

## 沉淀与提升

本项目已直接产生全局框架资产：

- `00-system/`
- `01-governance/`
- `02-roles/`
- `03-inputs/`
- `04-workflows/`
- `05-standards/`
- `06-templates/`
- `07-prompts/`
- `08-outputs/`
- `09-examples/`
- `10-knowledge-base/`
- `11-evaluations/`
- `12-projects/project-template/`
- `99-archive/`

后续可将本项目整理为 `09-examples/cross-functional/` 下的第一个完整案例包。
