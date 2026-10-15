# 可用资产索引

本文件由 `tools/generate_asset_index.py` 自动生成，用来回答：当前 WorkflowProject 里有哪些能力可以直接使用。

它和 `12-projects/project-index.md` 的区别：

- `project-index.md` 看具体项目：项目是怎么来的、现在到哪一步、下次怎么继续。
- `asset-index.md` 看可复用资产：现在有哪些角色包、工作流、模板、评分表、标准和脚本可以调用。

刷新方式：

```bash
python3 tools/generate_asset_index.py
```

如果要同时刷新项目索引、控制台数据和 XMind，运行：

```bash
python3 tools/refresh_maps.py
```

## 先用哪个

| 场景 | 推荐入口 |
| --- | --- |
| 不知道该用哪个产品能力 | `14-exports/product-manager-kit/START-HERE.md` |
| 不知道该用哪个开发能力 | `14-exports/developer-kit/START-HERE.md` |
| 想继续某个历史项目 | `12-projects/project-index.md` |
| 想找某个工作流或模板 | 本文件对应章节 |
| 想刷新全局视图 | `python3 tools/refresh_maps.py` |

## 角色能力包

### developer-kit

- 路径：`14-exports/developer-kit`
- 入口：`14-exports/developer-kit/START-HERE.md`
- 作用：`developer-kit` 是从 WorkflowProject 中拆分出来的开发治理能力包。
- 使用示例：

```text
请使用 developer-kit 处理我的任务：{写下你的任务或材料}
```

### 产品经理能力包

- 路径：`14-exports/product-manager-kit`
- 入口：`14-exports/product-manager-kit/START-HERE.md`
- 作用：这是从 WorkflowProject 导出的产品经理独立能力包。
- 使用示例：

```text
请使用 product-manager-kit 处理我的任务：{写下你的任务或材料}
```

### project-governance-kit

- 路径：`14-exports/project-governance-kit`
- 入口：`14-exports/project-governance-kit/START-HERE.md`
- 作用：`project-governance-kit` 是面向真实代码项目的 AI 开发前置治理能力包。
- 使用示例：

```text
请使用 project-governance-kit 处理我的任务：{写下你的任务或材料}
```

### team-orchestration-kit

- 路径：`14-exports/team-orchestration-kit`
- 入口：`14-exports/team-orchestration-kit/START-HERE.md`
- 作用：`team-orchestration-kit` 是从 WorkflowProject 中拆分出来的跨角色团队总调度能力包。
- 使用示例：

```text
请使用 team-orchestration-kit 处理我的任务：{写下你的任务或材料}
```

### tester-kit

- 路径：`14-exports/tester-kit`
- 入口：`14-exports/tester-kit/START-HERE.md`
- 作用：`tester-kit` 是从 WorkflowProject 导出的测试工程师能力包。
- 使用示例：

```text
请使用 tester-kit 处理我的任务：{写下你的任务或材料}
```

### ui-designer-kit

- 路径：`14-exports/ui-designer-kit`
- 入口：`14-exports/ui-designer-kit/START-HERE.md`
- 作用：`ui-designer-kit` 是从 WorkflowProject 导出的 UI 设计能力包。
- 使用示例：

```text
请使用 ui-designer-kit 处理我的任务：{写下你的任务或材料}
```

### WorkflowProject 统一能力包

- 路径：`14-exports/workflowproject-kit`
- 入口：`14-exports/workflowproject-kit/START-HERE.md`
- 作用：这是从 WorkflowProject 导出的可携带开发治理包。它把项目治理、跨角色调度、产品、UI、开发和测试能力放在一个 Skill 目录中，适合复制到其他代码项目后直接安装。
- 使用示例：

```text
请使用 workflowproject-kit 处理我的任务：{写下你的任务或材料}
```

## 产品经理

### 工作流

- `04-workflows/product-manager/acceptance-criteria-workflow.md`：验收标准生成工作流。把 PRD、功能说明和功能清单转化为可观察、可验证、可被开发和测试承接的验收标准。
- `04-workflows/product-manager/competitor-analysis-workflow.md`：竞品分析工作流。把竞品资料、截图、页面结构、功能说明或体验记录整理成竞品功能拆解、差异点、可借鉴点、风险和产品机会。
- `04-workflows/product-manager/feature-planning-workflow.md`：功能规划工作流。把产品目标、PRD、功能清单和业务约束整理成可执行的功能规划，明确当前版本先做什么、后做什么、暂不做什么。
- `04-workflows/product-manager/prd-generation-workflow.md`：PRD 生成工作流。把已经完成的需求分析结果转化为可被设计、开发、测试和后续项目管理承接的 PRD 初稿。
- `04-workflows/product-manager/priority-decision-workflow.md`：优先级判断工作流。把需求、功能、用户反馈、竞品机会和业务约束转化为可解释的优先级建议，帮助产品经理判断先做什么、后做什么、暂不做什么。
- `04-workflows/product-manager/product-manager-workflow.md`：产品经理总入口工作流。这是产品经理角色的总入口。
- `04-workflows/product-manager/product-roadmap-workflow.md`：产品路线图工作流。把产品策略判断、需求池、优先级判断、版本规划、业务目标和资源约束整理成中长期产品路线图，帮助产品经理说明未来一段时间产品往哪里走、每个阶段解决什么问题、哪些方向先后推进。
- `04-workflows/product-manager/product-strategy-workflow.md`：产品策略判断工作流。把用户问题、业务目标、市场机会、竞品变化和资源约束整理成可解释的产品策略判断，帮助产品经理判断某个方向是否值得推进、为什么现在做、优先服务谁、后续应该进入哪个产品工作流。
- `04-workflows/product-manager/requirement-analysis-workflow.md`：需求分析工作流。把用户想法、业务背景、需求草稿、用户反馈或会议纪要整理成结构化需求分析结果。
- `04-workflows/product-manager/requirement-change-evaluation-workflow.md`：需求变更评估工作流。在路线图、版本规划、PRD 或开发排期已经形成后，对新增需求、范围变化、优先级调整或需求取消进行影响评估，帮助产品经理判断变更能不能接、什么时候接、会影响什么、需要谁确认。
- `04-workflows/product-manager/requirement-pool-workflow.md`：需求池管理工作流。把来自用户反馈、业务输入、需求分析、竞品分析、产品策略判断和团队讨论的需求整理成可长期维护的需求池，帮助产品经理追踪需求来源、当前状态、价值线索、优先级、版本归属和后续动作。
- `04-workflows/product-manager/user-feedback-workflow.md`：用户反馈整理工作流。把零散用户反馈、吐槽、客服记录、访谈摘录或评论整理成结构化产品线索，帮助产品经理判断是否进入需求分析。
- `04-workflows/product-manager/user-story-workflow.md`：用户故事生成工作流。把 PRD、用户场景、功能规划和功能说明转化为用户视角的故事表达，让设计、开发和测试理解功能背后的用户目标和价值。
- `04-workflows/product-manager/version-planning-workflow.md`：版本规划工作流。把产品目标、功能规划、优先级判断、资源约束和风险整理成阶段化版本路线，明确 v1、v1.1、v2 分别做什么。
- `04-workflows/product-manager/version-retrospective-workflow.md`：版本复盘工作流。在一个版本完成、上线或阶段结束后，复盘目标达成、需求交付、变更影响、质量问题、协作问题、用户反馈和后续改进，帮助产品经理把一次版本结果转化为下一轮产品决策依据。

