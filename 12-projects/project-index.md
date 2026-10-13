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

## 分组总览

### 跨角色项目

- 角色目录：`12-projects/mixed/`
- 项目数量：2

#### 能力建设项目

- 项目类型：`capability-building`
- 项目数量：2

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
请使用 12-projects/mixed/capability-building/capability-export-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/capability-export-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/mixed/capability-building/workflowproject-framework-refresh 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/mixed/capability-building/workflowproject-framework-refresh 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/acceptance-criteria-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/acceptance-criteria-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/competitor-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/competitor-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/feature-planning-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/feature-planning-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/prd-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/prd-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/priority-decision-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/priority-decision-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/product-manager-capability-system 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-manager-capability-system 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/product-manager-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-manager-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/product-roadmap-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-roadmap-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/product-strategy-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/product-strategy-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/requirement-analysis-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-analysis-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/requirement-change-evaluation-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-change-evaluation-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/requirement-pool-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/requirement-pool-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/user-feedback-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/user-feedback-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/user-story-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/user-story-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/version-planning-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/version-planning-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/capability-building/version-retrospective-workflow 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请使用 12-projects/product-manager/capability-building/version-retrospective-workflow 继续这个能力建设项目，
并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。

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
请使用 12-projects/product-manager/real-cases/ai-template-tool-prd 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
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
请使用 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 继续这个项目，并先阅读 README.md、00-progress/next-actions.md 和 00-progress/progress-log.md。
```

- 使用示例：

```text
请参考 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 的项目结构处理一个真实使用任务。

我的想法是：
{写你的真实需求或产品想法}

请输出到 12-projects/product-manager/real-cases/{项目名}/，
并把核心结果保存到对应的 02-analysis、04-outputs 或 05-review 目录。
```
