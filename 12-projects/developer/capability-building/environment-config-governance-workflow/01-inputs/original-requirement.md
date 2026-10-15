# 原始需求

## 用户背景

用户正在建设 developer-kit，希望 AI 能长期维护项目，不只管代码，还要管环境、配置、构建和部署相关风险。

当前已经完成：

- 第一阶段开发前治理链路。
- 第二阶段开发过程治理链路。
- 架构决策记录工作流。
- 依赖与技术债治理工作流。

下一步需要解决：环境变量、启动命令、构建配置、部署配置和不同环境差异如何被 AI 稳定管理。

## 本次建设目标

创建“环境与配置治理工作流”，用于：

1. 识别配置对象。
2. 梳理现有配置。
3. 输出配置项清单。
4. 记录环境差异。
5. 识别敏感信息、生产、安全、构建和部署风险。
6. 给出治理方案、验证要求、回滚要求和文档同步建议。

## 输出要求

需要沉淀为全局可复用资产：

```text
04-workflows/developer/environment-config-governance-workflow.md
06-templates/developer/environment-config-governance-template.md
11-evaluations/output-scorecards/environment-config-governance-scorecard.md
```

同时保留项目记录：

```text
12-projects/developer/capability-building/environment-config-governance-workflow/
```

## 约束

- 文档主体使用中文。
- 英文保留在路径、命令、文件名和技术名中。
- 不得写入真实密钥或敏感信息。
- 生产、安全、权限、支付、数据相关配置必须高风险处理。
