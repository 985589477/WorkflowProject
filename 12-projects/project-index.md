# 项目索引

本文件由 `tools/generate_project_index.py` 自动生成，用来解决项目变多后不知道每个项目是干什么、从哪里继续的问题。

刷新方式：

```bash
python3 tools/generate_project_index.py
```

如果要同时刷新可视化控制台和 XMind，运行：

```bash
python3 tools/refresh_maps.py
```

## 当前工作区

当前工作区由 `12-projects/current-focus.md` 维护，只保留当前主线和入口，不代表全部项目。

这不是全部项目清单，只回答：现在应该先看什么、继续什么、暂时不要碰什么。

## 当前主线

### 1. 项目治理框架

当前主线已经从“继续细化角色”调整为“治理真实代码项目”。先看：

```text
00-system/project-governance-model.md
04-workflows/common/project-governance-workflow.md
14-exports/project-governance-kit/START-HERE.md
```

安装到真实代码项目：

```bash
python3 tools/install_project_kits.py /你的代码项目路径 --dry-run
python3 tools/install_project_kits.py /你的代码项目路径
```

### 2. 真实项目验证

下一步应找一个真实代码项目，验证 `project-governance-kit` 是否能在写代码前完成：

```text
项目规则检查
架构和模块检查
设计规范检查
任务列表生成
逐条执行和验证
文档同步
```

### 3. 角色能力维护

产品、UI、开发、测试角色已经作为可选专业能力保留。后续只有在真实验证中出现专业缺口或 badcase 时，才回到对应角色项目优化，不再继续无目标地扩展角色细分。

## 暂时不要做

- 不要重新打开所有已经完成的角色能力建设项目。
- 不要为了项目数量继续新建角色工作流。
- 不要把每一次真实需求都创建成能力建设项目。
- 不要删除历史项目；需要清理时先归档并保留索引。

## 三个入口

| 你想知道什么 | 先看哪里 |
| --- | --- |
| 当前应该做什么 | `12-projects/current-focus.md` |
| 有哪些可复用能力 | `12-projects/asset-index.md` |
| 所有历史和建设项目 | `12-projects/project-index.md` |

## 当前项目选择规则

- 建设或修改通用能力：使用 `capability-building`。
- 验证一个真实需求或真实项目：使用 `real-cases`。
- 验证不稳定想法：使用 `experiments`。
- 只是日常使用已完成能力：直接使用导出包或全局工作流，不新建能力建设项目。

## 分组总览

### 跨角色项目

- 角色目录：`12-projects/mixed/`
- 项目数量：4

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：4

##### 能力导出工作流建设项目

- 状态：completed
- 路径：`12-projects/mixed/capability-building/capability-export-workflow`
- 项目职责：这个项目负责定义“如何导出能力包”，不是直接导出某一个具体能力包。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 WorkflowProject 的能力导出工作流。
- 当前状态：已完成第一版，并已完成第一次真实导出验证准备。
- 推荐下一步：已完成： 14-exports/product-manager-kit/ 推荐下一步： 请在新对话或其他项目中输入一个真实产品需求，验证 product-manager-kit skill 是否会正确触发，并观察它是否能正确选择 workflow、template 和 scorecard。 更快的验证入口：
- 启动方式：

```text
请使用 12-projects/mixed/capability-building/capability-export-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/capability-export-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 跨角色团队总调度导出包建设项目

- 状态：completed
- 路径：`12-projects/mixed/capability-building/team-orchestration-kit-export-workflow`
- 项目职责：把跨角色团队总调度能力导出为可复制到外部项目使用的独立能力包。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：把跨角色团队总调度能力导出为可复制到外部项目使用的独立能力包。
- 当前状态：已完成 `14-exports/team-orchestration-kit/` 导出包建设，并更新导出区 README。
- 推荐下一步：推荐把 `team-orchestration-kit` 与四个角色包一起复制到外部项目验证。
- 启动方式：

```text
请使用 12-projects/mixed/capability-building/team-orchestration-kit-export-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/team-orchestration-kit-export-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 跨角色团队总调度工作流建设项目

