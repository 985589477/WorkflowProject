# 标准目录

这里存放 WorkflowProject 的全局质量标准。

标准用于约束工作流、模板、提示词、输出、评审、角色能力包和导出包，避免每次建设都重新定义规则。

## 当前关键标准

| 文件 | 作用 |
| --- | --- |
| `input-standard.md` | 输入材料标准 |
| `workflow-standard.md` | 工作流结构标准 |
| `template-standard.md` | 模板结构标准 |
| `prompt-standard.md` | 正式提示词标准 |
| `output-standard.md` | 输出结果标准 |
| `review-standard.md` | 评审标准 |
| `example-standard.md` | 案例沉淀标准 |
| `project-standard.md` | 项目结构标准 |
| `iteration-memory-standard.md` | 迭代记忆管理标准 |
| `role-standard.md` | 角色定义标准 |
| `exported-kit-start-here-standard.md` | 导出能力包入口标准 |
| `role-kit-lifecycle-standard.md` | 角色能力包生命周期标准 |
| `agent-orchestration-standard.md` | Skill、父 Agent、子 Agent 的分流和边界标准 |
| `interaction-quality-standard.md` | 产品和 UI 交互质量、操作区域、反馈恢复和视觉层级标准 |

## 新增角色能力包时必须看

```text
role-kit-lifecycle-standard.md
exported-kit-start-here-standard.md
workflow-standard.md
```

其中 `role-kit-lifecycle-standard.md` 负责统一所有角色能力包的共性：

- 主入口工作流。
- 生命周期推进。
- 执行状态格式。
- 主动询问规则。
- 阶段门禁。
- 任务结束标准。
- 外部使用体验层。

## 新增具体输出时必须看

如果只是做一次具体项目，优先看：

```text
input-standard.md
output-standard.md
review-standard.md
iteration-memory-standard.md
```

如果要把结果沉淀为案例，再看：

```text
example-standard.md
```
