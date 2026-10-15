# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能够长期维护项目，避免为了短期开发速度留下不可控依赖和技术债。

当前已经完成：

- 第一阶段开发前治理链路。
- 第二阶段开发过程治理链路。
- 架构决策记录工作流。

下一步需要解决：AI 在新增依赖、使用临时方案、发现技术债时，如何判断必要性、风险、偿还计划和是否需要 ADR。

## 本次建设目标

创建“依赖与技术债治理工作流”，用于：

1. 判断依赖或技术债治理对象。
2. 判断新增依赖或技术债处理的必要性。
3. 比较备选方案。
4. 评估安全、许可证、维护、体积、性能和兼容性风险。
5. 记录技术债和偿还条件。
6. 给出验证、回滚和 ADR 判断。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/dependency-and-tech-debt-workflow.md
06-templates/developer/dependency-and-tech-debt-template.md
11-evaluations/output-scorecards/dependency-and-tech-debt-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/dependency-and-tech-debt-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 新增依赖必须说明必要性。
- 临时方案必须记录还债条件。