- 状态：completed
- 路径：`12-projects/mixed/capability-building/team-orchestration-workflow`
- 项目职责：这个项目负责沉淀团队级编排规则：当用户提出需求时，判断哪些角色需要参与、谁先接管、如何交接、如何互相验收，以及出现沟通不畅时如何反馈 badcase 并回到对应角色能力项目优化。
- 何时使用：当一个任务不只是单个角色能完成，而是需要产品、UI、开发、测试连续协作时，使用这个项目。 当你要在外部项目中直接使用团队总调度时，优先使用： 04-workflows/mixed/team-orchestration-workflow.md
- 关键产物：`04-workflows/mixed/team-orchestration-workflow.md` `06-templates/mixed/team-orchestration-template.md` `11-evaluations/output-scorecards/team-orchestration-scorecard.md`
- 目标：建设一个跨角色团队总调度能力，用于协调产品经理、UI 设计师、开发工程师、测试工程师按完整团队链路协作。
- 当前状态：已完成团队总调度能力建设，并提升到全局 mixed 工作流、模板和评分表。
- 推荐下一步：使用一个真实完整需求验证 `04-workflows/mixed/team-orchestration-workflow.md`，重点观察： 是否能正确判断当前接管角色。 是否能按产品 -> UI -> 开发 -> 测试推进。 是否能发现上游产物让下游看不懂的问题。 是否能判断开发交付是否通过产品、UI、测试验收。
- 启动方式：

```text
请使用 12-projects/mixed/capability-building/team-orchestration-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/team-orchestration-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### WorkflowProject 框架刷新项目

- 状态：completed
- 路径：`12-projects/mixed/capability-building/workflowproject-framework-refresh`
- 项目职责：这个项目是当前 WorkflowProject 的最新框架同步记录。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：刷新 WorkflowProject 当前框架说明，让项目从最初的 bootstrap 状态同步到当前真实结构。
- 当前状态：已完成第一版。
- 推荐下一步：已完成： 12-projects/mixed/capability-building/workflowproject-framework-bootstrap/ -> 99-archive/projects/workflowproject-framework-bootstrap/ 推荐下一步： 使用能力导出工作流，将产品经理能力导出到 14-exports/product-manager-kit/
- 启动方式：

```text
请使用 12-projects/mixed/capability-building/workflowproject-framework-refresh 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/workflowproject-framework-refresh 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

### 产品经理项目

- 角色目录：`12-projects/product-manager/`
- 项目数量：18

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：16