### 模板

- `06-templates/product-manager/acceptance-criteria-template.md`：验收标准模板。当已经有 PRD、功能说明或功能清单，需要生成验收标准时使用。
- `06-templates/product-manager/competitor-analysis-template.md`：竞品分析模板。当已经有竞品资料、截图、页面说明、体验记录或用户评价，需要整理成竞品分析时使用。
- `06-templates/product-manager/feature-planning-template.md`：功能规划模板。当已经有 PRD、功能清单、产品目标或业务约束，需要拆分功能范围和优先级时使用。
- `06-templates/product-manager/prd-template.md`：PRD 模板。当已经完成需求分析，需要生成 PRD 初稿时使用。
- `06-templates/product-manager/priority-decision-template.md`：优先级判断模板。当需要在多个需求、功能、反馈机会或竞品启发之间判断先后顺序时使用。
- `06-templates/product-manager/product-roadmap-template.md`：产品路线图模板。当需要基于产品策略、需求池、优先级判断和版本规划生成中长期产品路线图时使用。
- `06-templates/product-manager/product-strategy-template.md`：产品策略判断模板。当需要判断一个产品方向、机会点、策略主题或功能方向是否值得推进时使用。
- `06-templates/product-manager/requirement-analysis-template.md`：需求分析模板。当用户提供一个产品想法、需求草稿、会议纪要、用户反馈或业务背景，需要先整理成结构化需求分析时使用。
- `06-templates/product-manager/requirement-change-evaluation-template.md`：需求变更评估模板。当 PRD、版本规划、路线图或开发排期已经形成后，出现新增需求、范围变化、优先级调整或需求取消时使用。
- `06-templates/product-manager/requirement-pool-template.md`：需求池管理模板。当需要把多个来源的需求、反馈、想法或业务输入整理成可长期维护的需求池时使用。
- `06-templates/product-manager/user-feedback-template.md`：用户反馈整理模板。当已经有用户反馈、客服记录、访谈摘录、社群讨论或评论，需要整理成产品线索时使用。
- `06-templates/product-manager/user-story-template.md`：用户故事模板。当已经有 PRD、用户场景、功能清单或功能说明，需要生成用户故事时使用。
- `06-templates/product-manager/version-planning-template.md`：版本规划模板。当已经有产品目标、功能规划、优先级判断或资源约束，需要生成版本路线时使用。
- `06-templates/product-manager/version-retrospective-template.md`：版本复盘模板。当一个版本完成、上线或阶段结束后，需要复盘目标达成、需求交付、变更影响、质量问题、协作问题和后续改进时使用。

## 开发工程师

### 工作流

- `04-workflows/developer/ai-collaboration-retrospective-workflow.md`：AI 协作复盘工作流。在一次 AI 协作开发、评审、发布或故障处理之后，帮助用户复盘 AI 协作中的失控点、误判、漏测和规则缺口，并沉淀为后续可复用规则。
- `04-workflows/developer/architecture-decision-record-workflow.md`：架构决策记录工作流。当项目出现关键技术或架构选择时，帮助 AI 记录决策背景、备选方案、取舍原因、影响范围和后续复盘点。
- `04-workflows/developer/change-risk-assessment-workflow.md`：变更风险评估工作流。在代码修改前，帮助 AI 判断本次变更的风险等级，并决定是否可以直接执行、是否需要先输出方案、是否必须等待人工确认。
- `04-workflows/developer/code-review-workflow.md`：代码评审工作流。在代码实现、测试与文档同步之后，帮助 AI 对本次变更进行最终评审，优先发现 bug、风险、边界破坏、漏测和文档不一致。
- `04-workflows/developer/data-api-contract-workflow.md`：数据/API/状态契约工作流。当需求或问题涉及接口字段、数据模型、状态归属、前后端协作、缓存、错误处理或兼容性时，帮助 AI 明确契约边界，避免随手改字段、随手改状态、随手跨模块取数据。
- `04-workflows/developer/dependency-and-tech-debt-workflow.md`：依赖与技术债治理工作流。在项目长期维护中，帮助 AI 判断是否应该新增、升级、替换或移除依赖，并记录临时方案和技术债的偿还计划。
- `04-workflows/developer/developer-kit-workflow.md`：开发治理总入口工作流。这是开发角色的总入口。
- `04-workflows/developer/documentation-sync-workflow.md`：文档同步工作流。在代码实现和验证完成后，帮助 AI 判断哪些项目文档需要同步更新，并以最小必要范围更新文档。
- `04-workflows/developer/environment-config-governance-workflow.md`：环境与配置治理工作流。在项目长期维护中，帮助 AI 管理环境变量、启动配置、构建配置、部署配置和不同环境之间的差异。
- `04-workflows/developer/impact-analysis-workflow.md`：影响范围分析工作流。在进入代码实现前，帮助 AI 把变更影响拆成具体的文件、模块、接口、数据、测试和文档清单。
- `04-workflows/developer/implementation-workflow.md`：代码实现执行工作流。在影响范围、风险等级和模块边界已经明确后，指导 AI 稳定完成代码修改。
- `04-workflows/developer/issue-diagnosis-workflow.md`：问题定位工作流。当用户反馈报错、异常、白屏、接口失败、性能变慢、测试失败或线上问题时，帮助 AI 先定位问题，再决定是否进入修复实现。
- `04-workflows/developer/minimal-change-governance-workflow.md`：最小必要变更治理工作流。用于在开发前、实现中和代码评审时抑制 AI 过度设计、过度编码和无意义扩展。
- `04-workflows/developer/module-boundary-analysis-workflow.md`：模块边界分析工作流。当需求涉及多个模块、模块职责不清或可能新增模块时，帮助 AI 判断模块边界和协作方式。
- `04-workflows/developer/project-bootstrap-workflow.md`：新项目启动治理工作流。在一个新代码项目启动时，帮助用户建立适合 AI 协作开发的基础治理结构。
- `04-workflows/developer/project-understanding-workflow.md`：已有项目理解工作流。在接手一个已经存在的代码项目时，帮助 AI 先建立项目全局理解，再决定如何进入开发。
- `04-workflows/developer/release-and-rollback-workflow.md`：发布与回滚治理工作流。在项目准备上线或交付时，帮助 AI 梳理发布前检查、发布步骤、回滚方案、上线后观察和异常处理。
- `04-workflows/developer/requirement-to-architecture-workflow.md`：需求到架构影响分析工作流。当一个产品需求准备进入开发时，帮助 AI 把需求翻译成开发可执行前的架构影响分析。
- `04-workflows/developer/security-permission-workflow.md`：安全与权限治理工作流。当开发任务涉及登录、鉴权、权限、用户数据、密钥、上传下载、支付、隐私、管理后台或生产配置时，帮助 AI 先识别安全和权限风险，再决定是否可以实现。
- `04-workflows/developer/testing-verification-workflow.md`：测试与验收工作流。在代码实现完成后，帮助 AI 根据变更范围和风险等级制定并执行合适的验证方案。
- `04-workflows/developer/workflow-orchestration-guide.md`：开发工作流协同编排指南。本指南用于增强 developer-kit 内部工作流之间的协同能力。

