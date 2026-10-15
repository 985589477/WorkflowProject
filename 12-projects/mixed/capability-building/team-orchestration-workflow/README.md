# 跨角色团队总调度工作流建设项目

状态: completed
角色: mixed
项目类型: capability-building
创建日期: 2026-10-14

## 目标

建设一个跨角色团队总调度能力，用于协调产品经理、UI 设计师、开发工程师、测试工程师按完整团队链路协作。

## 项目职责

这个项目负责沉淀团队级编排规则：当用户提出需求时，判断哪些角色需要参与、谁先接管、如何交接、如何互相验收，以及出现沟通不畅时如何反馈 badcase 并回到对应角色能力项目优化。

## 何时使用

当一个任务不只是单个角色能完成，而是需要产品、UI、开发、测试连续协作时，使用这个项目。

当你要在外部项目中直接使用团队总调度时，优先使用：

```text
04-workflows/mixed/team-orchestration-workflow.md
```

## 关键产物

- `04-workflows/mixed/team-orchestration-workflow.md`
- `06-templates/mixed/team-orchestration-template.md`
- `11-evaluations/output-scorecards/team-orchestration-scorecard.md`

## 角色

混合角色团队总调度。

## 输入材料

用户提出：需要在 mixed 里添加一个项目，用来总调度产品、UI、开发、测试；各角色需要判断是否接管部分任务，并按优先级引导用户推进；角色之间需要互相检查能否看懂、能否验收；如果沟通不畅，需要反馈给用户并作为 badcase 回到项目细分优化。

## 使用的工作流

`04-workflows/mixed/team-orchestration-workflow.md`

## 使用的模板

`06-templates/mixed/team-orchestration-template.md`

## 当前状态

已完成团队总调度能力建设，并提升到全局 mixed 工作流、模板和评分表。

## 下一步

使用一个真实完整需求验证团队总调度，例如从一个产品想法开始，依次检查产品、UI、开发、测试是否能正确接管、交接和互相验收。

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

然后对 AI 说：

```text
请使用 12-projects/mixed/capability-building/team-orchestration-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

## 进度记录

关键执行节点记录到：

```text
00-progress/progress-log.md
```

当前项目状态摘要记录到：

```text
00-progress/memory-summary.md
```

如果项目持续迭代很多轮，优先更新 `memory-summary.md`，不要让 AI 每次读取所有历史记录。

## 沉淀与提升

项目结束时记录哪些内容提升到全局模板、案例、知识库或评估体系。