##### 验收标准工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/acceptance-criteria-workflow`
- 项目职责：这个项目负责生成并验证产品经理验收标准工作流。
- 何时使用：当你要建设、优化或评审验收标准生成能力时，使用这个项目。 当你要执行一次具体验收标准输出任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/acceptance-criteria-workflow.md
- 关键产物：项目输出：`04-outputs/acceptance-criteria-workflow.md` 全局沉淀：`04-workflows/product-manager/acceptance-criteria-workflow.md` 全局模板：`06-templates/product-manager/acceptance-criteria-template.md` 全局评分表：`11-evaluations/output-scorecards/acceptance-criteria-scorecard.md`
- 目标：建设产品经理能力体系中的验收标准生成工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理功能规划工作流。 建议项目路径： 12-projects/product-manager/capability-building/feature-planning-workflow/
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/acceptance-criteria-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/acceptance-criteria-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 竞品分析工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/competitor-analysis-workflow`
- 项目职责：这个项目负责生成并验证产品经理竞品分析工作流。
- 何时使用：当你要建设、优化或评审竞品分析能力时，使用这个项目。 当你要执行一次具体竞品分析任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/competitor-analysis-workflow.md
- 关键产物：项目输出：`04-outputs/competitor-analysis-workflow.md` 全局沉淀：`04-workflows/product-manager/competitor-analysis-workflow.md` 全局模板：`06-templates/product-manager/competitor-analysis-template.md` 全局评分表：`11-evaluations/output-scorecards/competitor-analysis-scorecard.md`
- 目标：建设产品经理能力体系中的竞品分析工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理优先级判断工作流。 建议项目路径： 12-projects/product-manager/capability-building/priority-decision-workflow/
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/competitor-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/competitor-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 功能规划工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/feature-planning-workflow`
- 项目职责：这个项目负责生成并验证产品经理功能规划工作流。
- 何时使用：当你要建设、优化或评审功能规划能力时，使用这个项目。 当你要执行一次具体功能规划任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/feature-planning-workflow.md
- 关键产物：项目输出：`04-outputs/feature-planning-workflow.md` 全局沉淀：`04-workflows/product-manager/feature-planning-workflow.md` 全局模板：`06-templates/product-manager/feature-planning-template.md` 全局评分表：`11-evaluations/output-scorecards/feature-planning-scorecard.md`
- 目标：建设产品经理能力体系中的功能规划工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理用户故事生成工作流。 也可以进入判断决策类能力： 优先级判断工作流 版本规划工作流
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/feature-planning-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/feature-planning-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### PRD 工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/prd-workflow`
- 项目职责：这个项目负责生成并验证产品经理 PRD 工作流。
- 何时使用：当你要建设、优化或评审产品经理 PRD 生成能力时，使用这个项目。 当你要执行一次具体 PRD 输出任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/prd-generation-workflow.md
- 关键产物：项目输出：`04-outputs/prd-generation-workflow.md` 全局沉淀：`04-workflows/product-manager/prd-generation-workflow.md` 测试输入：`12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/` 作用定位：产品经理 PRD 生成细分工作流
- 目标：建设产品经理能力体系中的 PRD 生成工作流。
- 当前状态：已完成第一版。
- 推荐下一步：PRD 工作流、模板和评分表已完成第一版沉淀。 推荐下一步： 使用 12-projects/product-manager/real-cases/ai-template-tool-prd/ 作为输入， 继续建设 UI 设计输入工作流，或先建设验收标准工作流。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/prd-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/prd-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 优先级判断工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/priority-decision-workflow`
- 项目职责：这个项目负责生成并验证产品经理优先级判断工作流。
- 何时使用：当你要建设、优化或评审优先级判断能力时，使用这个项目。 当你要执行一次具体优先级判断任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/priority-decision-workflow.md
- 关键产物：项目输出：`04-outputs/priority-decision-workflow.md` 全局沉淀：`04-workflows/product-manager/priority-decision-workflow.md` 全局模板：`06-templates/product-manager/priority-decision-template.md` 全局评分表：`11-evaluations/output-scorecards/priority-decision-scorecard.md`
- 目标：建设产品经理能力体系中的优先级判断工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理版本规划工作流。 建议项目路径： 12-projects/product-manager/capability-building/version-planning-workflow/
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/priority-decision-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/priority-decision-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 产品经理能力体系规划项目

- 状态：draft
- 路径：`12-projects/product-manager/capability-building/product-manager-capability-system`
- 项目职责：这个项目负责规划“产品经理能力体系地图”。
- 何时使用：当你不是要完成一个具体产品输出，而是要决定产品经理体系接下来怎么建设时，使用这个项目。 典型场景： 我想知道产品经理后续应该补哪些能力。 我想决定先做需求分析、PRD、验收标准还是竞品分析。
- 关键产物：项目输出：`04-outputs/product-manager-capability-system.md` 全局沉淀：`10-knowledge-base/patterns/product-manager-capability-system.md` 作用定位：产品经理能力地图 / 后续建设路线图
- 目标：规划产品经理后续能力细分体系，形成可以指导后续 workflow、template、example 和 evaluation 建设的总地图。
- 当前状态：已完成。
- 推荐下一步：优先启动需求分析工作流项目： python3 tools/create_project.py product-manager requirement-analysis-workflow --type capability-building 原因： 需求分析是 PRD、功能规划和验收标准的上游能力。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/product-manager-capability-system 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-manager-capability-system 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 产品经理任务总入口项目

- 状态：draft
- 路径：`12-projects/product-manager/capability-building/product-manager-workflow`
- 项目职责：这个项目负责生成并验证“产品经理任务总入口工作流”。
- 何时使用：当你有一个具体产品任务，但还不确定应该走需求分析、PRD、功能规划还是验收标准时，先使用这个项目沉淀出的全局工作流。 典型场景： 我有一个产品想法，不知道怎么整理。 我想生成 PRD，但还没有标准输入。
- 关键产物：项目输出：`04-outputs/product-manager-workflow-v2-output.md` 全局沉淀：`04-workflows/product-manager/product-manager-workflow.md` 作用定位：产品经理任务总入口 / 能力调度入口
- 目标：通过 `idea-to-input-generator` 从用户一句模糊描述开始，重新生成产品经理通用工作流，并验证“模糊想法 -> 标准 input -> 后续输出”的完整链路。
- 当前状态：已完成。
- 推荐下一步：启动一个真实 PRD 项目，使用新版产品经理工作流验证： python3 tools/create_project.py product-manager sample-prd --type real-cases 然后只给一句产品想法，让 `idea-to-input-generator` 先生成 input。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/product-manager-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-manager-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 产品路线图工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/product-roadmap-workflow`
- 项目职责：这个项目负责生成并验证产品经理产品路线图工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设产品经理能力体系中的产品路线图工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理需求变更评估工作流。 原因：路线图和版本规划完成后，真实执行中经常出现新增需求、范围变化和优先级调整，需要稳定评估变更影响。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/product-roadmap-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-roadmap-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 产品策略判断工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/product-strategy-workflow`
- 项目职责：这个项目负责生成并验证产品经理产品策略判断工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设产品经理能力体系中的产品策略判断工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理需求池管理工作流。 原因：产品策略判断会筛选出值得进入产品系统的方向，需求池管理负责长期保存、分类、更新和流转这些需求。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/product-strategy-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-strategy-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 需求分析工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/requirement-analysis-workflow`
- 项目职责：这个项目负责生成并验证产品经理需求分析工作流。
- 何时使用：当你要建设或优化产品经理的需求分析能力时，使用这个项目。 当你要执行一次具体需求分析任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/requirement-analysis-workflow.md
- 关键产物：项目输出：`04-outputs/requirement-analysis-workflow.md` 全局沉淀：`04-workflows/product-manager/requirement-analysis-workflow.md` 作用定位：产品经理需求分析细分工作流
- 目标：建设产品经理能力体系中的第一个细分能力：需求分析工作流。
- 当前状态：已完成第一版，并已通过真实案例验证。
- 推荐下一步：下一步建议不要继续扩写本能力建设项目，而是使用它处理更多真实需求。 已有验证项目： 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis/ 目标： 观察真实使用过程中哪些地方仍然不够顺手，再反向迭代需求分析模板和评分表。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/requirement-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 需求变更评估工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/requirement-change-evaluation-workflow`
- 项目职责：这个项目负责生成并验证产品经理需求变更评估工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设产品经理能力体系中的需求变更评估工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理版本复盘工作流。 原因：需求变更会影响版本执行，版本完成后需要复盘目标达成、变更影响、问题原因和后续改进。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/requirement-change-evaluation-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-change-evaluation-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 需求池管理工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/requirement-pool-workflow`
- 项目职责：这个项目负责生成并验证产品经理需求池管理工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设产品经理能力体系中的需求池管理工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理产品路线图工作流。 原因：需求池管理解决“有哪些需求和状态”，产品路线图负责把策略、版本和需求放到更长周期的方向规划中。
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/requirement-pool-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-pool-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 用户反馈整理工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/user-feedback-workflow`
- 项目职责：这个项目负责生成并验证产品经理用户反馈整理工作流。
- 何时使用：当你要建设、优化或评审用户反馈整理能力时，使用这个项目。 当你要执行一次具体用户反馈分析任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/user-feedback-workflow.md
- 关键产物：项目输出：`04-outputs/user-feedback-workflow.md` 全局沉淀：`04-workflows/product-manager/user-feedback-workflow.md` 全局模板：`06-templates/product-manager/user-feedback-template.md` 全局评分表：`11-evaluations/output-scorecards/user-feedback-scorecard.md`
- 目标：建设产品经理能力体系中的用户反馈整理工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理竞品分析工作流。 建议项目路径： 12-projects/product-manager/capability-building/competitor-analysis-workflow/
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/user-feedback-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/user-feedback-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 用户故事生成工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/user-story-workflow`
- 项目职责：这个项目负责生成并验证产品经理用户故事生成工作流。
- 何时使用：当你要建设、优化或评审用户故事生成能力时，使用这个项目。 当你要执行一次具体用户故事输出任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/user-story-workflow.md
- 关键产物：项目输出：`04-outputs/user-story-workflow.md` 全局沉淀：`04-workflows/product-manager/user-story-workflow.md` 全局模板：`06-templates/product-manager/user-story-template.md` 全局评分表：`11-evaluations/output-scorecards/user-story-scorecard.md`
- 目标：建设产品经理能力体系中的用户故事生成工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理用户反馈整理工作流。 也可以进入判断决策类能力： 优先级判断工作流 版本规划工作流
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/user-story-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/user-story-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 版本规划工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/version-planning-workflow`
- 项目职责：这个项目负责生成并验证产品经理版本规划工作流。
- 何时使用：当你要建设、优化或评审版本规划能力时，使用这个项目。 当你要执行一次具体版本规划任务时，使用本项目沉淀出的全局工作流： 04-workflows/product-manager/version-planning-workflow.md
- 关键产物：项目输出：`04-outputs/version-planning-workflow.md` 全局沉淀：`04-workflows/product-manager/version-planning-workflow.md` 全局模板：`06-templates/product-manager/version-planning-template.md` 全局评分表：`11-evaluations/output-scorecards/version-planning-scorecard.md`
- 目标：建设产品经理能力体系中的版本规划工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 继续建设产品经理产品策略判断工作流。 也可以进入长期管理能力： 需求池管理工作流
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/version-planning-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/version-planning-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 版本复盘工作流建设项目

- 状态：completed
- 路径：`12-projects/product-manager/capability-building/version-retrospective-workflow`
- 项目职责：这个项目负责生成并验证产品经理版本复盘工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设产品经理能力体系中的版本复盘工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 使用真实案例验证产品经理主链路，或继续扩展数据现象分析、会议纪要转需求、上线检查工作流。 如果继续能力建设，建议优先： 数据现象分析工作流
- 启动方式：

```text
请使用 12-projects/product-manager/capability-building/version-retrospective-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/version-retrospective-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