### 模板

- `06-templates/developer/ai-collaboration-retrospective-template.md`：AI 协作复盘报告模板。1. 2. 3.
- `06-templates/developer/architecture-decision-record-template.md`：ADR 模板。推荐格式：
- `06-templates/developer/change-risk-assessment-template.md`：变更风险评估报告模板。说明：
- `06-templates/developer/code-review-template.md`：代码评审报告模板。可交付 / 修正后交付 / 暂不交付 / 需要人工确认
- `06-templates/developer/data-api-contract-template.md`：数据/API/状态契约报告。打开文件查看详细说明。
- `06-templates/developer/dependency-and-tech-debt-template.md`：依赖与技术债治理报告模板。新增依赖 / 升级依赖 / 替换依赖 / 移除依赖 / 临时方案 / 技术债记录 / 技术债偿还
- `06-templates/developer/documentation-sync-template.md`：文档同步报告模板。1. 2. 3.
- `06-templates/developer/environment-config-governance-template.md`：环境与配置治理报告模板。环境变量 / 启动命令 / 构建命令 / 部署配置 / CI/CD / Docker / 第三方服务 / 数据库 / 安全配置
- `06-templates/developer/impact-analysis-template.md`：影响范围分析报告模板。入口 -> 调用模块 -> 数据/状态 -> 输出 -> 异常处理
- `06-templates/developer/implementation-template.md`：实现交付说明模板。1. 2. 3.
- `06-templates/developer/issue-diagnosis-template.md`：问题定位报告。打开文件查看详细说明。
- `06-templates/developer/minimal-change-governance-template.md`：最小必要变更治理模板。-
- `06-templates/developer/module-boundary-analysis-template.md`：模块边界分析报告模板。说明本次分析的是：
- `06-templates/developer/project-bootstrap-template.md`：新项目启动治理模板。当一个新代码项目准备开始开发，且希望 Codex、Cursor 等 AI 工具长期参与协作时使用。
- `06-templates/developer/project-understanding-template.md`：项目理解报告模板。用一句话说明这个项目是做什么的。
- `06-templates/developer/release-and-rollback-template.md`：发布与回滚治理报告模板。说明无法完整回滚时如何降低影响。
- `06-templates/developer/requirement-to-architecture-template.md`：架构影响分析报告模板。用 3 到 5 句话说明：
- `06-templates/developer/security-permission-template.md`：安全与权限治理报告。打开文件查看详细说明。
- `06-templates/developer/testing-verification-template.md`：测试与验收报告模板。说明本次验证要证明什么。
- `06-templates/developer/workflow-orchestration-template.md`：开发工作流协同编排记录。打开文件查看详细说明。

## UI 设计

### 工作流

- `04-workflows/ui-designer/accessibility-usability-review-workflow.md`：可访问性与可用性检查工作流。用于检查 UI 设计是否易用、可理解、可操作，并覆盖基础可访问性要求。
- `04-workflows/ui-designer/component-library-planning-workflow.md`：组件库规划工作流。用于把页面设计需求拆成可复用组件、组件变体、组件状态和组件治理规则，避免每个页面都临时设计一套。
- `04-workflows/ui-designer/design-handoff-workflow.md`：设计交接工作流。把 UI 设计输出整理成产品、开发、测试都能继续使用的交接说明。
- `04-workflows/ui-designer/design-input-analysis-workflow.md`：设计输入分析工作流。把 PRD、需求分析、用户故事、竞品页面、品牌资料或用户描述整理成 UI 设计可以承接的输入。
- `04-workflows/ui-designer/design-review-workflow.md`：设计评审工作流。评审 UI brief、页面结构、组件说明或设计稿说明是否满足产品目标、用户场景、信息架构、可用性和交接要求。
- `04-workflows/ui-designer/design-specification-workflow.md`：设计规范确认工作流。在进入页面结构、组件设计或视觉方向之前，先确认当前项目需要遵守什么样的设计规范。
- `04-workflows/ui-designer/design-system-audit-workflow.md`：设计系统检查工作流。用于检查当前项目是否已有可遵守的设计系统、品牌规范、组件规范和平台规范，并判断新设计应该复用、扩展还是补齐规范。
- `04-workflows/ui-designer/design-to-development-handoff-workflow.md`：设计到开发实现约束工作流。用于把 UI 设计方案转换成开发可实现、可估算、可验收的实现约束，减少设计交接后反复沟通。
- `04-workflows/ui-designer/design-token-workflow.md`：设计令牌与平台适配工作流。把设计规范转换成平台中立的设计令牌，并根据目标平台输出对应的适配说明或实现文件。
- `04-workflows/ui-designer/information-architecture-workflow.md`：信息架构工作流。把设计输入整理成页面信息架构，明确页面需要呈现什么、信息优先级是什么、内容之间如何组织。
- `04-workflows/ui-designer/interaction-optimization-workflow.md`：交互体验优化工作流。专门处理“操作不方便、点击区域太小、流程绕、反馈不清、页面难看或视觉层级混乱”等问题，把问题转成可执行的 UI 优化方案。
- `04-workflows/ui-designer/interaction-state-workflow.md`：交互状态设计工作流。围绕页面、组件或流程，补齐用户操作过程中的状态、反馈、异常和边界场景。
- `04-workflows/ui-designer/page-type-pattern-workflow.md`：页面类型设计模式工作流。用于根据页面类型选择合适的信息结构、布局模式、组件组合和交互模式，避免每个页面从零规划。
- `04-workflows/ui-designer/responsive-adaptation-workflow.md`：响应式与多端适配工作流。为 Web、移动端、iPad、小程序、桌面端或多端产品设计布局适配策略，避免只给一个静态页面结构。
- `04-workflows/ui-designer/ui-designer-workflow.md`：UI 设计总入口工作流。这是 UI 设计角色的总入口。

