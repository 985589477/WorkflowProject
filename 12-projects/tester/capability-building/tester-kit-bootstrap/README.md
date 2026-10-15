# 测试工程师能力包启动项目

状态: completed
角色: tester
项目类型: capability-building
创建日期: 2026-10-14

## 目标

建设并细化测试工程师角色能力包。

## 项目职责

这个项目负责启动并细化测试角色能力体系，沉淀总入口、细分工作流、模板、评分表和导出包。

## 何时使用

当你要继续完善测试角色、拆分缺陷复现、回归测试、发布验收等细分能力时，使用这个项目。

当你要执行一次具体测试任务时，优先使用：

```text
14-exports/tester-kit/START-HERE.md
```

## 关键产物

- `04-workflows/tester/tester-workflow.md`
- `04-workflows/tester/test-scope-analysis-workflow.md`
- `04-workflows/tester/test-case-design-workflow.md`
- `04-workflows/tester/regression-test-workflow.md`
- `04-workflows/tester/defect-reproduction-workflow.md`
- `04-workflows/tester/release-acceptance-workflow.md`
- `06-templates/tester/`
- `11-evaluations/output-scorecards/*test*`
- `05-standards/quality-checklists/tester-checklist.md`
- `14-exports/tester-kit/`

## 角色

测试工程师。

## 输入材料

用户提出需要建设测试角色。

## 使用的工作流

`04-workflows/tester/tester-workflow.md`

## 使用的模板

`06-templates/tester/test-plan-template.md`

## 当前状态

已完成测试治理能力版，并补齐验收标准检查、测试策略规划、测试数据与环境准备、接口与集成测试、兼容性测试、非功能风险测试、探索式测试、自动化测试规划、测试执行报告能力，已同步到 `14-exports/tester-kit/`。

## 下一步

使用一个真实 PRD、开发变更或缺陷案例验证 `tester-kit`，重点检查是否能先确认验收标准、测试策略、测试环境、接口集成、兼容性和非功能风险，再进入用例设计或发布判断。

## 如何启动

下次继续本项目时，先阅读：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

然后对 AI 说：

```text
请使用 12-projects/tester/capability-building/tester-kit-bootstrap 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
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