#### 真实使用项目

- 项目类型：`real-cases`
- 项目数量：2

##### AI 提示词模板工具 PRD 项目

- 状态：completed
- 路径：`12-projects/product-manager/real-cases/ai-template-tool-prd`
- 项目职责：这个项目负责验证 `04-workflows/product-manager/prd-generation-workflow.md` 是否能从需求分析结果生成可用 PRD。
- 何时使用：当你想参考“如何从需求分析生成 PRD”时，使用这个项目。 当你想继续推进 AI 协作资产导航层的 UI 设计、开发拆解或验收标准时，也可以从这个项目继续。
- 关键产物：输入材料：`01-inputs/original-requirement.md` PRD 就绪判断：`02-analysis/prd-readiness.md` PRD 范围：`02-analysis/prd-scope.md` 用户场景：`02-analysis/prd-user-scenarios.md`
- 目标：使用 PRD 生成工作流，把已有需求分析结果转化为 AI 协作资产导航层的 PRD 初稿。
- 当前状态：已完成第一轮 PRD 生成与评审。
- 推荐下一步：推荐下一步： 使用本项目作为输入，建设 UI 设计输入工作流或创建 UI 设计真实项目。 可创建 UI 设计项目： python3 tools/create_project.py ui-designer ai-asset-navigation-ui --type real-cases --title "AI 协作资产导航层 UI 设计项目"
- 启动方式：