### 模板

- `06-templates/ui-designer/accessibility-usability-review-template.md`：可访问性与可用性检查模板。打开文件查看详细说明。
- `06-templates/ui-designer/component-library-planning-template.md`：组件库规划模板。1. 2. 3.
- `06-templates/ui-designer/design-handoff-template.md`：设计交接模板。产品 / 开发 / 测试 / 多角色
- `06-templates/ui-designer/design-input-analysis-template.md`：设计输入分析模板。### 范围内
- `06-templates/ui-designer/design-review-template.md`：设计评审模板。可交接 / 修正后交接 / 暂不交接 / 需要用户确认
- `06-templates/ui-designer/design-specification-template.md`：设计规范确认模板。### 品牌规范
- `06-templates/ui-designer/design-system-audit-template.md`：设计系统检查模板。-
- `06-templates/ui-designer/design-to-development-handoff-template.md`：设计到开发实现约束模板。打开文件查看详细说明。
- `06-templates/ui-designer/information-architecture-template.md`：信息架构模板。进入页面结构 / 进入交互状态 / 需要补充输入
- `06-templates/ui-designer/interaction-optimization-template.md`：交互体验优化方案模板。打开文件查看详细说明。
- `06-templates/ui-designer/interaction-state-template.md`：交互状态模板。打开文件查看详细说明。
- `06-templates/ui-designer/page-type-pattern-template.md`：页面类型设计模式模板。1. 2. 3.
- `06-templates/ui-designer/platform-adaptation-template.md`：平台适配说明模板。### 字体和文字渲染
- `06-templates/ui-designer/responsive-adaptation-template.md`：响应式与多端适配模板。打开文件查看详细说明。
- `06-templates/ui-designer/ui-brief-template.md`：UI Brief 模板。### 品牌规范

## 测试工程师

### 工作流

- `04-workflows/tester/acceptance-criteria-review-workflow.md`：验收标准检查工作流。用于检查 PRD、用户故事或开发任务中的验收标准是否可测试、可判断、可追踪。
- `04-workflows/tester/api-integration-test-workflow.md`：接口与集成测试工作流。用于检查接口契约、前后端集成、模块协作和外部服务依赖是否符合预期。
- `04-workflows/tester/automation-test-planning-workflow.md`：自动化测试规划工作流。用于判断哪些测试适合自动化、优先级如何、自动化收益和维护成本是否合理。
- `04-workflows/tester/compatibility-test-workflow.md`：兼容性测试工作流。用于规划 Web、移动端、桌面端、多浏览器、多系统、多设备和特殊屏幕形态的兼容测试范围。
- `04-workflows/tester/defect-reproduction-workflow.md`：缺陷复现工作流。把用户反馈、报错截图、日志、测试失败或线上问题整理成可复现、可定位、可交给开发处理的缺陷说明。
- `04-workflows/tester/exploratory-test-workflow.md`：探索式测试工作流。用于在需求和用例之外，基于风险、经验和用户行为探索潜在问题。
- `04-workflows/tester/non-functional-risk-test-workflow.md`：非功能风险测试工作流。用于识别性能、稳定性、安全、可访问性、可用性、日志监控和数据一致性等非功能风险。
- `04-workflows/tester/regression-test-workflow.md`：回归测试范围工作流。根据开发变更、影响模块、历史风险和发布范围，判断需要回归哪些功能、哪些路径可以抽样、哪些风险需要人工确认。
- `04-workflows/tester/release-acceptance-workflow.md`：发布验收工作流。在版本发布、上线或交付前，整理测试结果、未解决问题、回归状态和发布风险，形成是否可以发布的验收建议。
- `04-workflows/tester/test-case-design-workflow.md`：测试用例设计工作流。基于测试范围、PRD、验收标准和开发变更，设计可执行的测试场景和测试用例。
- `04-workflows/tester/test-data-environment-workflow.md`：测试数据与环境准备工作流。用于明确测试执行所需的环境、账号、权限、数据状态、配置和外部依赖。
- `04-workflows/tester/test-execution-report-workflow.md`：测试执行报告工作流。用于把测试执行结果、阻塞问题、缺陷状态、风险和发布建议整理成可决策报告。
- `04-workflows/tester/test-scope-analysis-workflow.md`：测试范围分析工作流。把 PRD、验收标准、开发变更或缺陷反馈整理成测试范围和非范围，明确本次测试应该覆盖什么、不覆盖什么、风险在哪里。
- `04-workflows/tester/test-strategy-planning-workflow.md`：测试策略规划工作流。用于在测试执行前确定测试目标、测试层级、测试方法、风险优先级和资源投入方式。
- `04-workflows/tester/tester-workflow.md`：测试工程师总入口工作流。这是测试角色的总入口。

### 模板

- `06-templates/tester/acceptance-criteria-review-template.md`：验收标准检查模板。-
- `06-templates/tester/api-integration-test-template.md`：接口与集成测试模板。-
- `06-templates/tester/automation-test-planning-template.md`：自动化测试规划模板。-
- `06-templates/tester/compatibility-test-template.md`：兼容性测试模板。打开文件查看详细说明。
- `06-templates/tester/defect-reproduction-template.md`：缺陷复现模板。1. 2. 3.
- `06-templates/tester/exploratory-test-template.md`：探索式测试模板。-
- `06-templates/tester/non-functional-risk-test-template.md`：非功能风险测试模板。-
- `06-templates/tester/regression-test-template.md`：回归测试范围模板。可回归 / 补充后回归 / 暂不回归
- `06-templates/tester/release-acceptance-template.md`：发布验收模板。可发布 / 修复后发布 / 暂缓发布 / 需要用户确认
- `06-templates/tester/test-case-template.md`：测试用例模板。打开文件查看详细说明。
- `06-templates/tester/test-data-environment-template.md`：测试数据与环境准备模板。-
- `06-templates/tester/test-execution-report-template.md`：测试执行报告模板。-
- `06-templates/tester/test-plan-template.md`：测试计划与用例模板。### 范围内
- `06-templates/tester/test-scope-analysis-template.md`：测试范围分析模板。可进入 / 补充后进入 / 暂不进入
- `06-templates/tester/test-strategy-planning-template.md`：测试策略规划模板。打开文件查看详细说明。

## 通用能力

### 工作流

