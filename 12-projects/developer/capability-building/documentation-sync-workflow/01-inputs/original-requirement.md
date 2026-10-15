# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 在项目开发中不只完成代码修改，还能维护项目长期可理解性。

当前已经完成：

- 第一阶段开发前治理链路。
- 代码实现执行工作流。
- 测试与验收工作流。

下一步需要解决：代码实现和验证完成后，AI 如何判断 README、AGENTS、docs、API、架构、模块和配置文档是否需要同步。

## 本次建设目标

创建“文档同步工作流”，用于：

1. 基于真实变更事实判断文档影响。
2. 判断哪些文档需要同步。
3. 选择同步策略。
4. 执行最小必要文档更新。
5. 检查路径、命令、模块名和 API 是否一致。
6. 输出文档同步报告。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/documentation-sync-workflow.md
06-templates/developer/documentation-sync-template.md
11-evaluations/output-scorecards/documentation-sync-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/documentation-sync-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 不得大范围重写无关文档。
- 不得把推断写成事实。