```text
请使用 12-projects/product-manager/real-cases/ai-template-tool-prd 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请参考 12-projects/product-manager/real-cases/ai-template-tool-prd 的项目结构处理一个真实使用任务。

我的想法是：
{写你的真实需求或产品想法}

请输出到 12-projects/product-manager/real-cases/{项目名}/，
并把核心结果保存到对应的 02-analysis、04-outputs 或 05-review 目录。
```

##### AI 提示词模板工具需求分析项目

- 状态：completed
- 路径：`12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis`
- 项目职责：这个项目负责验证“需求分析工作流”是否能把一句话产品想法变成可进入 PRD 的需求分析。
- 何时使用：当你想参考“如何用需求分析工作流处理一个模糊产品想法”时，使用这个项目。 当你想继续把 AI 提示词模板工具推进到 PRD、功能规划或界面设计时，也可以从这个项目继续。
- 关键产物：标准输入：`01-inputs/original-requirement.md` 需求分析：`02-analysis/requirement-analysis.md` 扣分点解决方案：`02-analysis/review-gap-resolution.md` 输出评审：`05-review/output-review.md`
- 目标：使用产品经理需求分析工作流，把一个模糊产品想法整理成结构化需求分析结果。
- 当前状态：已完成第一轮需求分析与评审。
- 推荐下一步：推荐创建 PRD 项目，并把 `02-analysis/review-gap-resolution.md` 作为 PRD 输入材料之一： python3 tools/create_project.py product-manager ai-template-tool-prd --type real-cases --title "AI 提示词模板工具 PRD 项目" 启动话术： 请参考 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 的需求分析结果， 尤其是 02-analysis/requirement-analysis.md 和 02-analysis/review-gap-resolution.md， 继续生成 AI 提示词模板工具的 PRD 初稿。
- 启动方式：