- `04-workflows/common/agent-orchestration-workflow.md`：Agent 调度工作流。根据任务复杂度决定直接调用 Skill，或由父 Agent 创建子 Agent 协作，控制上下文长度、角色边界和最终验收。
- `04-workflows/common/asset-promotion-workflow.md`：资产提升工作流。判断一个项目产物是否应该从 `12-projects/` 提升到全局资产目录。
- `04-workflows/common/capability-export-workflow.md`：能力导出工作流。把 WorkflowProject 中已经沉淀稳定的角色能力或专项能力，整理成可以脱离当前项目独立使用的能力包。
- `04-workflows/common/example-extraction-workflow.md`：案例提取工作流。将高质量任务沉淀为可复用案例。
- `04-workflows/common/idea-to-input-workflow.md`：想法转输入工作流。把用户口头描述、模糊想法、零散需求或不完整背景，整理成一份可以进入后续流程的标准输入文档。
- `04-workflows/common/input-analysis-workflow.md`：输入分析工作流。将原始资料分析为 AI 可处理的结构化输入。
- `04-workflows/common/iteration-memory-management-workflow.md`：迭代记忆管理工作流。当项目经过多轮产品、开发、设计、测试或复盘迭代后，帮助 AI 把大量历史记录整理成可继续使用的项目记忆，降低后续上下文读取成本。
- `04-workflows/common/output-review-workflow.md`：输出评审工作流。评审 AI 输出是否符合任务要求，是否可进入 accepted 或 example。
- `04-workflows/common/project-execution-workflow.md`：项目执行总控工作流。把一次具体任务从创建项目到最终沉淀串成完整流程。
- `04-workflows/common/project-governance-workflow.md`：项目治理与开发前置工作流。本工作流是 WorkflowProject 面向真实代码项目的通用主流程。
- `04-workflows/common/prompt-generation-workflow.md`：正式提示词生成工作流。使用模板和输入资料生成正式提示词。
- `04-workflows/common/template-generation-workflow.md`：模板生成工作流。从原始资料或优秀案例中抽象可复用模板。
- `04-workflows/common/template-iteration-workflow.md`：模板迭代工作流。基于多次使用反馈持续优化模板。

### 模板

- `06-templates/common/agent-result-report-template.md`：子 Agent 结果回报。打开文件查看详细说明。
- `06-templates/common/agent-task-brief-template.md`：子 Agent 任务简报。打开文件查看详细说明。
- `06-templates/common/capability-export-template.md`：能力导出模板。当需要把 WorkflowProject 中某个角色或某组能力导出成独立能力包时使用。
- `06-templates/common/framework-bootstrap-template.md`：框架启动提示词模板。当你需要搭建一个新的 AI 工作流文档项目、AI 协作规范项目或多角色文档工程项目时，使用本模板。
- `06-templates/common/general-task-template.md`：通用任务提示词模板。当任务暂时无法明确归到产品经理、开发工程师、UI 设计师等具体角色时，使用这个通用模板。
- `06-templates/common/iteration-memory-summary-template.md`：项目记忆摘要。打开文件查看详细说明。
- `06-templates/common/project-governance-checklist-template.md`：项目治理检查清单模板。### 已确认事实

## Meta 能力

### 模板

- `06-templates/meta/example-extractor.md`：案例提取器。当某次任务结果质量较高，需要沉淀为案例包时使用。
- `06-templates/meta/explainable-project-runner.md`：可解释项目运行助手。当用户希望 AI 不只是执行任务，还要解释“做了什么、为什么做、怎么影响项目、下一步怎么判断”时使用。
- `06-templates/meta/idea-to-input-generator.md`：想法转输入生成器。当用户只有一句话、模糊想法、零散需求或口头描述，还没有形成标准 input 文档时使用。
- `06-templates/meta/output-reviewer.md`：输出评审器。用于评审 AI 输出结果是否合格，是否可以进入 accepted 或 example。
- `06-templates/meta/project-runner.md`：项目运行助手。当你已经有一个 `12-projects/` 下的具体项目，需要 AI 按项目规则协助推进下一步时，使用本模板。
- `06-templates/meta/prompt-generator.md`：正式提示词生成器。当你已经有模板和具体输入资料，需要生成可直接执行的正式提示词时使用。
- `06-templates/meta/template-generator.md`：模板生成器。当你有原始资料，但不知道如何抽象成可复用模板时，使用本 meta 模板。
- `06-templates/meta/template-optimizer.md`：模板优化器。当某个模板经过多次使用后，需要根据案例和问题进行优化时使用。

## 评分表

### 验收标准检查评分表

- 路径：`11-evaluations/output-scorecards/acceptance-criteria-review-scorecard.md`
- 作用：适用对象：验收标准检查、需求可测性检查
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/acceptance-criteria-review-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 验收标准评分表

- 路径：`11-evaluations/output-scorecards/acceptance-criteria-scorecard.md`
- 作用：适用对象: 产品经理验收标准输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/acceptance-criteria-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 可访问性与可用性检查评分表

- 路径：`11-evaluations/output-scorecards/accessibility-usability-review-scorecard.md`
- 作用：适用对象：UI 可用性检查、无障碍检查、设计评审
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/accessibility-usability-review-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### Agent 调度验收表

