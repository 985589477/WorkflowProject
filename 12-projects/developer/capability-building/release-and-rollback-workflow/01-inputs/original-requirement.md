# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够长期治理项目开发，并覆盖发布和回滚这种高风险环节。

当前已经完成：

- 第一阶段开发前治理链路。
- 第二阶段开发过程治理链路。
- 第三阶段长期维护中的 ADR、依赖技术债、环境配置治理。

下一步需要解决：发布前如何检查，发布时如何执行，失败后如何回滚，上线后如何观察。

## 本次建设目标

创建“发布与回滚治理工作流”，用于：

1. 明确发布范围。
2. 检查发布前条件。
3. 制定发布步骤。
4. 制定回滚方案。
5. 定义上线后观察。
6. 判断是否建议发布。
7. 将发布异常进入复盘。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/release-and-rollback-workflow.md
06-templates/developer/release-and-rollback-template.md
11-evaluations/output-scorecards/release-and-rollback-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/release-and-rollback-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 生产发布默认高风险。
- 没有回滚方案时不建议发布。