```text
请使用 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请参考 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 的项目结构处理一个真实使用任务。

我的想法是：
{写你的真实需求或产品想法}

请输出到 12-projects/product-manager/real-cases/{项目名}/，
并把核心结果保存到对应的 02-analysis、04-outputs 或 05-review 目录。
```

### 开发工程师项目

- 角色目录：`12-projects/developer/`
- 项目数量：18

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：18

##### AI 协作复盘工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/ai-collaboration-retrospective-workflow`
- 项目职责：建设 developer-kit 的“AI 协作复盘工作流”，用于把 AI 协作中的误判、越界、漏测、文档遗漏和发布问题沉淀为后续规则。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“AI 协作复盘工作流”，用于把 AI 协作中的误判、越界、漏测、文档遗漏和发布问题沉淀为后续规则。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/ai-collaboration-retrospective-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/ai-collaboration-retrospective-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 架构决策记录工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/architecture-decision-record-workflow`
- 项目职责：建设 developer-kit 的“架构决策记录工作流”，用于记录关键架构选择的背景、备选方案、取舍原因、影响范围、风险代价和复盘条件。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“架构决策记录工作流”，用于记录关键架构选择的背景、备选方案、取舍原因、影响范围、风险代价和复盘条件。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/architecture-decision-record-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/architecture-decision-record-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 变更风险评估工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/change-risk-assessment-workflow`
- 项目职责：建设 developer-kit 的“变更风险评估工作流”，用于在代码修改前判断风险等级、AI 执行策略、人工确认点、验证要求和回滚要求。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“变更风险评估工作流”，用于在代码修改前判断风险等级、AI 执行策略、人工确认点、验证要求和回滚要求。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/change-risk-assessment-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/change-risk-assessment-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 代码评审工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/code-review-workflow`
- 项目职责：建设 developer-kit 的“代码评审工作流”，用于在交付前检查代码、测试、文档、风险和可维护性，判断是否建议交付。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“代码评审工作流”，用于在交付前检查代码、测试、文档、风险和可维护性，判断是否建议交付。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/code-review-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/code-review-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 依赖与技术债治理工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/dependency-and-tech-debt-workflow`
- 项目职责：建设 developer-kit 的“依赖与技术债治理工作流”，用于管理新增依赖、依赖调整、临时方案、技术债记录和偿还计划。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“依赖与技术债治理工作流”，用于管理新增依赖、依赖调整、临时方案、技术债记录和偿还计划。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/dependency-and-tech-debt-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/dependency-and-tech-debt-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 开发治理能力体系建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/developer-governance-capability-system`
- 项目职责：建设 developer-kit 的开发治理能力体系。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的开发治理能力体系。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 建设 project-bootstrap-workflow，用于新项目启动时检查并补齐 AI 协作开发规范。 建议项目路径： 12-projects/developer/capability-building/project-bootstrap-workflow/
- 启动方式：

```text
请使用 12-projects/developer/capability-building/developer-governance-capability-system 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/developer-governance-capability-system 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### developer-kit 总入口整合与导出项目