- 路径：`11-evaluations/output-scorecards/agent-orchestration-scorecard.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/agent-orchestration-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### AI 协作复盘评分表

- 路径：`11-evaluations/output-scorecards/ai-collaboration-retrospective-scorecard.md`
- 作用：适用对象: developer-kit AI 协作复盘报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/ai-collaboration-retrospective-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 接口与集成测试评分表

- 路径：`11-evaluations/output-scorecards/api-integration-test-scorecard.md`
- 作用：适用对象：接口测试、集成测试、联调测试
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/api-integration-test-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 架构决策记录评分表

- 路径：`11-evaluations/output-scorecards/architecture-decision-record-scorecard.md`
- 作用：适用对象: developer-kit ADR 文档
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/architecture-decision-record-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 自动化测试规划评分表

- 路径：`11-evaluations/output-scorecards/automation-test-planning-scorecard.md`
- 作用：适用对象：自动化测试策略、自动化测试规划
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/automation-test-planning-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 能力导出评分表

- 路径：`11-evaluations/output-scorecards/capability-export-scorecard.md`
- 作用：用于评估从 WorkflowProject 导出的角色能力包或专项能力包是否完整、清晰、可独立使用、可维护。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/capability-export-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 变更风险评估评分表

- 路径：`11-evaluations/output-scorecards/change-risk-assessment-scorecard.md`
- 作用：适用对象: developer-kit 变更风险评估报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/change-risk-assessment-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 代码评审评分表

- 路径：`11-evaluations/output-scorecards/code-review-scorecard.md`
- 作用：适用对象: developer-kit 代码评审报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/code-review-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 兼容性测试评分表

- 路径：`11-evaluations/output-scorecards/compatibility-test-scorecard.md`
- 作用：适用对象：兼容性测试矩阵、多端设备测试
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/compatibility-test-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 竞品分析评分表

- 路径：`11-evaluations/output-scorecards/competitor-analysis-scorecard.md`
- 作用：适用对象: 产品经理竞品分析输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/competitor-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 组件库规划评分表

- 路径：`11-evaluations/output-scorecards/component-library-planning-scorecard.md`
- 作用：适用对象：组件库规划、组件清单、组件复用方案
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/component-library-planning-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 数据/API/状态契约评分表

- 路径：`11-evaluations/output-scorecards/data-api-contract-scorecard.md`
- 作用：适用对象: developer-kit 数据/API/状态契约报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/data-api-contract-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 缺陷复现评分表

- 路径：`11-evaluations/output-scorecards/defect-reproduction-scorecard.md`
- 作用：适用对象: 缺陷复现报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/defect-reproduction-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 依赖与技术债治理评分表

- 路径：`11-evaluations/output-scorecards/dependency-and-tech-debt-scorecard.md`
- 作用：适用对象: developer-kit 依赖与技术债治理报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/dependency-and-tech-debt-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计交接评分表

- 路径：`11-evaluations/output-scorecards/design-handoff-scorecard.md`
- 作用：适用对象: 设计交接说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-handoff-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计输入分析评分表

- 路径：`11-evaluations/output-scorecards/design-input-analysis-scorecard.md`
- 作用：适用对象: 设计输入分析输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-input-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计评审评分表

- 路径：`11-evaluations/output-scorecards/design-review-scorecard.md`
- 作用：适用对象: UI 设计评审输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-review-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计规范确认评分表

- 路径：`11-evaluations/output-scorecards/design-specification-scorecard.md`
- 作用：适用对象: 设计规范确认输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-specification-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计系统检查评分表

- 路径：`11-evaluations/output-scorecards/design-system-audit-scorecard.md`
- 作用：适用对象：设计系统检查、规范审计、风格一致性检查
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-system-audit-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计到开发实现约束评分表

- 路径：`11-evaluations/output-scorecards/design-to-development-handoff-scorecard.md`
- 作用：适用对象：设计开发交接、实现约束、开发验收说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-to-development-handoff-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 设计令牌与平台适配评分表

- 路径：`11-evaluations/output-scorecards/design-token-scorecard.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/design-token-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 文档同步评分表

- 路径：`11-evaluations/output-scorecards/documentation-sync-scorecard.md`
- 作用：适用对象: developer-kit 文档同步报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/documentation-sync-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 环境与配置治理评分表

- 路径：`11-evaluations/output-scorecards/environment-config-governance-scorecard.md`
- 作用：适用对象: developer-kit 环境与配置治理报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/environment-config-governance-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 探索式测试评分表

- 路径：`11-evaluations/output-scorecards/exploratory-test-scorecard.md`
- 作用：适用对象：探索式测试记录、风险探索报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/exploratory-test-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 功能规划评分表

- 路径：`11-evaluations/output-scorecards/feature-planning-scorecard.md`
- 作用：适用对象: 产品经理功能规划输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/feature-planning-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 影响范围分析评分表

- 路径：`11-evaluations/output-scorecards/impact-analysis-scorecard.md`
- 作用：适用对象: developer-kit 影响范围分析报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/impact-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 代码实现执行评分表

- 路径：`11-evaluations/output-scorecards/implementation-scorecard.md`
- 作用：适用对象: developer-kit 实现交付说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/implementation-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 信息架构评分表

- 路径：`11-evaluations/output-scorecards/information-architecture-scorecard.md`
- 作用：适用对象: 页面信息架构输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/information-architecture-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 交互体验优化评分表

- 路径：`11-evaluations/output-scorecards/interaction-optimization-scorecard.md`
- 作用：适用对象：交互优化方案、可用性问题修复、设计评审和开发交付复核。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/interaction-optimization-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 交互状态评分表

- 路径：`11-evaluations/output-scorecards/interaction-state-scorecard.md`
- 作用：适用对象: 组件状态和交互状态说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/interaction-state-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 问题定位评分表

- 路径：`11-evaluations/output-scorecards/issue-diagnosis-scorecard.md`
- 作用：适用对象: developer-kit 问题定位报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/issue-diagnosis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 最小必要变更治理评分表

- 路径：`11-evaluations/output-scorecards/minimal-change-governance-scorecard.md`
- 作用：适用对象：最小变更方案、实现计划、代码评审中的过度设计检查。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/minimal-change-governance-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 模块边界分析评分表

- 路径：`11-evaluations/output-scorecards/module-boundary-analysis-scorecard.md`
- 作用：适用对象: developer-kit 模块边界分析报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/module-boundary-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 非功能风险测试评分表

- 路径：`11-evaluations/output-scorecards/non-functional-risk-test-scorecard.md`
- 作用：适用对象：性能、稳定性、安全、可用性等非功能风险测试
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/non-functional-risk-test-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 页面类型设计模式评分表

- 路径：`11-evaluations/output-scorecards/page-type-pattern-scorecard.md`
- 作用：适用对象：页面模式、页面骨架、页面类型设计
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/page-type-pattern-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### PRD 评分表

- 路径：`11-evaluations/output-scorecards/prd-scorecard.md`
- 作用：适用对象: 产品经理 PRD 输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/prd-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 优先级判断评分表

- 路径：`11-evaluations/output-scorecards/priority-decision-scorecard.md`
- 作用：适用对象: 产品经理优先级判断输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/priority-decision-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 产品路线图评分表

- 路径：`11-evaluations/output-scorecards/product-roadmap-scorecard.md`
- 作用：用于评估产品路线图输出是否目标清晰、阶段合理、可解释、可沟通，是否可以进入 PRD、版本规划、开发排期或团队对齐。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/product-roadmap-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 产品策略判断评分表

- 路径：`11-evaluations/output-scorecards/product-strategy-scorecard.md`
- 作用：用于评估产品策略判断输出是否足够清晰、可信、可执行，是否可以进入需求分析、优先级判断、版本规划或产品路线图。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/product-strategy-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 新项目启动治理评分表

- 路径：`11-evaluations/output-scorecards/project-bootstrap-scorecard.md`
- 作用：适用对象: developer-kit 新项目启动治理输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/project-bootstrap-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 项目完成检查表

- 路径：`11-evaluations/output-scorecards/project-completion-scorecard.md`
- 作用：用于判断 `12-projects/` 下的一个项目是否已经完成。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/project-completion-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 已有项目理解评分表

