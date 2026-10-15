# 进度记录

## 2026-10-13

- 创建 `developer-kit-export-workflow` 能力建设项目。
- 创建 `14-exports/developer-kit/`。
- 导出开发工作流到 `workflows/developer/`。
- 导出开发模板到 `templates/developer/`。
- 导出开发评分表到 `scorecards/`。
- 导出开发治理能力总纲到 `knowledge/`。
- 编写 `START-HERE.md`、`README.md`、`usage-guide.md`、`manifest.md` 和 `SKILL.md`。
- 更新 `14-exports/README.md` 和 `04-workflows/developer/README.md`。

## 2026-10-13 补充

- 补充 `04-workflows/developer/developer-kit-workflow.md` 作为开发治理总入口工作流。
- 同步更新导出包中的入口引用，避免只有 `START-HERE.md` 而缺少角色调度工作流。

## 2026-10-13 再次补充

- 将 `developer-kit-workflow.md` 从任务分流器升级为开发治理主流程。
- 增加标准开发生命周期：需求理解、开发确认、项目理解、功能规划、实现、验证、文档、评审、发布或复盘。
- 增加开发前门禁：实现前必须完成整体功能规划。
- 增加主动询问规则：不明确或高风险时先询问用户。
- 同步更新 `14-exports/developer-kit/` 的入口、说明和 skill 草稿。

## 2026-10-13 使用体验补齐

- 新增 `14-exports/developer-kit/INSTALL.md`。
- 新增 `14-exports/developer-kit/examples/quick-start-example.md`。
- 新增 `14-exports/developer-kit/integrations/codex-usage.md`。
- 新增 `14-exports/developer-kit/integrations/cursor-usage.md`。
- 在 `START-HERE.md`、`usage-guide.md` 和 `developer-kit-workflow.md` 中补充执行状态格式和任务结束标准。

## 2026-10-13 实现阶段增强

- 在 developer 总入口中增加“实现前必须拆成开发任务列表”的规则。
- 在 `implementation-workflow.md` 中增加“逐条执行、逐条验证”的执行步骤。
- 在 `implementation-template.md` 中增加开发任务列表、当前执行任务和逐条执行记录。
- 在 `implementation-scorecard.md` 中增加任务拆解和逐条执行评分维度。
- 同步更新 `14-exports/developer-kit/`。

## 2026-10-13 开发前规范检查增强

- 在 developer 总入口中增加“实现前必须检查项目规范”的门禁。
- 在 `project-understanding-workflow.md` 中增加规范资产扫描。
- 在 `implementation-workflow.md` 中增加项目规范检查步骤。
- 在 `implementation-template.md` 中增加项目规范检查输出区。
- 在 `implementation-scorecard.md` 中增加规范检查评分维度。
- 同步更新 `14-exports/developer-kit/`。

## 2026-10-13 真实开发协同能力补齐

- 新增 `issue-diagnosis-workflow.md`、模板和评分表。
- 新增 `data-api-contract-workflow.md`、模板和评分表。
- 新增 `security-permission-workflow.md`、模板和评分表。
- 新增 `workflow-orchestration-guide.md`、模板和评分表。
- 更新 developer 总入口、能力总纲、目录说明和导出包。

## 2026-10-13 迭代记忆管理补齐

- 新增 `05-standards/iteration-memory-standard.md`。
- 新增 `04-workflows/common/iteration-memory-management-workflow.md`。
- 新增 `06-templates/common/iteration-memory-summary-template.md`。
- 在项目模板和创建脚本中增加 `00-progress/memory-summary.md`。
- 为当前 developer-kit 导出建设项目补充 `00-progress/memory-summary.md`，后续继续项目时优先读取摘要而不是完整历史。

## 2026-10-14 迭代记忆管理落地到已有项目和导出包

- 为现有 `12-projects/` 下项目批量补充 `00-progress/memory-summary.md`。
- 将项目 README 的继续读取顺序调整为优先读取 `README.md`、`00-progress/memory-summary.md`、`00-progress/next-actions.md`。
- 更新能力导出标准和能力导出工作流，要求长期使用的导出包携带或说明迭代记忆管理。
- 将 `iteration-memory-management-workflow.md` 和 `iteration-memory-summary-template.md` 同步到 `product-manager-kit` 和 `developer-kit`。
- 更新两个导出包的 `START-HERE.md`、`usage-guide.md`、`SKILL.md` 和 `manifest.md`，说明外部项目使用 `docs/ai-memory-summary.md` 或已有记忆文件。

## 2026-10-13

- 当前阶段：项目已创建
- 调度角色：项目创建脚本
- 使用工作流：04-workflows/common/project-execution-workflow.md
- 使用模板：12-projects/project-template/
- 输入位置：未放入
- 输出位置：12-projects/developer/capability-building/developer-kit-export-workflow
- 当前结果：已创建项目《developer-kit 总入口整合与导出项目》
- 下一步：把原始材料放入 01-inputs/