- 状态：done
- 路径：`12-projects/developer/capability-building/developer-kit-export-workflow`
- 项目职责：把已经完成的开发治理能力整合并导出为可在外部项目独立使用的 `developer-kit`。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：把已经完成的开发治理能力整合并导出为可在外部项目独立使用的 `developer-kit`。
- 当前状态：已完成第一版导出，输出位置：
- 推荐下一步：在一个真实代码项目中复制 `14-exports/developer-kit/`，验证以下链路： 1. 项目理解。 2. 需求到架构影响分析。 3. 模块边界判断。 4. 小范围实现。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/developer-kit-export-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/developer-kit-export-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 文档同步工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/documentation-sync-workflow`
- 项目职责：建设 developer-kit 的“文档同步工作流”，用于在代码实现和验证后，判断并同步 README、AGENTS、docs、API、架构、模块和配置文档。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“文档同步工作流”，用于在代码实现和验证后，判断并同步 README、AGENTS、docs、API、架构、模块和配置文档。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/documentation-sync-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/documentation-sync-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 环境与配置治理工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/environment-config-governance-workflow`
- 项目职责：建设 developer-kit 的“环境与配置治理工作流”，用于管理环境变量、启动配置、构建配置、部署配置、环境差异、验证和回滚。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“环境与配置治理工作流”，用于管理环境变量、启动配置、构建配置、部署配置、环境差异、验证和回滚。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/environment-config-governance-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/environment-config-governance-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 影响范围分析工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/impact-analysis-workflow`
- 项目职责：建设 developer-kit 的“影响范围分析工作流”，用于在进入实现前拆解确定影响文件、可能影响文件、调用链、接口、数据状态、测试和文档影响。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“影响范围分析工作流”，用于在进入实现前拆解确定影响文件、可能影响文件、调用链、接口、数据状态、测试和文档影响。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/impact-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/impact-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 代码实现执行工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/implementation-workflow`
- 项目职责：建设 developer-kit 的“代码实现执行工作流”，用于在影响范围和风险等级明确后，指导 AI 受控修改代码、补充测试文档并输出交付说明。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“代码实现执行工作流”，用于在影响范围和风险等级明确后，指导 AI 受控修改代码、补充测试文档并输出交付说明。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/implementation-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/implementation-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 最小必要变更治理工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/minimal-change-governance-workflow`
- 项目职责：把 Ponytail 项目中的“少写代码、优先复用、最小完整变更、反过度设计”思想融合进 WorkflowProject 的开发角色能力中，形成可复用的开发治理能力。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：把 Ponytail 项目中的“少写代码、优先复用、最小完整变更、反过度设计”思想融合进 WorkflowProject 的开发角色能力中，形成可复用的开发治理能力。
- 当前状态：已完成全局资产建设，并同步到 `14-exports/developer-kit/`。
- 推荐下一步：推荐暂停本能力建设项目，转入真实开发任务验证。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/minimal-change-governance-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/minimal-change-governance-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 模块边界分析工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/module-boundary-analysis-workflow`
- 项目职责：建设 developer-kit 的“模块边界分析工作流”，用于判断能力归属、模块职责、新增模块、依赖方向、数据状态归属和模块协作方式。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“模块边界分析工作流”，用于判断能力归属、模块职责、新增模块、依赖方向、数据状态归属和模块协作方式。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/module-boundary-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/module-boundary-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 新项目启动治理工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/project-bootstrap-workflow`
- 项目职责：建设 developer-kit 的第一条细分工作流：新项目启动治理工作流。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的第一条细分工作流：新项目启动治理工作流。
- 当前状态：已完成第一版。
- 推荐下一步：推荐下一步： 建设 project-understanding-workflow，用于已有项目接手时帮助 AI 读取上下文、理解结构和发现风险。 建议项目路径： 12-projects/developer/capability-building/project-understanding-workflow/
- 启动方式：

```text
请使用 12-projects/developer/capability-building/project-bootstrap-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/project-bootstrap-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 已有项目理解工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/project-understanding-workflow`
- 项目职责：建设 developer-kit 的“已有项目理解工作流”，让 AI 在接手已有代码项目时，先输出项目理解报告，再进入后续开发。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“已有项目理解工作流”，让 AI 在接手已有代码项目时，先输出项目理解报告，再进入后续开发。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/project-understanding-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/project-understanding-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 发布与回滚治理工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/release-and-rollback-workflow`
- 项目职责：建设 developer-kit 的“发布与回滚治理工作流”，用于管理发布前检查、发布步骤、回滚方案、上线后观察和发布复盘入口。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“发布与回滚治理工作流”，用于管理发布前检查、发布步骤、回滚方案、上线后观察和发布复盘入口。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/release-and-rollback-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/release-and-rollback-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 需求到架构影响分析工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/requirement-to-architecture-workflow`
- 项目职责：建设 developer-kit 的“需求到架构影响分析工作流”，把产品需求转换为开发前的影响范围、模块变更、数据/API/状态影响和风险等级。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“需求到架构影响分析工作流”，把产品需求转换为开发前的影响范围、模块变更、数据/API/状态影响和风险等级。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/requirement-to-architecture-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/requirement-to-architecture-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

##### 测试与验收工作流建设项目

- 状态：completed
- 路径：`12-projects/developer/capability-building/testing-verification-workflow`
- 项目职责：建设 developer-kit 的“测试与验收工作流”，用于在代码实现后制定验证计划、运行验证、输出手动验收步骤、记录未验证内容并判断是否建议交付。
- 何时使用：需要理解或继续这个项目时使用。
- 关键产物：查看项目 README、04-outputs、05-review 和 06-lessons。
- 目标：建设 developer-kit 的“测试与验收工作流”，用于在代码实现后制定验证计划、运行验证、输出手动验收步骤、记录未验证内容并判断是否建议交付。
- 当前状态：已完成第一版能力建设，并提升到全局可复用目录。
- 推荐下一步：待填写。
- 启动方式：

```text
请使用 12-projects/developer/capability-building/testing-verification-workflow 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/developer/capability-building/testing-verification-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