- 路径：`11-evaluations/output-scorecards/project-understanding-scorecard.md`
- 作用：适用对象: developer-kit 项目理解报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/project-understanding-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 回归测试评分表

- 路径：`11-evaluations/output-scorecards/regression-test-scorecard.md`
- 作用：适用对象: 回归测试范围输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/regression-test-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 发布验收评分表

- 路径：`11-evaluations/output-scorecards/release-acceptance-scorecard.md`
- 作用：适用对象: 发布验收结论
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/release-acceptance-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 发布与回滚治理评分表

- 路径：`11-evaluations/output-scorecards/release-and-rollback-scorecard.md`
- 作用：适用对象: developer-kit 发布与回滚治理报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/release-and-rollback-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 需求分析评分表

- 路径：`11-evaluations/output-scorecards/requirement-analysis-scorecard.md`
- 作用：适用对象: 产品经理需求分析输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/requirement-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 需求变更评估评分表

- 路径：`11-evaluations/output-scorecards/requirement-change-evaluation-scorecard.md`
- 作用：用于评估需求变更评估输出是否清晰、完整、可解释、可执行，是否可以支持团队做变更决策。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/requirement-change-evaluation-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 需求池管理评分表

- 路径：`11-evaluations/output-scorecards/requirement-pool-scorecard.md`
- 作用：用于评估需求池管理输出是否足够清晰、可维护、可追踪，是否可以支持后续需求分析、产品策略判断、优先级判断、PRD 或版本规划。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/requirement-pool-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 需求到架构影响分析评分表

- 路径：`11-evaluations/output-scorecards/requirement-to-architecture-scorecard.md`
- 作用：适用对象: developer-kit 架构影响分析报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/requirement-to-architecture-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 响应式与多端适配评分表

- 路径：`11-evaluations/output-scorecards/responsive-adaptation-scorecard.md`
- 作用：适用对象: 响应式布局、多端适配、iPad 适配说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/responsive-adaptation-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 角色能力包验收评分表

- 路径：`11-evaluations/output-scorecards/role-kit-acceptance-scorecard.md`
- 作用：适用对象: 角色能力包、导出能力包、角色总入口
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/role-kit-acceptance-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 安全与权限治理评分表

- 路径：`11-evaluations/output-scorecards/security-permission-scorecard.md`
- 作用：适用对象: developer-kit 安全与权限治理报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/security-permission-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 跨角色团队总调度评分表

- 路径：`11-evaluations/output-scorecards/team-orchestration-scorecard.md`
- 作用：适用对象：跨角色团队调度计划、角色协作流、交接验收和 badcase 反馈。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/team-orchestration-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试用例评分表

- 路径：`11-evaluations/output-scorecards/test-case-scorecard.md`
- 作用：适用对象: 测试场景和测试用例
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/test-case-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试数据与环境准备评分表

- 路径：`11-evaluations/output-scorecards/test-data-environment-scorecard.md`
- 作用：适用对象：测试数据准备、测试环境准备
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/test-data-environment-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试执行报告评分表

- 路径：`11-evaluations/output-scorecards/test-execution-report-scorecard.md`
- 作用：适用对象：测试执行报告、阶段测试报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/test-execution-report-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试范围分析评分表

- 路径：`11-evaluations/output-scorecards/test-scope-analysis-scorecard.md`
- 作用：适用对象: 测试范围分析输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/test-scope-analysis-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试策略规划评分表

- 路径：`11-evaluations/output-scorecards/test-strategy-planning-scorecard.md`
- 作用：适用对象：测试策略、测试计划前置规划
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/test-strategy-planning-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试输出评分表

- 路径：`11-evaluations/output-scorecards/tester-scorecard.md`
- 作用：适用对象: 测试计划、测试用例、回归范围、发布验收结论
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/tester-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 测试与验收评分表

- 路径：`11-evaluations/output-scorecards/testing-verification-scorecard.md`
- 作用：适用对象: developer-kit 测试与验收报告
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/testing-verification-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### UI 设计输出评分表

- 路径：`11-evaluations/output-scorecards/ui-design-scorecard.md`
- 作用：适用对象: UI brief、页面结构、组件说明、交互状态说明
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/ui-design-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 理解检查表

- 路径：`11-evaluations/output-scorecards/understanding-check-scorecard.md`
- 作用：用于检查用户是否真正理解 AI 刚刚做了什么，以及是否能判断下一步方向。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/understanding-check-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 用户反馈整理评分表

- 路径：`11-evaluations/output-scorecards/user-feedback-scorecard.md`
- 作用：适用对象: 产品经理用户反馈整理输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/user-feedback-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 用户故事评分表

- 路径：`11-evaluations/output-scorecards/user-story-scorecard.md`
- 作用：适用对象: 产品经理用户故事输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/user-story-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 版本规划评分表

- 路径：`11-evaluations/output-scorecards/version-planning-scorecard.md`
- 作用：适用对象: 产品经理版本规划输出
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/version-planning-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 版本复盘评分表

- 路径：`11-evaluations/output-scorecards/version-retrospective-scorecard.md`
- 作用：用于评估版本复盘输出是否清晰、真实、可解释、可改进，是否可以支持下一轮需求池、路线图、版本规划或流程优化。
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/version-retrospective-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

### 开发工作流协同编排评分表

- 路径：`11-evaluations/output-scorecards/workflow-orchestration-scorecard.md`
- 作用：适用对象: developer-kit 工作流协同编排记录
- 使用示例：

```text
请使用 11-evaluations/output-scorecards/workflow-orchestration-scorecard.md 评审这份输出：{粘贴或指向输出文档}
```

## 标准和检查清单

### Agent 调度标准

- 路径：`05-standards/agent-orchestration-standard.md`
- 作用：规定 WorkflowProject 在不同运行环境中的 Skill、父 Agent 和子 Agent 如何协作，避免简单任务被过度拆分，也避免组合任务被单个 Agent 承担到上下文失控。
- 使用示例：

```text
请按 05-standards/agent-orchestration-standard.md 检查或约束当前工作。
```

### 设计令牌标准

- 路径：`05-standards/design-token-standard.md`
- 作用：规定 UI 设计如何输出可复用、可跨平台转换的设计令牌，避免把设计规范直接绑定到 CSS 或某一个 UI 框架。
- 使用示例：

```text
请按 05-standards/design-token-standard.md 检查或约束当前工作。
```

### 案例标准

- 路径：`05-standards/example-standard.md`
- 作用：一个合格案例建议使用目录形式：
- 使用示例：

```text
请按 05-standards/example-standard.md 检查或约束当前工作。
```

### 导出能力包 START-HERE 标准

- 路径：`05-standards/exported-kit-start-here-standard.md`
- 作用：`START-HERE.md` 是所有导出能力包的统一入口文件。
- 使用示例：

