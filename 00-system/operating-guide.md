# 操作指南

## 新任务执行流程

如果任务涉及真实代码项目，优先使用：

```text
04-workflows/common/project-governance-workflow.md
```

先检查项目治理基础，再决定是否调用产品、UI、开发或测试能力。不要因为任务看起来属于某个角色，就跳过项目架构、模块边界、设计规范和任务列表检查。

1. 如果是 WorkflowProject 自身的能力建设，优先使用 `tools/create_project.py` 创建任务目录。
2. 如果是外部真实代码项目，先检查其 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`.cursor/rules/` 和 `docs/`。
3. 也可以手动复制 `12-projects/project-template/` 作为 WorkflowProject 任务项目骨架。
4. 将原始资料放到任务目录的 `01-inputs/`，必要时同步到全局 `03-inputs/`。
5. 根据项目治理检查结果，按需选择 `02-roles/` 中的角色定义。
6. 根据当前阶段选择 `04-workflows/` 中的工作流。
7. 如果没有合适模板，使用 `06-templates/meta/template-generator.md` 生成初版模板。
8. 根据 `05-standards/` 优化输出结构。
9. 执行任务，保存输出、验证结果和项目文档变更。
10. 使用 `11-evaluations/` 中的评分或评估方法进行评审。
11. 将稳定、可复用的结果沉淀为案例、知识或能力包。
12. 如果新增或修改了全局资产、项目、导出包，运行 `python3 tools/refresh_maps.py` 同步刷新项目索引、资产索引、控制台数据和 XMind 导图。

执行过程中遵守：

```text
00-system/progress-reporting-rules.md
00-system/execution-brief-rules.md
00-system/result-report-rules.md
05-standards/iteration-memory-standard.md
```

## 长期迭代项目的记忆管理

如果项目会持续迭代，不要让 AI 每次读取所有历史记录。

继续项目时优先读取：

```text
README.md
00-progress/memory-summary.md
00-progress/next-actions.md
```

只有需要追溯原因、审计过程或处理历史冲突时，再读取：

```text
00-progress/progress-log.md
00-progress/decision-log.md
02-analysis/
05-review/
06-lessons/
```

当 `progress-log.md` 变长、项目完成阶段或准备沉淀时，使用：

```text
04-workflows/common/iteration-memory-management-workflow.md
```

更新 `00-progress/memory-summary.md`。

## 创建项目命令

示例：

```bash
python3 tools/create_project.py mixed my-first-task --type real-cases
python3 tools/create_project.py developer login-bug-fix --type real-cases
python3 tools/create_project.py product-manager member-subscription-prd --type real-cases
```

如果需要中文项目标题：

```bash
python3 tools/create_project.py mixed workflowproject-framework-bootstrap --type capability-building --title "WorkflowProject 框架启动项目"
```

如果需要指定项目根目录：

```bash
python3 tools/create_project.py mixed ai-template-tool --output 12-projects/mixed/real-cases/ai-template-tool
```

## 查找当前可用能力

如果不知道当前项目里有哪些角色包、工作流、模板、评分表、标准或工具脚本可以使用，不要先翻目录，先看：

```text
12-projects/asset-index.md
```

它由脚本自动生成：

```bash
python3 tools/generate_asset_index.py
```

通常直接运行统一刷新命令即可：

```bash
python3 tools/refresh_maps.py
```

`12-projects/project-index.md` 用来找历史项目，`12-projects/asset-index.md` 用来找可复用能力。

## 语言要求

新增文档时遵守 `00-system/language-rules.md`：

- 文档标题、说明、步骤、结论优先使用中文。
- 目录名和文件名可保留英文，保证引用稳定。
- 非必要不新增英文标题。

## 新增角色流程

新增角色时至少补齐：

- `02-roles/{role}/role-definition.md`
- `04-workflows/{role}/README.md`
- `06-templates/{role}/README.md`
- `05-standards/quality-checklists/{role}-checklist.md`

如果该角色需要导出为独立能力包，还必须遵守：

```text
05-standards/role-kit-lifecycle-standard.md
05-standards/exported-kit-start-here-standard.md
```

角色能力包必须包含：

- 主入口工作流，且主入口是生命周期编排器，不是单点分流器。
- 执行状态格式。
- 任务结束标准。
- 主动询问规则。
- 关键阶段门禁。
- `INSTALL.md`。
- `examples/quick-start-example.md`。
- `integrations/codex-usage.md`。
- `integrations/cursor-usage.md`。
- `SKILL.md` 草稿。

## 新增模板流程

新增模板时必须说明：

- 适用角色
- 适用场景
- 输入变量
- 输出格式
- 质量标准
- 至少一个测试或使用记录