### UI 设计项目

- 角色目录：`12-projects/ui-designer/`
- 项目数量：1

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：1

##### UI 设计能力包启动项目

- 状态：completed
- 路径：`12-projects/ui-designer/capability-building/ui-designer-kit-bootstrap`
- 项目职责：这个项目负责启动并细化 UI 设计能力体系，沉淀总入口、细分工作流、模板、评分表和导出包。
- 何时使用：当你要继续完善 UI 设计角色、拆分页面评审、组件设计、设计系统检查等细分能力时，使用这个项目。 当你要执行一次具体 UI 设计任务时，优先使用： 14-exports/ui-designer-kit/START-HERE.md
- 关键产物：`04-workflows/ui-designer/ui-designer-workflow.md` `04-workflows/ui-designer/design-specification-workflow.md` `04-workflows/ui-designer/responsive-adaptation-workflow.md` `04-workflows/ui-designer/design-input-analysis-workflow.md`
- 目标：建设并细化 UI 设计角色能力包。
- 当前状态：已完成设计治理能力版，并补齐设计规范确认、设计系统检查、响应式与多端适配、页面类型模式、组件库规划、可访问性与可用性检查、设计到开发实现约束能力，已同步到 `14-exports/ui-designer-kit/`。
- 推荐下一步：使用一个真实页面设计任务验证 `14-exports/ui-designer-kit/`，重点观察是否能正确选择设计系统检查、设计规范确认、响应式适配、页面类型模式、组件库规划、信息架构、交互状态、可访问性与可用性检查、设计评审、设计交接或开发实现约束。
- 启动方式：

```text
请使用 12-projects/ui-designer/capability-building/ui-designer-kit-bootstrap 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/ui-designer/capability-building/ui-designer-kit-bootstrap 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```

### 测试工程师项目

- 角色目录：`12-projects/tester/`
- 项目数量：1

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：1

##### 测试工程师能力包启动项目

- 状态：completed
- 路径：`12-projects/tester/capability-building/tester-kit-bootstrap`
- 项目职责：这个项目负责启动并细化测试角色能力体系，沉淀总入口、细分工作流、模板、评分表和导出包。
- 何时使用：当你要继续完善测试角色、拆分缺陷复现、回归测试、发布验收等细分能力时，使用这个项目。 当你要执行一次具体测试任务时，优先使用： 14-exports/tester-kit/START-HERE.md
- 关键产物：`04-workflows/tester/tester-workflow.md` `04-workflows/tester/test-scope-analysis-workflow.md` `04-workflows/tester/test-case-design-workflow.md` `04-workflows/tester/regression-test-workflow.md`
- 目标：建设并细化测试工程师角色能力包。
- 当前状态：已完成测试治理能力版，并补齐验收标准检查、测试策略规划、测试数据与环境准备、接口与集成测试、兼容性测试、非功能风险测试、探索式测试、自动化测试规划、测试执行报告能力，已同步到 `14-exports/tester-kit/`。
- 推荐下一步：使用一个真实 PRD、验收标准或开发变更验证 `14-exports/tester-kit/`，重点观察是否能正确选择验收标准检查、测试策略规划、测试范围分析、测试数据与环境准备、测试用例设计、接口与集成测试、兼容性测试、非功能风险测试、回归测试、探索式测试、自动化测试规划、缺陷复现、测试执行报告或发布验收。
- 启动方式：

```text
请使用 12-projects/tester/capability-building/tester-kit-bootstrap 继续这个项目，并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。
```

- 使用示例：

```text
请使用 12-projects/tester/capability-building/tester-kit-bootstrap 继续这个能力建设项目，
并先阅读 README.md、00-progress/memory-summary.md 和 00-progress/next-actions.md。

我想要优化或继续建设这个能力：
{写你的想法或修改要求}

请按项目流程更新 input、analysis、prompt、output、review 和 lessons。
```