```text
请按 05-standards/exported-kit-start-here-standard.md 检查或约束当前工作。
```

### 输入标准

- 路径：`05-standards/input-standard.md`
- 作用：输入可以来自两类情况：
- 使用示例：

```text
请按 05-standards/input-standard.md 检查或约束当前工作。
```

### 交互质量标准

- 路径：`05-standards/interaction-quality-standard.md`
- 作用：把“好不好用、是否容易操作、视觉是否清楚、流程是否顺畅”转化为产品和 UI 都能执行与验收的规则。
- 使用示例：

```text
请按 05-standards/interaction-quality-standard.md 检查或约束当前工作。
```

### 迭代记忆管理标准

- 路径：`05-standards/iteration-memory-standard.md`
- 作用：本标准用于管理产品经理、开发、设计、测试等角色在持续迭代中产生的大量历史记录。
- 使用示例：

```text
请按 05-standards/iteration-memory-standard.md 检查或约束当前工作。
```

### 输出标准

- 路径：`05-standards/output-standard.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/output-standard.md 检查或约束当前工作。
```

### 项目治理标准

- 路径：`05-standards/project-governance-standard.md`
- 作用：本标准约束 AI 在真实项目中进行长期协作开发时，如何检查和维护项目治理基础。
- 使用示例：

```text
请按 05-standards/project-governance-standard.md 检查或约束当前工作。
```

### 项目标准

- 路径：`05-standards/project-standard.md`
- 作用：默认项目路径：
- 使用示例：

```text
请按 05-standards/project-standard.md 检查或约束当前工作。
```

### 正式提示词标准

- 路径：`05-standards/prompt-standard.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/prompt-standard.md 检查或约束当前工作。
```

### 评审标准

- 路径：`05-standards/review-standard.md`
- 作用：每个维度使用 1 到 5 分：
- 使用示例：

```text
请按 05-standards/review-standard.md 检查或约束当前工作。
```

### 角色能力包生命周期标准

- 路径：`05-standards/role-kit-lifecycle-standard.md`
- 作用：本标准用于统一所有角色能力包的总入口设计。
- 使用示例：

```text
请按 05-standards/role-kit-lifecycle-standard.md 检查或约束当前工作。
```

### 角色标准

- 路径：`05-standards/role-standard.md`
- 作用：一个角色进入 active 状态前，必须具备：
- 使用示例：

```text
请按 05-standards/role-standard.md 检查或约束当前工作。
```

### 模板标准

- 路径：`05-standards/template-standard.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/template-standard.md 检查或约束当前工作。
```

### 工作流标准

- 路径：`05-standards/workflow-standard.md`
- 作用：如果某个 workflow 是角色能力包的总入口，例如：
- 使用示例：

```text
请按 05-standards/workflow-standard.md 检查或约束当前工作。
```

### 通用质量检查清单

- 路径：`05-standards/quality-checklists/common-checklist.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/quality-checklists/common-checklist.md 检查或约束当前工作。
```

### 开发工程师质量检查清单

- 路径：`05-standards/quality-checklists/developer-checklist.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/quality-checklists/developer-checklist.md 检查或约束当前工作。
```

### 产品经理质量检查清单

- 路径：`05-standards/quality-checklists/product-manager-checklist.md`
- 作用：打开文件查看详细说明。
- 使用示例：

```text
请按 05-standards/quality-checklists/product-manager-checklist.md 检查或约束当前工作。
```

### 角色能力包验收清单

- 路径：`05-standards/quality-checklists/role-kit-acceptance-checklist.md`
- 作用：用于验收一个角色能力包是否已经达到“可以交给外部项目或外部 AI 对话使用”的最低标准。
- 使用示例：

```text
请按 05-standards/quality-checklists/role-kit-acceptance-checklist.md 检查或约束当前工作。
```

### 测试质量检查清单

- 路径：`05-standards/quality-checklists/tester-checklist.md`
- 作用：可执行 / 补充后执行 / 暂不执行 / 需要用户确认
- 使用示例：

```text
请按 05-standards/quality-checklists/tester-checklist.md 检查或约束当前工作。
```

### UI 设计质量检查清单

- 路径：`05-standards/quality-checklists/ui-designer-checklist.md`
- 作用：可交接 / 补充后交接 / 暂不交接 / 需要用户确认
- 使用示例：

```text
请按 05-standards/quality-checklists/ui-designer-checklist.md 检查或约束当前工作。
```

## 工具脚本

### create_project.py

- 路径：`tools/create_project.py`
- 作用：创建标准项目目录和 00-06 执行结构。
- 使用示例：

```text
python3 tools/create_project.py
```

### export_unified_kit.py

- 路径：`tools/export_unified_kit.py`
- 作用：项目维护脚本，打开文件查看具体用途。
- 使用示例：

```text
python3 tools/export_unified_kit.py
```

### generate_asset_index.py

- 路径：`tools/generate_asset_index.py`
- 作用：刷新可用资产索引，帮助按能力查找角色包、工作流、模板和评分表。
- 使用示例：

```text
python3 tools/generate_asset_index.py
```

### generate_dashboard_data.py

- 路径：`tools/generate_dashboard_data.py`
- 作用：刷新 React 可视化控制台使用的数据。
- 使用示例：

```text
python3 tools/generate_dashboard_data.py
```

### generate_file_responsibility_xmind.py

- 路径：`tools/generate_file_responsibility_xmind.py`
- 作用：项目维护脚本，打开文件查看具体用途。
- 使用示例：

```text
python3 tools/generate_file_responsibility_xmind.py
```

### generate_operation_flow_xmind.py

- 路径：`tools/generate_operation_flow_xmind.py`
- 作用：项目维护脚本，打开文件查看具体用途。
- 使用示例：

```text
python3 tools/generate_operation_flow_xmind.py
```

### generate_project_index.py

- 路径：`tools/generate_project_index.py`
- 作用：刷新项目索引，帮助判断项目职责、状态和启动方式。
- 使用示例：

```text
python3 tools/generate_project_index.py
```

### generate_xmind.py

- 路径：`tools/generate_xmind.py`
- 作用：项目维护脚本，打开文件查看具体用途。
- 使用示例：

```text
python3 tools/generate_xmind.py
```

### install_project_kits.py

- 路径：`tools/install_project_kits.py`
- 作用：项目维护脚本，打开文件查看具体用途。
- 使用示例：

```text
python3 tools/install_project_kits.py
```

### refresh_maps.py

- 路径：`tools/refresh_maps.py`
- 作用：一键刷新项目索引、资产索引、控制台数据和 XMind 导图。
- 使用示例：

```text
python3 tools/refresh_maps.py
```
