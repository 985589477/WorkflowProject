# 项目架构

## 总体定位

WorkflowProject 首先是面向 AI 协作开发的项目治理约束框架，其次才是角色能力和提示词资产的生产框架。

真实项目的主链路是：

```text
项目规则和事实
-> 架构与模块治理
-> 设计规范检查
-> 整体规划和任务列表
-> 逐条实现与验证
-> 文档同步和复盘
```

角色、工作流、模板和评分表是按需调用的工具，不是所有任务都必须经过的固定流水线。

## 能力资产生产链路

```text
03-inputs
-> 04-workflows
-> 06-templates
-> 07-prompts
-> 08-outputs
-> 11-evaluations
-> 09-examples
-> 10-knowledge-base
-> 14-exports
```

## 分层说明

### 系统层

系统层定义项目如何存在。

- `00-system/`：项目愿景、架构、术语、命名、生命周期、操作指南。
- `01-governance/`：变更管理、评审流程、质量门禁、版本规则、决策记录。

### 项目治理层

项目治理层定义 AI 如何进入并维护真实代码项目。

- `00-system/project-governance-model.md`：项目治理模型和重新定位。
- `01-governance/`：治理门禁、变更规则和架构决策。
- `04-workflows/common/project-governance-workflow.md`：通用项目治理主流程。
- `05-standards/project-governance-standard.md`：真实项目治理标准。
- `06-templates/common/project-governance-checklist-template.md`：项目治理检查模板。

这一层优先关注项目架构、模块边界、设计规范、任务列表、模块文档和验证证据。

### 专业能力层

专业能力层承载按需调用的角色判断和专项工作流。

- `02-roles/`：定义 AI 协作角色及其边界。角色是可选专家能力，不是固定总流程。
- `03-inputs/`：存放原始资料。
- `04-workflows/`：定义 AI 如何处理资料、生成模板、生成提示词、评审输出。
- `06-templates/`：存放可复用提示词模板。
- `07-prompts/`：存放正式提示词。
- `08-outputs/`：存放 AI 输出结果。
- `12-projects/`：承载具体任务项目。长期迭代项目通过 `00-progress/memory-summary.md` 管理当前记忆，完整历史按需追溯。

项目真实架构、模块文档、设计规范和任务状态应优先保存在被治理的外部项目中，而不是假设通用角色包能够替代这些事实。

### 资产层

资产层沉淀长期价值。

- `05-standards/`：定义质量标准。
- `09-examples/`：沉淀优秀案例。
- `10-knowledge-base/`：提炼可复用知识。
- `11-evaluations/`：沉淀测试、评分和评估方法。
- `14-exports/`：存放可脱离当前项目独立使用的角色能力包或专项能力包。
- `99-archive/`：保存历史和废弃内容。

## 全局目录与项目目录的关系

全局目录沉淀通用规则和可复用资产。`12-projects/` 存放具体任务的一次性过程材料。

当某个项目产物被证明稳定、可复用时，再提升到全局目录：

```text
12-projects/.../template.md -> 06-templates/
12-projects/.../output.md -> 09-examples/
12-projects/.../lesson.md -> 10-knowledge-base/
```

当某组能力已经稳定，并需要提供给某个角色或外部项目独立使用时，再导出到 `14-exports/`：

```text
04-workflows/{role}/
06-templates/{role}/
11-evaluations/output-scorecards/
10-knowledge-base/
-> 14-exports/{role}-kit/
```

导出的角色能力包必须遵守统一生命周期标准：

```text
05-standards/role-kit-lifecycle-standard.md
```

这意味着每个角色能力包都必须有主入口工作流，并且主入口应承担生命周期编排职责，而不是只做单点任务分流。
