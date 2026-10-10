# Architecture

## 总体链路

```text
03-inputs
-> 04-workflows
-> 06-templates
-> 07-prompts
-> 08-outputs
-> 11-evaluations
-> 09-examples
-> 10-knowledge-base
```

## 分层说明

### 系统层

系统层定义项目如何存在。

- `00-system/`：项目愿景、架构、术语、命名、生命周期、操作指南。
- `01-governance/`：变更管理、评审流程、质量门禁、版本规则、决策记录。

### 生产层

生产层承载从资料到输出的真实过程。

- `02-roles/`：定义 AI 协作角色及其边界。
- `03-inputs/`：存放原始资料。
- `04-workflows/`：定义 AI 如何处理资料、生成模板、生成提示词、评审输出。
- `06-templates/`：存放可复用提示词模板。
- `07-prompts/`：存放正式提示词。
- `08-outputs/`：存放 AI 输出结果。
- `12-projects/`：承载具体任务项目。

### 资产层

资产层沉淀长期价值。

- `05-standards/`：定义质量标准。
- `09-examples/`：沉淀优秀案例。
- `10-knowledge-base/`：提炼可复用知识。
- `11-evaluations/`：沉淀测试、评分和评估方法。
- `99-archive/`：保存历史和废弃内容。

## 全局目录与项目目录的关系

全局目录沉淀通用规则和可复用资产。`12-projects/` 存放具体任务的一次性过程材料。

当某个项目产物被证明稳定、可复用时，再提升到全局目录：

```text
12-projects/.../template.md -> 06-templates/
12-projects/.../output.md -> 09-examples/
12-projects/.../lesson.md -> 10-knowledge-base/
```
