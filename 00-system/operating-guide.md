# Operating Guide

## 新任务执行流程

1. 在 `12-projects/` 下创建任务目录。
2. 可复制 `12-projects/project-template/` 作为新任务项目骨架。
3. 将原始资料放到任务目录的 `01-inputs/`，必要时同步到全局 `03-inputs/`。
4. 根据任务角色选择 `02-roles/` 中的角色定义。
5. 根据任务类型选择 `04-workflows/` 中的工作流。
6. 如果没有合适模板，使用 `06-templates/meta/template-generator.md` 生成初版模板。
7. 根据 `05-standards/template-standard.md` 优化模板。
8. 使用模板和输入资料生成正式提示词。
9. 执行提示词，保存 AI 输出。
10. 使用 `11-evaluations/` 中的评分或评估方法进行评审。
11. 将优秀结果沉淀为案例，将规律提炼为知识。

## 新增角色流程

新增角色时至少补齐：

- `02-roles/{role}/role-definition.md`
- `04-workflows/{role}/README.md`
- `06-templates/{role}/README.md`
- `05-standards/quality-checklists/{role}-checklist.md`

## 新增模板流程

新增模板时必须说明：

- 适用角色
- 适用场景
- 输入变量
- 输出格式
- 质量标准
- 至少一个测试或使用记录
