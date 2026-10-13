# 框架输出

## 已创建的全局框架

已建立以下全局框架目录：

```text
00-system/
01-governance/
02-roles/
03-inputs/
04-workflows/
05-standards/
06-templates/
07-prompts/
08-outputs/
09-examples/
10-knowledge-base/
11-evaluations/
12-projects/
13-visual-maps/
15-dashboard/
99-archive/
tools/
```

## 已创建的系统文档

- `README.md`
- `00-system/quick-start.md`
- `00-system/project-vision.md`
- `00-system/architecture.md`
- `00-system/terminology.md`
- `00-system/naming-rules.md`
- `00-system/language-rules.md`
- `00-system/document-lifecycle.md`
- `00-system/operating-guide.md`
- `00-system/progress-reporting-rules.md`

## 已创建的治理文档

- `01-governance/contribution-rules.md`
- `01-governance/change-management.md`
- `01-governance/versioning-rules.md`
- `01-governance/review-process.md`
- `01-governance/quality-gates.md`
- `01-governance/decision-records/0001-project-architecture.md`

## 已创建的标准文档

- `05-standards/input-standard.md`
- `05-standards/role-standard.md`
- `05-standards/workflow-standard.md`
- `05-standards/template-standard.md`
- `05-standards/prompt-standard.md`
- `05-standards/output-standard.md`
- `05-standards/example-standard.md`
- `05-standards/project-standard.md`
- `05-standards/review-standard.md`
- `05-standards/quality-checklists/common-checklist.md`
- `05-standards/quality-checklists/product-manager-checklist.md`
- `05-standards/quality-checklists/developer-checklist.md`
- `05-standards/quality-checklists/ui-designer-checklist.md`

## 已创建的 Meta 模板

- `06-templates/meta/template-generator.md`
- `06-templates/meta/prompt-generator.md`
- `06-templates/meta/output-reviewer.md`
- `06-templates/meta/example-extractor.md`
- `06-templates/meta/template-optimizer.md`

## 已创建的低成本使用入口

- `tools/create_project.py`
- `00-system/quick-start.md`
- `00-system/progress-reporting-rules.md`
- `04-workflows/common/project-execution-workflow.md`
- `04-workflows/common/asset-promotion-workflow.md`
- `06-templates/common/general-task-template.md`
- `10-knowledge-base/how-to-write-knowledge.md`
- `11-evaluations/output-scorecards/project-completion-scorecard.md`

## 已创建的通用工作流

- `04-workflows/common/input-analysis-workflow.md`
- `04-workflows/common/template-generation-workflow.md`
- `04-workflows/common/prompt-generation-workflow.md`
- `04-workflows/common/output-review-workflow.md`
- `04-workflows/common/example-extraction-workflow.md`
- `04-workflows/common/template-iteration-workflow.md`
- `04-workflows/common/asset-promotion-workflow.md`
- `04-workflows/common/project-execution-workflow.md`

## 已创建的思维导图

- `13-visual-maps/WorkflowProject.xmind`
- `13-visual-maps/WorkflowProject-mindmap-outline.md`
- `13-visual-maps/WorkflowProject-operation-flow.xmind`
- `13-visual-maps/WorkflowProject-operation-flow-outline.md`
- `13-visual-maps/WorkflowProject-file-responsibility.xmind`
- `13-visual-maps/WorkflowProject-file-responsibility-outline.md`

## 已创建的第一个项目

本项目本身：

```text
12-projects/mixed/capability-building/workflowproject-framework-bootstrap/
```

## 已验证的能力

- 可通过 `tools/create_project.py` 创建标准项目。
- 新项目会自动生成 `00-progress/progress-log.md`。
- 文件职责图可通过 `tools/generate_file_responsibility_xmind.py` 自动扫描当前目录生成。
- 文档正文已调整为中文优先。
- 项目执行过程已加入“当前进度、调度角色、使用工作流、使用模板、下一步”的汇报要求。
- 可通过 `15-dashboard/` React 控制台查看项目总览、能力地图、流程地图、资产索引、风险和下一步建议。
