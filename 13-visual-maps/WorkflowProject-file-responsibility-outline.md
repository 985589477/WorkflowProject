# WorkflowProject 当前文件与职责（自动扫描）
  职责：本导图由脚本自动扫描当前项目目录生成；新增文件后重新运行脚本即可更新。
- README.md：项目总入口
    职责：说明当前目录的用途、使用方式和注意事项。
- .codex-skill-staging
    职责：项目目录。
  - workflowproject-executor：空目录
      职责：按上级目录规则归类的子目录。
- .gitignore
    职责：项目文件。
- 00-system
    职责：系统规则层：定义项目是什么、如何组织、如何运行。
  - architecture.md：项目架构
      职责：定义总体架构、分层关系和全局目录与项目目录的关系。
  - document-lifecycle.md：文档生命周期
      职责：定义文档生命周期和晋级规则。
  - execution-brief-rules.md：执行前说明规则
      职责：规定 AI 执行前如何说明目标、原因、影响文件、调度角色和预计产出。
  - language-rules.md：语言使用规则
      职责：规定文档默认中文，必要技术标识保留英文。
  - naming-rules.md：命名规则
      职责：规定目录和文件命名方式，以及路径英文、正文中文原则。
  - operating-guide.md：操作指南
      职责：说明如何创建任务、选择角色、使用工作流、生成模板、评审和沉淀。
  - progress-reporting-rules.md：进度汇报规则
      职责：规定项目执行过程中如何汇报当前进度、调度角色、使用工作流和下一步。
  - project-governance-model.md：项目治理模型
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - project-vision.md：项目愿景
      职责：定义项目愿景、目标和非目标。
  - quick-start.md：快速开始
      职责：新用户快速入口：用最短路径说明如何从材料开始完成一次任务。
  - result-report-rules.md：结果报告规则
      职责：规定 AI 执行后如何报告完成内容、文件变化、用途、下一步和风险。
  - terminology.md：术语说明
      职责：解释项目核心术语。
- 01-governance
    职责：项目治理层：定义项目如何维护、变更、评审和管控。
  - decision-records
      职责：决策记录目录：记录重要架构或治理决策。
    - 0001-project-architecture.md：0001 项目架构决策
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - 0002-project-governance-first-repositioning.md：0002 以项目治理为核心重新定位
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - change-management.md：变更管理
      职责：规定变更类型、变更要求和影响范围。
  - contribution-rules.md：贡献规则
      职责：规定新增内容前如何判断归属，以及贡献要求和禁止事项。
  - quality-gates.md：质量门禁
      职责：规定进入正式状态或案例库前必须满足的质量门禁。
  - review-process.md：评审流程
      职责：规定模板、正式提示词、输出和案例的评审流程。
  - versioning-rules.md：版本规则
      职责：规定模板、标准和工作流等内容的版本管理方式。
- 02-roles
    职责：角色定义层：定义 AI 以什么角色参与任务。
  - common
      职责：通用内容目录：存放跨角色可复用内容。
    - role-definition.md：通用角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - developer
      职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
    - minimal-change-guardian.md：最小必要变更守门人
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - role-definition.md：开发工程师角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - marketer
      职责：市场营销目录：预留营销相关角色、工作流或模板。
    - role-definition.md：市场营销角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - product-manager
      职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
    - role-definition.md：产品经理角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - researcher
      职责：研究员目录：预留研究相关角色、工作流或模板。
    - role-definition.md：研究员角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - tester
      职责：按上级目录规则归类的子目录。
    - role-definition.md：测试工程师角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - ui-designer
      职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
    - role-definition.md：UI 设计师角色定义
        职责：定义该角色的职责、常见输入和常见输出。
  - role-registry.md：角色注册表
      职责：登记当前活跃角色和计划支持角色。
- 03-inputs
    职责：全局输入资料层：存放可长期复用的原始资料。
  - external-docs：空目录
      职责：外部文档目录：存放来自外部的资料。
  - meeting-notes：空目录
      职责：会议纪要目录：存放会议记录。
  - raw-materials：空目录
      职责：原始材料目录：存放未加工资料。
  - references：空目录
      职责：参考资料目录：存放参考文档和参考信息。
  - requirements：空目录
      职责：需求资料目录：存放需求类输入。
  - screenshots：空目录
      职责：截图资料目录：存放截图或截图说明。
  - README.md：输入资料
      职责：说明当前目录的用途、使用方式和注意事项。
- 03-prompts：空目录
    职责：项目目录。
- 04-workflows
    职责：工作流层：定义从材料到输出的处理步骤。
  - common
      职责：通用内容目录：存放跨角色可复用内容。
    - README.md：通用工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - agent-orchestration-workflow.md：Agent 调度工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - asset-promotion-workflow.md：资产提升工作流
        职责：用于判断项目产物是否应提升为模板、案例、知识或评估方法。
    - capability-export-workflow.md：能力导出工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - example-extraction-workflow.md：案例提取工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - idea-to-input-workflow.md：想法转输入工作流
        职责：用于把用户口头描述、模糊想法或零散需求整理成标准输入。
    - input-analysis-workflow.md：输入分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - iteration-memory-management-workflow.md：迭代记忆管理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - output-review-workflow.md：输出评审工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - project-execution-workflow.md：项目执行总控工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - project-governance-workflow.md：项目治理与开发前置工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - prompt-generation-workflow.md：正式提示词生成工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - template-generation-workflow.md：模板生成工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - template-iteration-workflow.md：模板迭代工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
  - developer
      职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
    - README.md：开发工程师工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - ai-collaboration-retrospective-workflow.md：AI 协作复盘工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - architecture-decision-record-workflow.md：架构决策记录工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - change-risk-assessment-workflow.md：变更风险评估工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - code-review-workflow.md：代码评审工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - data-api-contract-workflow.md：数据/API/状态契约工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - dependency-and-tech-debt-workflow.md：依赖与技术债治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - developer-kit-workflow.md：开发治理总入口工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - documentation-sync-workflow.md：文档同步工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - environment-config-governance-workflow.md：环境与配置治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - impact-analysis-workflow.md：影响范围分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - implementation-workflow.md：代码实现执行工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - issue-diagnosis-workflow.md：问题定位工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - minimal-change-governance-workflow.md：最小必要变更治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - module-boundary-analysis-workflow.md：模块边界分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - project-bootstrap-workflow.md：新项目启动治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - project-understanding-workflow.md：已有项目理解工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - release-and-rollback-workflow.md：发布与回滚治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - requirement-to-architecture-workflow.md：需求到架构影响分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - security-permission-workflow.md：安全与权限治理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - testing-verification-workflow.md：测试与验收工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - workflow-orchestration-guide.md：开发工作流协同编排指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - marketer
      职责：市场营销目录：预留营销相关角色、工作流或模板。
    - README.md：市场营销工作流
        职责：说明当前目录的用途、使用方式和注意事项。
  - mixed
      职责：跨角色项目目录：承载不属于单一角色的任务项目。
    - README.md：混合角色工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - team-orchestration-workflow.md：跨角色团队总调度工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
  - product-manager
      职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
    - README.md：产品经理工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - acceptance-criteria-workflow.md：验收标准生成工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - competitor-analysis-workflow.md：竞品分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - feature-planning-workflow.md：功能规划工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - prd-generation-workflow.md：PRD 生成工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - priority-decision-workflow.md：优先级判断工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - product-manager-workflow.md：产品经理总入口工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - product-roadmap-workflow.md：产品路线图工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - product-strategy-workflow.md：产品策略判断工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - requirement-analysis-workflow.md：需求分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - requirement-change-evaluation-workflow.md：需求变更评估工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - requirement-pool-workflow.md：需求池管理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - user-feedback-workflow.md：用户反馈整理工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - user-story-workflow.md：用户故事生成工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - version-planning-workflow.md：版本规划工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - version-retrospective-workflow.md：版本复盘工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
  - researcher
      职责：研究员目录：预留研究相关角色、工作流或模板。
    - README.md：研究员工作流
        职责：说明当前目录的用途、使用方式和注意事项。
  - tester
      职责：按上级目录规则归类的子目录。
    - README.md：测试工程师工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - acceptance-criteria-review-workflow.md：验收标准检查工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - api-integration-test-workflow.md：接口与集成测试工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - automation-test-planning-workflow.md：自动化测试规划工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - compatibility-test-workflow.md：兼容性测试工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - defect-reproduction-workflow.md：缺陷复现工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - exploratory-test-workflow.md：探索式测试工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - non-functional-risk-test-workflow.md：非功能风险测试工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - regression-test-workflow.md：回归测试范围工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - release-acceptance-workflow.md：发布验收工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - test-case-design-workflow.md：测试用例设计工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - test-data-environment-workflow.md：测试数据与环境准备工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - test-execution-report-workflow.md：测试执行报告工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - test-scope-analysis-workflow.md：测试范围分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - test-strategy-planning-workflow.md：测试策略规划工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - tester-workflow.md：测试工程师总入口工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
  - ui-designer
      职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
    - README.md：UI 设计师工作流
        职责：说明当前目录的用途、使用方式和注意事项。
    - accessibility-usability-review-workflow.md：可访问性与可用性检查工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - component-library-planning-workflow.md：组件库规划工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-handoff-workflow.md：设计交接工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-input-analysis-workflow.md：设计输入分析工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-review-workflow.md：设计评审工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-specification-workflow.md：设计规范确认工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-system-audit-workflow.md：设计系统检查工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-to-development-handoff-workflow.md：设计到开发实现约束工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - design-token-workflow.md：设计令牌与平台适配工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - information-architecture-workflow.md：信息架构工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - interaction-optimization-workflow.md：交互体验优化工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - interaction-state-workflow.md：交互状态设计工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - page-type-pattern-workflow.md：页面类型设计模式工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - responsive-adaptation-workflow.md：响应式与多端适配工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - ui-designer-workflow.md：UI 设计总入口工作流
        职责：工作流文件：说明某类任务从输入到输出的处理步骤。
- 05-standards
    职责：标准层：定义什么样的输入、模板、提示词、输出和案例算合格。
  - quality-checklists
      职责：质量检查清单目录：存放通用或角色专属检查清单。
    - common-checklist.md：通用质量检查清单
        职责：通用质量检查清单。
    - developer-checklist.md：开发工程师质量检查清单
        职责：开发工程师任务质量检查清单。
    - product-manager-checklist.md：产品经理质量检查清单
        职责：产品经理任务质量检查清单。
    - role-kit-acceptance-checklist.md：角色能力包验收清单
        职责：检查清单文件：用于快速确认内容是否达标。
    - tester-checklist.md：测试质量检查清单
        职责：检查清单文件：用于快速确认内容是否达标。
    - ui-designer-checklist.md：UI 设计质量检查清单
        职责：UI 设计师任务质量检查清单。
  - README.md：标准目录
      职责：说明当前目录的用途、使用方式和注意事项。
  - agent-orchestration-standard.md：Agent 调度标准
      职责：标准文件：定义某类内容的合格条件。
  - design-token-standard.md：设计令牌标准
      职责：标准文件：定义某类内容的合格条件。
  - example-standard.md：案例标准
      职责：定义优秀案例包结构和进入条件。
  - exported-kit-start-here-standard.md：导出能力包 START-HERE 标准
      职责：标准文件：定义某类内容的合格条件。
  - input-standard.md：输入标准
      职责：定义输入资料必须包含的信息结构。
  - interaction-quality-standard.md：交互质量标准
      职责：标准文件：定义某类内容的合格条件。
  - iteration-memory-standard.md：迭代记忆管理标准
      职责：标准文件：定义某类内容的合格条件。
  - output-standard.md：输出标准
      职责：定义合格 AI 输出和不合格输出的表现。
  - project-governance-standard.md：项目治理标准
      职责：标准文件：定义某类内容的合格条件。
  - project-standard.md：项目标准
      职责：定义 12-projects 下任务项目的标准结构。
  - prompt-standard.md：正式提示词标准
      职责：定义正式提示词必须满足的要求。
  - review-standard.md：评审标准
      职责：定义评审维度和评分建议。
  - role-kit-lifecycle-standard.md：角色能力包生命周期标准
      职责：标准文件：定义某类内容的合格条件。
  - role-standard.md：角色标准
      职责：定义角色文档和 active 角色的要求。
  - template-standard.md：模板标准
      职责：定义可复用模板必须包含的字段和禁止事项。
  - workflow-standard.md：工作流标准
      职责：定义工作流文档必须包含的结构。
- 06-templates
    职责：模板层：沉淀可复用提示词骨架和 meta 模板。
  - common
      职责：通用内容目录：存放跨角色可复用内容。
    - README.md：通用模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - agent-result-report-template.md：子 Agent 结果回报
        职责：模板文件：提供可复用提示词骨架。
    - agent-task-brief-template.md：子 Agent 任务简报
        职责：模板文件：提供可复用提示词骨架。
    - capability-export-template.md：能力导出模板
        职责：模板文件：提供可复用提示词骨架。
    - framework-bootstrap-template.md：框架启动提示词模板
        职责：用于搭建新的 AI 工作流文档框架。
    - general-task-template.md：通用任务提示词模板
        职责：模板文件：提供可复用提示词骨架。
    - iteration-memory-summary-template.md：项目记忆摘要
        职责：模板文件：提供可复用提示词骨架。
    - project-governance-checklist-template.md：项目治理检查清单模板
        职责：模板文件：提供可复用提示词骨架。
  - developer
      职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
    - README.md：开发工程师模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - ai-collaboration-retrospective-template.md：AI 协作复盘报告模板
        职责：模板文件：提供可复用提示词骨架。
    - architecture-decision-record-template.md：ADR 模板
        职责：模板文件：提供可复用提示词骨架。
    - change-risk-assessment-template.md：变更风险评估报告模板
        职责：模板文件：提供可复用提示词骨架。
    - code-review-template.md：代码评审报告模板
        职责：模板文件：提供可复用提示词骨架。
    - data-api-contract-template.md：数据/API/状态契约报告
        职责：模板文件：提供可复用提示词骨架。
    - dependency-and-tech-debt-template.md：依赖与技术债治理报告模板
        职责：模板文件：提供可复用提示词骨架。
    - documentation-sync-template.md：文档同步报告模板
        职责：模板文件：提供可复用提示词骨架。
    - environment-config-governance-template.md：环境与配置治理报告模板
        职责：模板文件：提供可复用提示词骨架。
    - impact-analysis-template.md：影响范围分析报告模板
        职责：模板文件：提供可复用提示词骨架。
    - implementation-template.md：实现交付说明模板
        职责：模板文件：提供可复用提示词骨架。
    - issue-diagnosis-template.md：问题定位报告
        职责：模板文件：提供可复用提示词骨架。
    - minimal-change-governance-template.md：最小必要变更治理模板
        职责：模板文件：提供可复用提示词骨架。
    - module-boundary-analysis-template.md：模块边界分析报告模板
        职责：模板文件：提供可复用提示词骨架。
    - project-bootstrap-template.md：新项目启动治理模板
        职责：模板文件：提供可复用提示词骨架。
    - project-understanding-template.md：项目理解报告模板
        职责：模板文件：提供可复用提示词骨架。
    - release-and-rollback-template.md：发布与回滚治理报告模板
        职责：模板文件：提供可复用提示词骨架。
    - requirement-to-architecture-template.md：架构影响分析报告模板
        职责：模板文件：提供可复用提示词骨架。
    - security-permission-template.md：安全与权限治理报告
        职责：模板文件：提供可复用提示词骨架。
    - testing-verification-template.md：测试与验收报告模板
        职责：模板文件：提供可复用提示词骨架。
    - workflow-orchestration-template.md：开发工作流协同编排记录
        职责：模板文件：提供可复用提示词骨架。
  - marketer
      职责：市场营销目录：预留营销相关角色、工作流或模板。
    - README.md：市场营销模板
        职责：说明当前目录的用途、使用方式和注意事项。
  - meta
      职责：元模板目录：存放用于生成、评审、提取和优化提示词资产的模板。
    - README.md：Meta 模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - example-extractor.md：案例提取器
        职责：用于把高质量任务整理成案例包。
    - explainable-project-runner.md：可解释项目运行助手
        职责：用于让 AI 以可解释方式推进项目，帮助用户理解过程和把控方向。
    - idea-to-input-generator.md：想法转输入生成器
        职责：用于把用户模糊想法整理成标准输入文档。
    - output-reviewer.md：输出评审器
        职责：用于评审 AI 输出质量。
    - project-runner.md：项目运行助手
        职责：用于让 AI 按项目规则推进具体项目，并持续汇报进度和调度角色。
    - prompt-generator.md：正式提示词生成器
        职责：用于从模板和输入资料生成正式提示词。
    - template-generator.md：模板生成器
        职责：用于从原始资料生成可复用模板。
    - template-optimizer.md：模板优化器
        职责：用于根据案例和评审问题优化模板。
  - mixed
      职责：跨角色项目目录：承载不属于单一角色的任务项目。
    - README.md：混合角色模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - team-orchestration-template.md：跨角色团队总调度模板
        职责：模板文件：提供可复用提示词骨架。
  - product-manager
      职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
    - README.md：产品经理模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - acceptance-criteria-template.md：验收标准模板
        职责：模板文件：提供可复用提示词骨架。
    - competitor-analysis-template.md：竞品分析模板
        职责：模板文件：提供可复用提示词骨架。
    - feature-planning-template.md：功能规划模板
        职责：模板文件：提供可复用提示词骨架。
    - prd-template.md：PRD 模板
        职责：模板文件：提供可复用提示词骨架。
    - priority-decision-template.md：优先级判断模板
        职责：模板文件：提供可复用提示词骨架。
    - product-roadmap-template.md：产品路线图模板
        职责：模板文件：提供可复用提示词骨架。
    - product-strategy-template.md：产品策略判断模板
        职责：模板文件：提供可复用提示词骨架。
    - requirement-analysis-template.md：需求分析模板
        职责：模板文件：提供可复用提示词骨架。
    - requirement-change-evaluation-template.md：需求变更评估模板
        职责：模板文件：提供可复用提示词骨架。
    - requirement-pool-template.md：需求池管理模板
        职责：模板文件：提供可复用提示词骨架。
    - user-feedback-template.md：用户反馈整理模板
        职责：模板文件：提供可复用提示词骨架。
    - user-story-template.md：用户故事模板
        职责：模板文件：提供可复用提示词骨架。
    - version-planning-template.md：版本规划模板
        职责：模板文件：提供可复用提示词骨架。
    - version-retrospective-template.md：版本复盘模板
        职责：模板文件：提供可复用提示词骨架。
  - researcher
      职责：研究员目录：预留研究相关角色、工作流或模板。
    - README.md：研究员模板
        职责：说明当前目录的用途、使用方式和注意事项。
  - tester
      职责：按上级目录规则归类的子目录。
    - README.md：测试工程师模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - acceptance-criteria-review-template.md：验收标准检查模板
        职责：模板文件：提供可复用提示词骨架。
    - api-integration-test-template.md：接口与集成测试模板
        职责：模板文件：提供可复用提示词骨架。
    - automation-test-planning-template.md：自动化测试规划模板
        职责：模板文件：提供可复用提示词骨架。
    - compatibility-test-template.md：兼容性测试模板
        职责：模板文件：提供可复用提示词骨架。
    - defect-reproduction-template.md：缺陷复现模板
        职责：模板文件：提供可复用提示词骨架。
    - exploratory-test-template.md：探索式测试模板
        职责：模板文件：提供可复用提示词骨架。
    - non-functional-risk-test-template.md：非功能风险测试模板
        职责：模板文件：提供可复用提示词骨架。
    - regression-test-template.md：回归测试范围模板
        职责：模板文件：提供可复用提示词骨架。
    - release-acceptance-template.md：发布验收模板
        职责：模板文件：提供可复用提示词骨架。
    - test-case-template.md：测试用例模板
        职责：模板文件：提供可复用提示词骨架。
    - test-data-environment-template.md：测试数据与环境准备模板
        职责：模板文件：提供可复用提示词骨架。
    - test-execution-report-template.md：测试执行报告模板
        职责：模板文件：提供可复用提示词骨架。
    - test-plan-template.md：测试计划与用例模板
        职责：模板文件：提供可复用提示词骨架。
    - test-scope-analysis-template.md：测试范围分析模板
        职责：模板文件：提供可复用提示词骨架。
    - test-strategy-planning-template.md：测试策略规划模板
        职责：模板文件：提供可复用提示词骨架。
  - ui-designer
      职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
    - README.md：UI 设计师模板
        职责：说明当前目录的用途、使用方式和注意事项。
    - accessibility-usability-review-template.md：可访问性与可用性检查模板
        职责：模板文件：提供可复用提示词骨架。
    - component-library-planning-template.md：组件库规划模板
        职责：模板文件：提供可复用提示词骨架。
    - design-handoff-template.md：设计交接模板
        职责：模板文件：提供可复用提示词骨架。
    - design-input-analysis-template.md：设计输入分析模板
        职责：模板文件：提供可复用提示词骨架。
    - design-review-template.md：设计评审模板
        职责：模板文件：提供可复用提示词骨架。
    - design-specification-template.md：设计规范确认模板
        职责：模板文件：提供可复用提示词骨架。
    - design-system-audit-template.md：设计系统检查模板
        职责：模板文件：提供可复用提示词骨架。
    - design-to-development-handoff-template.md：设计到开发实现约束模板
        职责：模板文件：提供可复用提示词骨架。
    - design-tokens-template.json
        职责：项目文件。
    - information-architecture-template.md：信息架构模板
        职责：模板文件：提供可复用提示词骨架。
    - interaction-optimization-template.md：交互体验优化方案模板
        职责：模板文件：提供可复用提示词骨架。
    - interaction-state-template.md：交互状态模板
        职责：模板文件：提供可复用提示词骨架。
    - page-type-pattern-template.md：页面类型设计模式模板
        职责：模板文件：提供可复用提示词骨架。
    - platform-adaptation-template.md：平台适配说明模板
        职责：模板文件：提供可复用提示词骨架。
    - responsive-adaptation-template.md：响应式与多端适配模板
        职责：模板文件：提供可复用提示词骨架。
    - ui-brief-template.md：UI Brief 模板
        职责：模板文件：提供可复用提示词骨架。
- 07-prompts
    职责：正式提示词层：保存可直接交给 AI 执行的提示词。
  - active：空目录
      职责：可用状态目录：存放当前推荐使用的内容。
  - deprecated：空目录
      职责：废弃状态目录：存放不再推荐使用但暂时保留的内容。
  - draft：空目录
      职责：草稿状态目录：存放尚未评审的内容。
  - reviewed：空目录
      职责：已评审状态目录：存放已经检查过的内容。
  - README.md：正式提示词
      职责：说明当前目录的用途、使用方式和注意事项。
- 08-outputs
    职责：AI 输出层：保存 AI 生成结果并按状态管理。
  - accepted：空目录
      职责：已采纳状态目录：存放确认可用的输出。
  - draft：空目录
      职责：草稿状态目录：存放尚未评审的内容。
  - rejected：空目录
      职责：不采纳状态目录：存放不采用但保留原因的输出。
  - reviewed：空目录
      职责：已评审状态目录：存放已经检查过的内容。
  - README.md：AI 输出
      职责：说明当前目录的用途、使用方式和注意事项。
- 09-examples
    职责：优秀案例层：保存经过评审且具备复用价值的案例。
  - cross-functional
      职责：跨角色案例目录：存放跨多个角色的优秀案例。
    - workflowproject-framework-bootstrap
        职责：按上级目录规则归类的子目录。
      - README.md：WorkflowProject 框架启动案例
          职责：说明当前目录的用途、使用方式和注意事项。
      - final-prompt.md：正式提示词
          职责：记录本项目使用的正式提示词。
      - input.md：输入材料
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - lessons.md：复盘经验
          职责：记录关键经验、可复用模式、反模式和后续改进。
      - output.md：输出结果
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - progress.md：进度记录
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - review.md：评审结果
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - template.md：使用的模板能力
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - workflow.md：使用的工作流
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - developer：空目录
      职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
  - product-manager：空目录
      职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
  - ui-designer：空目录
      职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
  - README.md：优秀案例
      职责：说明当前目录的用途、使用方式和注意事项。
- 10-knowledge-base
    职责：知识库层：沉淀跨任务的模式、反模式、最佳实践和经验。
  - anti-patterns：空目录
      职责：反模式目录：存放常见错误和应避免做法。
  - best-practices：空目录
      职责：最佳实践目录：存放稳定有效的做法。
  - lessons-learned：空目录
      职责：经验复盘目录：存放跨项目复盘经验。
  - patterns
      职责：成功模式目录：存放可复用成功规律。
    - developer-governance-capability-system.md：developer-kit 开发治理能力体系
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - framework-bootstrap-pattern.md：框架启动模式
        职责：从框架启动案例中提炼出的可复用搭建模式。
    - ponytail-minimal-change-principles.md：Ponytail 最小必要变更原则
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - product-manager-capability-system.md：产品经理能力体系
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - reusable-blocks：空目录
      职责：可复用片段目录：存放可复用提示词片段或文档片段。
  - README.md：知识库
      职责：说明当前目录的用途、使用方式和注意事项。
  - how-to-write-knowledge.md：如何写知识库内容
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
- 11-evaluations
    职责：评估层：保存测试、评分、对比和评估方法。
  - comparison-reports：空目录
      职责：对比报告目录：存放不同提示词或输出的对比结果。
  - evaluation-rubrics
      职责：评分规则目录：存放评估维度和评分规则。
    - common-output-rubric.md：通用输出评分规则
        职责：通用 AI 输出评分规则。
  - output-scorecards
      职责：输出评分目录：存放 AI 输出评分表。
    - README.md：输出评分表
        职责：说明当前目录的用途、使用方式和注意事项。
    - acceptance-criteria-review-scorecard.md：验收标准检查评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - acceptance-criteria-scorecard.md：验收标准评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - accessibility-usability-review-scorecard.md：可访问性与可用性检查评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - agent-orchestration-scorecard.md：Agent 调度验收表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - ai-collaboration-retrospective-scorecard.md：AI 协作复盘评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - api-integration-test-scorecard.md：接口与集成测试评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - architecture-decision-record-scorecard.md：架构决策记录评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - automation-test-planning-scorecard.md：自动化测试规划评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - capability-export-scorecard.md：能力导出评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - change-risk-assessment-scorecard.md：变更风险评估评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - code-review-scorecard.md：代码评审评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - compatibility-test-scorecard.md：兼容性测试评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - competitor-analysis-scorecard.md：竞品分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - component-library-planning-scorecard.md：组件库规划评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - data-api-contract-scorecard.md：数据/API/状态契约评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - defect-reproduction-scorecard.md：缺陷复现评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - dependency-and-tech-debt-scorecard.md：依赖与技术债治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-handoff-scorecard.md：设计交接评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-input-analysis-scorecard.md：设计输入分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-review-scorecard.md：设计评审评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-specification-scorecard.md：设计规范确认评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-system-audit-scorecard.md：设计系统检查评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-to-development-handoff-scorecard.md：设计到开发实现约束评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - design-token-scorecard.md：设计令牌与平台适配评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - documentation-sync-scorecard.md：文档同步评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - environment-config-governance-scorecard.md：环境与配置治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - exploratory-test-scorecard.md：探索式测试评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - feature-planning-scorecard.md：功能规划评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - impact-analysis-scorecard.md：影响范围分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - implementation-scorecard.md：代码实现执行评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - information-architecture-scorecard.md：信息架构评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - interaction-optimization-scorecard.md：交互体验优化评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - interaction-state-scorecard.md：交互状态评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - issue-diagnosis-scorecard.md：问题定位评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - minimal-change-governance-scorecard.md：最小必要变更治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - module-boundary-analysis-scorecard.md：模块边界分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - non-functional-risk-test-scorecard.md：非功能风险测试评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - page-type-pattern-scorecard.md：页面类型设计模式评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - prd-scorecard.md：PRD 评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - priority-decision-scorecard.md：优先级判断评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - product-roadmap-scorecard.md：产品路线图评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - product-strategy-scorecard.md：产品策略判断评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - project-bootstrap-scorecard.md：新项目启动治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - project-completion-scorecard.md：项目完成检查表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - project-understanding-scorecard.md：已有项目理解评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - regression-test-scorecard.md：回归测试评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - release-acceptance-scorecard.md：发布验收评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - release-and-rollback-scorecard.md：发布与回滚治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - requirement-analysis-scorecard.md：需求分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - requirement-change-evaluation-scorecard.md：需求变更评估评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - requirement-pool-scorecard.md：需求池管理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - requirement-to-architecture-scorecard.md：需求到架构影响分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - responsive-adaptation-scorecard.md：响应式与多端适配评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - role-kit-acceptance-scorecard.md：角色能力包验收评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - security-permission-scorecard.md：安全与权限治理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - team-orchestration-scorecard.md：跨角色团队总调度评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - test-case-scorecard.md：测试用例评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - test-data-environment-scorecard.md：测试数据与环境准备评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - test-execution-report-scorecard.md：测试执行报告评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - test-scope-analysis-scorecard.md：测试范围分析评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - test-strategy-planning-scorecard.md：测试策略规划评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - tester-scorecard.md：测试输出评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - testing-verification-scorecard.md：测试与验收评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - ui-design-scorecard.md：UI 设计输出评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - understanding-check-scorecard.md：理解检查表
        职责：用于检查用户是否理解 AI 做了什么、为什么做以及下一步如何判断。
    - user-feedback-scorecard.md：用户反馈整理评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - user-story-scorecard.md：用户故事评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - version-planning-scorecard.md：版本规划评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - version-retrospective-scorecard.md：版本复盘评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - workflow-orchestration-scorecard.md：开发工作流协同编排评分表
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - prompt-tests：空目录
      职责：提示词测试目录：存放提示词测试记录。
  - README.md：评估体系
      职责：说明当前目录的用途、使用方式和注意事项。
- 12-projects
    职责：具体项目执行层：每次真实任务的工作现场。
  - developer
      职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
    - capability-building
        职责：能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。
      - ai-collaboration-retrospective-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - ai-collaboration-retrospective-workflow.md：AI 协作复盘工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：AI 协作复盘工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - architecture-decision-record-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - architecture-decision-record-workflow.md：架构决策记录工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：架构决策记录工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - change-risk-assessment-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - change-risk-assessment-workflow.md：变更风险评估工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：变更风险评估工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - code-review-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - code-review-workflow.md：代码评审工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：代码评审工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - dependency-and-tech-debt-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - dependency-and-tech-debt-workflow.md：依赖与技术债治理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：依赖与技术债治理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - developer-governance-capability-system
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - developer-governance-capability-system.md：developer-kit 开发治理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：开发治理能力体系建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - developer-kit-export-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终执行提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - developer-kit-export-summary.md：developer-kit 导出结果
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：developer-kit 总入口整合与导出项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - documentation-sync-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - documentation-sync-workflow.md：文档同步工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：文档同步工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - environment-config-governance-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - environment-config-governance-workflow.md：环境与配置治理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：环境与配置治理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - impact-analysis-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - impact-analysis-workflow.md：影响范围分析工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：影响范围分析工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - implementation-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - implementation-workflow.md：代码实现执行工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：代码实现执行工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - minimal-change-governance-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - minimal-change-governance-output.md：最小必要变更治理能力输出
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：最小必要变更治理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - module-boundary-analysis-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - module-boundary-analysis-workflow.md：模块边界分析工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：模块边界分析工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - project-bootstrap-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - project-bootstrap-workflow.md：新项目启动治理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：新项目启动治理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - project-understanding-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - project-understanding-workflow.md：已有项目理解工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：已有项目理解工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - release-and-rollback-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - release-and-rollback-workflow.md：发布与回滚治理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：发布与回滚治理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - requirement-to-architecture-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - requirement-to-architecture-workflow.md：需求到架构影响分析工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：需求到架构影响分析工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - testing-verification-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - testing-verification-workflow.md：测试与验收工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：测试与验收工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
  - mixed
      职责：跨角色项目目录：承载不属于单一角色的任务项目。
    - capability-building
        职责：能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。
      - capability-export-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - capability-export-workflow.md：能力导出工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：能力导出工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - team-orchestration-kit-export-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - team-orchestration-kit-export-summary.md：跨角色团队总调度导出包输出
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：跨角色团队总调度导出包建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - team-orchestration-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - output.md：输出
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：跨角色团队总调度工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - workflowproject-framework-refresh
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - framework-refresh-report.md：WorkflowProject 框架刷新报告
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：WorkflowProject 框架刷新项目
            职责：说明当前目录的用途、使用方式和注意事项。
  - product-manager
      职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
    - capability-building
        职责：能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。
      - acceptance-criteria-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - acceptance-criteria-workflow.md：验收标准生成工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：验收标准工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - competitor-analysis-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - competitor-analysis-workflow.md：竞品分析工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：竞品分析工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - feature-planning-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - feature-planning-workflow.md：功能规划工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：功能规划工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - prd-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - prd-generation-workflow.md：PRD 生成工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：PRD 工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - priority-decision-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - priority-decision-workflow.md：优先级判断工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：优先级判断工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - product-manager-capability-system
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：正式提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - product-manager-capability-system.md：产品经理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - next-system-actions.md：后续体系建设建议
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：产品经理能力体系规划项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - product-manager-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：正式提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - product-manager-workflow-v2-output.md：产品经理通用工作流
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - iteration-notes.md：迭代记录
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：产品经理任务总入口项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - product-roadmap-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - product-roadmap-workflow.md：产品路线图工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：产品路线图工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - product-strategy-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - product-strategy-workflow.md：产品策略判断工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：产品策略判断工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - requirement-analysis-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：正式提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - requirement-analysis-workflow.md：需求分析工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - next-actions-after-promotion.md：后续建议
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：需求分析工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - requirement-change-evaluation-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - requirement-change-evaluation-workflow.md：需求变更评估工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：需求变更评估工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - requirement-pool-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - requirement-pool-workflow.md：需求池管理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：需求池管理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - user-feedback-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - user-feedback-workflow.md：用户反馈整理工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：用户反馈整理工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - user-story-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - user-story-workflow.md：用户故事生成工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：用户故事生成工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - version-planning-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - version-planning-workflow.md：版本规划工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：版本规划工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - version-retrospective-workflow
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：最终提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - version-retrospective-workflow.md：版本复盘工作流
              职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：版本复盘工作流建设项目
            职责：说明当前目录的用途、使用方式和注意事项。
    - real-cases
        职责：真实使用项目目录：承载使用已有能力处理具体业务需求的项目。
      - ai-template-tool-prd
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始输入
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - feature-list.md：功能清单
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - information-architecture.md：信息架构
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd-readiness.md：PRD 就绪判断
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd-scope.md：PRD 范围
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd-user-scenarios.md：用户角色和场景
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 03-prompts：空目录
            职责：项目提示词目录：存放本项目正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - acceptance-criteria.md：验收标准
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - feature-spec.md：功能说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd.md：PRD
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - prd-review.md：PRD 评审
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - validation-notes.md：验证记录
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：AI 提示词模板工具 PRD 项目
            职责：说明当前目录的用途、使用方式和注意事项。
      - ai-template-tool-requirement-analysis
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - requirement-analysis.md：需求分析
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - review-gap-resolution.md：评审扣分点解决方案
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 03-prompts：空目录
            职责：项目提示词目录：存放本项目正式提示词。
        - 04-outputs：空目录
            职责：项目输出目录：存放本项目 AI 输出结果。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：需求分析评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - validation-notes.md：验证记录
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：AI 提示词模板工具需求分析项目
            职责：说明当前目录的用途、使用方式和注意事项。
  - project-template
      职责：项目模板目录：新项目优先复制这个骨架。
    - 00-progress
        职责：按上级目录规则归类的子目录。
      - decision-log.md：决策记录
          职责：记录项目执行过程中的重要决策和原因。
      - memory-summary.md：项目记忆摘要
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - next-actions.md：下一步判断
          职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
      - progress-log.md：进度记录
          职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
    - 01-inputs：空目录
        职责：项目输入目录：存放本项目原始材料。
    - 02-analysis：空目录
        职责：项目分析目录：存放输入分析和需求整理结果。
    - 03-prompts：空目录
        职责：项目提示词目录：存放本项目正式提示词。
    - 04-outputs：空目录
        职责：项目输出目录：存放本项目 AI 输出结果。
    - 05-review：空目录
        职责：项目评审目录：存放输出评审和评分记录。
    - 06-lessons：空目录
        职责：项目复盘目录：存放经验、反模式和沉淀建议。
    - README.md：项目模板
        职责：说明当前目录的用途、使用方式和注意事项。
  - tester
      职责：按上级目录规则归类的子目录。
    - capability-building
        职责：能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。
      - tester-kit-bootstrap
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：正式提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - output.md：输出
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：测试工程师能力包启动项目
            职责：说明当前目录的用途、使用方式和注意事项。
  - ui-designer
      职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
    - capability-building
        职责：能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。
      - ui-designer-kit-bootstrap
          职责：按上级目录规则归类的子目录。
        - 00-progress
            职责：按上级目录规则归类的子目录。
          - decision-log.md：决策记录
              职责：记录项目执行过程中的重要决策和原因。
          - memory-summary.md：项目记忆摘要
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - next-actions.md：下一步判断
              职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
          - progress-log.md：进度记录
              职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
        - 01-inputs
            职责：项目输入目录：存放本项目原始材料。
          - original-requirement.md：原始需求
              职责：记录项目原始需求和逐步明确的需求。
        - 02-analysis
            职责：项目分析目录：存放输入分析和需求整理结果。
          - input-analysis.md：输入分析
              职责：记录输入分析、任务类型、核心问题和关键决策。
        - 03-prompts
            职责：项目提示词目录：存放本项目正式提示词。
          - final-prompt.md：正式提示词
              职责：记录本项目使用的正式提示词。
        - 04-outputs
            职责：项目输出目录：存放本项目 AI 输出结果。
          - output.md：输出
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - 05-review
            职责：项目评审目录：存放输出评审和评分记录。
          - output-review.md：输出评审
              职责：记录输出质量评审、评分和建议。
        - 06-lessons
            职责：项目复盘目录：存放经验、反模式和沉淀建议。
          - promotion-notes.md：沉淀记录
              职责：记录哪些内容已提升到全局，哪些暂不提升。
        - README.md：UI 设计能力包启动项目
            职责：说明当前目录的用途、使用方式和注意事项。
  - README.md：项目
      职责：说明当前目录的用途、使用方式和注意事项。
  - asset-index.md：可用资产索引
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - current-focus.md：当前工作区
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - project-index.md：项目索引
      职责：自动生成的项目总览：列出每个项目的目标、状态、路径、下一步和启动方式。
- 13-visual-maps
    职责：可视化导图层：统一保存 XMind 导图和 Markdown 大纲。
  - README.md：可视化导图
      职责：说明当前目录的用途、使用方式和注意事项。
  - WorkflowProject-file-responsibility-outline.md：WorkflowProject 当前文件与职责（自动扫描）
      职责：导图大纲文件：用于快速预览 XMind 内容。
  - WorkflowProject-mindmap-outline.md：WorkflowProject AI 工作流文档工程框架
      职责：导图大纲文件：用于快速预览 XMind 内容。
  - WorkflowProject-operation-flow-outline.md：从材料到输出的 AI 协作操作流程
      职责：导图大纲文件：用于快速预览 XMind 内容。
- 14-exports
    职责：项目目录。
  - .ai
      职责：按上级目录规则归类的子目录。
    - kits
        职责：按上级目录规则归类的子目录。
      - developer-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - README.md：示例区
              职责：说明当前目录的用途、使用方式和注意事项。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - developer-governance-capability-system.md：developer-kit 开发治理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - ponytail-minimal-change-principles.md：Ponytail 最小必要变更原则
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - minimal-change-guardian.md：最小必要变更守门人
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - role-definition.md：开发工程师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - ai-collaboration-retrospective-scorecard.md：AI 协作复盘评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - architecture-decision-record-scorecard.md：架构决策记录评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - change-risk-assessment-scorecard.md：变更风险评估评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - code-review-scorecard.md：代码评审评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - data-api-contract-scorecard.md：数据/API/状态契约评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - dependency-and-tech-debt-scorecard.md：依赖与技术债治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - documentation-sync-scorecard.md：文档同步评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - environment-config-governance-scorecard.md：环境与配置治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - impact-analysis-scorecard.md：影响范围分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - implementation-scorecard.md：代码实现执行评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - issue-diagnosis-scorecard.md：问题定位评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - minimal-change-governance-scorecard.md：最小必要变更治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - module-boundary-analysis-scorecard.md：模块边界分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - project-bootstrap-scorecard.md：新项目启动治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - project-understanding-scorecard.md：已有项目理解评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - release-and-rollback-scorecard.md：发布与回滚治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-to-architecture-scorecard.md：需求到架构影响分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - security-permission-scorecard.md：安全与权限治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - testing-verification-scorecard.md：测试与验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - workflow-orchestration-scorecard.md：开发工作流协同编排评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - developer
              职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
            - README.md：开发工程师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - ai-collaboration-retrospective-template.md：AI 协作复盘报告模板
                职责：模板文件：提供可复用提示词骨架。
            - architecture-decision-record-template.md：ADR 模板
                职责：模板文件：提供可复用提示词骨架。
            - change-risk-assessment-template.md：变更风险评估报告模板
                职责：模板文件：提供可复用提示词骨架。
            - code-review-template.md：代码评审报告模板
                职责：模板文件：提供可复用提示词骨架。
            - data-api-contract-template.md：数据/API/状态契约报告
                职责：模板文件：提供可复用提示词骨架。
            - dependency-and-tech-debt-template.md：依赖与技术债治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - documentation-sync-template.md：文档同步报告模板
                职责：模板文件：提供可复用提示词骨架。
            - environment-config-governance-template.md：环境与配置治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - impact-analysis-template.md：影响范围分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - implementation-template.md：实现交付说明模板
                职责：模板文件：提供可复用提示词骨架。
            - issue-diagnosis-template.md：问题定位报告
                职责：模板文件：提供可复用提示词骨架。
            - minimal-change-governance-template.md：最小必要变更治理模板
                职责：模板文件：提供可复用提示词骨架。
            - module-boundary-analysis-template.md：模块边界分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - project-bootstrap-template.md：新项目启动治理模板
                职责：模板文件：提供可复用提示词骨架。
            - project-understanding-template.md：项目理解报告模板
                职责：模板文件：提供可复用提示词骨架。
            - release-and-rollback-template.md：发布与回滚治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-to-architecture-template.md：架构影响分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - security-permission-template.md：安全与权限治理报告
                职责：模板文件：提供可复用提示词骨架。
            - testing-verification-template.md：测试与验收报告模板
                职责：模板文件：提供可复用提示词骨架。
            - workflow-orchestration-template.md：开发工作流协同编排记录
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - developer
              职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
            - README.md：开发工程师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - ai-collaboration-retrospective-workflow.md：AI 协作复盘工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - architecture-decision-record-workflow.md：架构决策记录工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - change-risk-assessment-workflow.md：变更风险评估工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - code-review-workflow.md：代码评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - data-api-contract-workflow.md：数据/API/状态契约工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - dependency-and-tech-debt-workflow.md：依赖与技术债治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - developer-kit-workflow.md：开发治理总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - documentation-sync-workflow.md：文档同步工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - environment-config-governance-workflow.md：环境与配置治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - impact-analysis-workflow.md：影响范围分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - implementation-workflow.md：代码实现执行工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - issue-diagnosis-workflow.md：问题定位工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - minimal-change-governance-workflow.md：最小必要变更治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - module-boundary-analysis-workflow.md：模块边界分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - project-bootstrap-workflow.md：新项目启动治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - project-understanding-workflow.md：已有项目理解工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - release-and-rollback-workflow.md：发布与回滚治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-to-architecture-workflow.md：需求到架构影响分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - security-permission-workflow.md：安全与权限治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - testing-verification-workflow.md：测试与验收工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - workflow-orchestration-guide.md：开发工作流协同编排指南
                职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：developer-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：developer-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - product-manager-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - README.md：示例说明
              职责：说明当前目录的用途、使用方式和注意事项。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - product-manager-capability-system.md：产品经理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：产品经理角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - acceptance-criteria-scorecard.md：验收标准评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - competitor-analysis-scorecard.md：竞品分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - feature-planning-scorecard.md：功能规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd-scorecard.md：PRD 评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - priority-decision-scorecard.md：优先级判断评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - product-roadmap-scorecard.md：产品路线图评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - product-strategy-scorecard.md：产品策略判断评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-analysis-scorecard.md：需求分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-change-evaluation-scorecard.md：需求变更评估评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-pool-scorecard.md：需求池管理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - user-feedback-scorecard.md：用户反馈整理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - user-story-scorecard.md：用户故事评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - version-planning-scorecard.md：版本规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - version-retrospective-scorecard.md：版本复盘评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - meta
              职责：元模板目录：存放用于生成、评审、提取和优化提示词资产的模板。
            - idea-to-input-generator.md：想法转输入生成器
                职责：用于把用户模糊想法整理成标准输入文档。
            - output-reviewer.md：输出评审器
                职责：用于评审 AI 输出质量。
          - product-manager
              职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
            - README.md：产品经理模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-template.md：验收标准模板
                职责：模板文件：提供可复用提示词骨架。
            - competitor-analysis-template.md：竞品分析模板
                职责：模板文件：提供可复用提示词骨架。
            - feature-planning-template.md：功能规划模板
                职责：模板文件：提供可复用提示词骨架。
            - prd-template.md：PRD 模板
                职责：模板文件：提供可复用提示词骨架。
            - priority-decision-template.md：优先级判断模板
                职责：模板文件：提供可复用提示词骨架。
            - product-roadmap-template.md：产品路线图模板
                职责：模板文件：提供可复用提示词骨架。
            - product-strategy-template.md：产品策略判断模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-analysis-template.md：需求分析模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-change-evaluation-template.md：需求变更评估模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-pool-template.md：需求池管理模板
                职责：模板文件：提供可复用提示词骨架。
            - user-feedback-template.md：用户反馈整理模板
                职责：模板文件：提供可复用提示词骨架。
            - user-story-template.md：用户故事模板
                职责：模板文件：提供可复用提示词骨架。
            - version-planning-template.md：版本规划模板
                职责：模板文件：提供可复用提示词骨架。
            - version-retrospective-template.md：版本复盘模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - idea-to-input-workflow.md：想法转输入工作流
                职责：用于把用户口头描述、模糊想法或零散需求整理成标准输入。
            - input-analysis-workflow.md：输入分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - output-review-workflow.md：输出评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - product-manager
              职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
            - README.md：产品经理工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-workflow.md：验收标准生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - competitor-analysis-workflow.md：竞品分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - feature-planning-workflow.md：功能规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - prd-generation-workflow.md：PRD 生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - priority-decision-workflow.md：优先级判断工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-manager-workflow.md：产品经理总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-roadmap-workflow.md：产品路线图工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-strategy-workflow.md：产品策略判断工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-analysis-workflow.md：需求分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-change-evaluation-workflow.md：需求变更评估工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-pool-workflow.md：需求池管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - user-feedback-workflow.md：用户反馈整理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - user-story-workflow.md：用户故事生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - version-planning-workflow.md：版本规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - version-retrospective-workflow.md：版本复盘工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：产品经理能力包
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：product-manager-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - project-governance-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - project-governance-standard.md：项目治理标准
              职责：标准文件：定义某类内容的合格条件。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - project-governance-checklist-template.md：项目治理检查清单
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - project-governance-workflow.md：项目治理与开发前置工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：project-governance-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：project-governance-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - team-orchestration-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - role-kit-lifecycle-standard.md：角色能力包生命周期标准
              职责：标准文件：定义某类内容的合格条件。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - team-orchestration-scorecard.md：跨角色团队总调度评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - mixed
              职责：跨角色项目目录：承载不属于单一角色的任务项目。
            - README.md：混合角色模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - team-orchestration-template.md：跨角色团队总调度模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - mixed
              职责：跨角色项目目录：承载不属于单一角色的任务项目。
            - README.md：混合角色工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - team-orchestration-workflow.md：跨角色团队总调度工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：安装说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：team-orchestration-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：team-orchestration-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - tester-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：tester-kit 快速示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：测试工程师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - acceptance-criteria-review-scorecard.md：验收标准检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - api-integration-test-scorecard.md：接口与集成测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - automation-test-planning-scorecard.md：自动化测试规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - compatibility-test-scorecard.md：兼容性测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - defect-reproduction-scorecard.md：缺陷复现评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - exploratory-test-scorecard.md：探索式测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - non-functional-risk-test-scorecard.md：非功能风险测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - regression-test-scorecard.md：回归测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - release-acceptance-scorecard.md：发布验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-case-scorecard.md：测试用例评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-data-environment-scorecard.md：测试数据与环境准备评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-execution-report-scorecard.md：测试执行报告评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-scope-analysis-scorecard.md：测试范围分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-strategy-planning-scorecard.md：测试策略规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - tester-scorecard.md：测试输出评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - testing-verification-scorecard.md：测试与验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - quality-checklists
              职责：质量检查清单目录：存放通用或角色专属检查清单。
            - tester-checklist.md：测试质量检查清单
                职责：检查清单文件：用于快速确认内容是否达标。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - tester
              职责：按上级目录规则归类的子目录。
            - README.md：测试工程师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-review-template.md：验收标准检查模板
                职责：模板文件：提供可复用提示词骨架。
            - api-integration-test-template.md：接口与集成测试模板
                职责：模板文件：提供可复用提示词骨架。
            - automation-test-planning-template.md：自动化测试规划模板
                职责：模板文件：提供可复用提示词骨架。
            - compatibility-test-template.md：兼容性测试模板
                职责：模板文件：提供可复用提示词骨架。
            - defect-reproduction-template.md：缺陷复现模板
                职责：模板文件：提供可复用提示词骨架。
            - exploratory-test-template.md：探索式测试模板
                职责：模板文件：提供可复用提示词骨架。
            - non-functional-risk-test-template.md：非功能风险测试模板
                职责：模板文件：提供可复用提示词骨架。
            - regression-test-template.md：回归测试范围模板
                职责：模板文件：提供可复用提示词骨架。
            - release-acceptance-template.md：发布验收模板
                职责：模板文件：提供可复用提示词骨架。
            - test-case-template.md：测试用例模板
                职责：模板文件：提供可复用提示词骨架。
            - test-data-environment-template.md：测试数据与环境准备模板
                职责：模板文件：提供可复用提示词骨架。
            - test-execution-report-template.md：测试执行报告模板
                职责：模板文件：提供可复用提示词骨架。
            - test-plan-template.md：测试计划与用例模板
                职责：模板文件：提供可复用提示词骨架。
            - test-scope-analysis-template.md：测试范围分析模板
                职责：模板文件：提供可复用提示词骨架。
            - test-strategy-planning-template.md：测试策略规划模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - tester
              职责：按上级目录规则归类的子目录。
            - README.md：测试工程师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-review-workflow.md：验收标准检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - api-integration-test-workflow.md：接口与集成测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - automation-test-planning-workflow.md：自动化测试规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - compatibility-test-workflow.md：兼容性测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - defect-reproduction-workflow.md：缺陷复现工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - exploratory-test-workflow.md：探索式测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - non-functional-risk-test-workflow.md：非功能风险测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - regression-test-workflow.md：回归测试范围工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - release-acceptance-workflow.md：发布验收工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-case-design-workflow.md：测试用例设计工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-data-environment-workflow.md：测试数据与环境准备工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-execution-report-workflow.md：测试执行报告工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-scope-analysis-workflow.md：测试范围分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-strategy-planning-workflow.md：测试策略规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - tester-workflow.md：测试工程师总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：tester-kit 接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：tester-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：tester-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：tester-kit 来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：tester-kit 使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - ui-designer-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：ui-designer-kit 快速示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：UI 设计师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - accessibility-usability-review-scorecard.md：可访问性与可用性检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - component-library-planning-scorecard.md：组件库规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-handoff-scorecard.md：设计交接评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-input-analysis-scorecard.md：设计输入分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-review-scorecard.md：设计评审评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-specification-scorecard.md：设计规范确认评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-system-audit-scorecard.md：设计系统检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-to-development-handoff-scorecard.md：设计到开发实现约束评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - information-architecture-scorecard.md：信息架构评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - interaction-state-scorecard.md：交互状态评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - page-type-pattern-scorecard.md：页面类型设计模式评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - responsive-adaptation-scorecard.md：响应式与多端适配评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - ui-design-scorecard.md：UI 设计输出评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - quality-checklists
              职责：质量检查清单目录：存放通用或角色专属检查清单。
            - ui-designer-checklist.md：UI 设计质量检查清单
                职责：UI 设计师任务质量检查清单。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - ui-designer
              职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
            - README.md：UI 设计师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - accessibility-usability-review-template.md：可访问性与可用性检查模板
                职责：模板文件：提供可复用提示词骨架。
            - component-library-planning-template.md：组件库规划模板
                职责：模板文件：提供可复用提示词骨架。
            - design-handoff-template.md：设计交接模板
                职责：模板文件：提供可复用提示词骨架。
            - design-input-analysis-template.md：设计输入分析模板
                职责：模板文件：提供可复用提示词骨架。
            - design-review-template.md：设计评审模板
                职责：模板文件：提供可复用提示词骨架。
            - design-specification-template.md：设计规范确认模板
                职责：模板文件：提供可复用提示词骨架。
            - design-system-audit-template.md：设计系统检查模板
                职责：模板文件：提供可复用提示词骨架。
            - design-to-development-handoff-template.md：设计到开发实现约束模板
                职责：模板文件：提供可复用提示词骨架。
            - information-architecture-template.md：信息架构模板
                职责：模板文件：提供可复用提示词骨架。
            - interaction-state-template.md：交互状态模板
                职责：模板文件：提供可复用提示词骨架。
            - page-type-pattern-template.md：页面类型设计模式模板
                职责：模板文件：提供可复用提示词骨架。
            - responsive-adaptation-template.md：响应式与多端适配模板
                职责：模板文件：提供可复用提示词骨架。
            - ui-brief-template.md：UI Brief 模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - ui-designer
              职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
            - README.md：UI 设计师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - accessibility-usability-review-workflow.md：可访问性与可用性检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - component-library-planning-workflow.md：组件库规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-handoff-workflow.md：设计交接工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-input-analysis-workflow.md：设计输入分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-review-workflow.md：设计评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-specification-workflow.md：设计规范确认工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-system-audit-workflow.md：设计系统检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-to-development-handoff-workflow.md：设计到开发实现约束工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - information-architecture-workflow.md：信息架构工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - interaction-state-workflow.md：交互状态设计工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - page-type-pattern-workflow.md：页面类型设计模式工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - responsive-adaptation-workflow.md：响应式与多端适配工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - ui-designer-workflow.md：UI 设计总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：ui-designer-kit 接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：ui-designer-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：ui-designer-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：ui-designer-kit 来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：ui-designer-kit 使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - .cursor
      职责：按上级目录规则归类的子目录。
    - rules
        职责：按上级目录规则归类的子目录。
      - workflowproject-governance.mdc
          职责：项目文件。
  - developer-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - README.md：示例区
          职责：说明当前目录的用途、使用方式和注意事项。
      - quick-start-example.md：快速启动示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - knowledge
        职责：按上级目录规则归类的子目录。
      - developer-governance-capability-system.md：developer-kit 开发治理能力体系
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - ponytail-minimal-change-principles.md：Ponytail 最小必要变更原则
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - roles
        职责：按上级目录规则归类的子目录。
      - minimal-change-guardian.md：最小必要变更守门人
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - role-definition.md：开发工程师角色定义
          职责：定义该角色的职责、常见输入和常见输出。
    - scorecards
        职责：按上级目录规则归类的子目录。
      - ai-collaboration-retrospective-scorecard.md：AI 协作复盘评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - architecture-decision-record-scorecard.md：架构决策记录评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - change-risk-assessment-scorecard.md：变更风险评估评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - code-review-scorecard.md：代码评审评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - data-api-contract-scorecard.md：数据/API/状态契约评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - dependency-and-tech-debt-scorecard.md：依赖与技术债治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - documentation-sync-scorecard.md：文档同步评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - environment-config-governance-scorecard.md：环境与配置治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - impact-analysis-scorecard.md：影响范围分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - implementation-scorecard.md：代码实现执行评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - issue-diagnosis-scorecard.md：问题定位评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - minimal-change-governance-scorecard.md：最小必要变更治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - module-boundary-analysis-scorecard.md：模块边界分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - project-bootstrap-scorecard.md：新项目启动治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - project-understanding-scorecard.md：已有项目理解评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - release-and-rollback-scorecard.md：发布与回滚治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - requirement-to-architecture-scorecard.md：需求到架构影响分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - security-permission-scorecard.md：安全与权限治理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - testing-verification-scorecard.md：测试与验收评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - workflow-orchestration-scorecard.md：开发工作流协同编排评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-summary-template.md：项目记忆摘要
            职责：模板文件：提供可复用提示词骨架。
      - developer
          职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
        - README.md：开发工程师模板
            职责：说明当前目录的用途、使用方式和注意事项。
        - ai-collaboration-retrospective-template.md：AI 协作复盘报告模板
            职责：模板文件：提供可复用提示词骨架。
        - architecture-decision-record-template.md：ADR 模板
            职责：模板文件：提供可复用提示词骨架。
        - change-risk-assessment-template.md：变更风险评估报告模板
            职责：模板文件：提供可复用提示词骨架。
        - code-review-template.md：代码评审报告模板
            职责：模板文件：提供可复用提示词骨架。
        - data-api-contract-template.md：数据/API/状态契约报告
            职责：模板文件：提供可复用提示词骨架。
        - dependency-and-tech-debt-template.md：依赖与技术债治理报告模板
            职责：模板文件：提供可复用提示词骨架。
        - documentation-sync-template.md：文档同步报告模板
            职责：模板文件：提供可复用提示词骨架。
        - environment-config-governance-template.md：环境与配置治理报告模板
            职责：模板文件：提供可复用提示词骨架。
        - impact-analysis-template.md：影响范围分析报告模板
            职责：模板文件：提供可复用提示词骨架。
        - implementation-template.md：实现交付说明模板
            职责：模板文件：提供可复用提示词骨架。
        - issue-diagnosis-template.md：问题定位报告
            职责：模板文件：提供可复用提示词骨架。
        - minimal-change-governance-template.md：最小必要变更治理模板
            职责：模板文件：提供可复用提示词骨架。
        - module-boundary-analysis-template.md：模块边界分析报告模板
            职责：模板文件：提供可复用提示词骨架。
        - project-bootstrap-template.md：新项目启动治理模板
            职责：模板文件：提供可复用提示词骨架。
        - project-understanding-template.md：项目理解报告模板
            职责：模板文件：提供可复用提示词骨架。
        - release-and-rollback-template.md：发布与回滚治理报告模板
            职责：模板文件：提供可复用提示词骨架。
        - requirement-to-architecture-template.md：架构影响分析报告模板
            职责：模板文件：提供可复用提示词骨架。
        - security-permission-template.md：安全与权限治理报告
            职责：模板文件：提供可复用提示词骨架。
        - testing-verification-template.md：测试与验收报告模板
            职责：模板文件：提供可复用提示词骨架。
        - workflow-orchestration-template.md：开发工作流协同编排记录
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-management-workflow.md：迭代记忆管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
      - developer
          职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
        - README.md：开发工程师工作流
            职责：说明当前目录的用途、使用方式和注意事项。
        - ai-collaboration-retrospective-workflow.md：AI 协作复盘工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - architecture-decision-record-workflow.md：架构决策记录工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - change-risk-assessment-workflow.md：变更风险评估工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - code-review-workflow.md：代码评审工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - data-api-contract-workflow.md：数据/API/状态契约工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - dependency-and-tech-debt-workflow.md：依赖与技术债治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - developer-kit-workflow.md：开发治理总入口工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - documentation-sync-workflow.md：文档同步工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - environment-config-governance-workflow.md：环境与配置治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - impact-analysis-workflow.md：影响范围分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - implementation-workflow.md：代码实现执行工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - issue-diagnosis-workflow.md：问题定位工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - minimal-change-governance-workflow.md：最小必要变更治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - module-boundary-analysis-workflow.md：模块边界分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - project-bootstrap-workflow.md：新项目启动治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - project-understanding-workflow.md：已有项目理解工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - release-and-rollback-workflow.md：发布与回滚治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - requirement-to-architecture-workflow.md：需求到架构影响分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - security-permission-workflow.md：安全与权限治理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - testing-verification-workflow.md：测试与验收工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - workflow-orchestration-guide.md：开发工作流协同编排指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - INSTALL.md：接入说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：developer-kit
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：developer-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - product-manager-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - README.md：示例说明
          职责：说明当前目录的用途、使用方式和注意事项。
      - quick-start-example.md：快速启动示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - knowledge
        职责：按上级目录规则归类的子目录。
      - product-manager-capability-system.md：产品经理能力体系
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - roles
        职责：按上级目录规则归类的子目录。
      - role-definition.md：产品经理角色定义
          职责：定义该角色的职责、常见输入和常见输出。
    - scorecards
        职责：按上级目录规则归类的子目录。
      - acceptance-criteria-scorecard.md：验收标准评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - competitor-analysis-scorecard.md：竞品分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - feature-planning-scorecard.md：功能规划评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - prd-scorecard.md：PRD 评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - priority-decision-scorecard.md：优先级判断评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - product-roadmap-scorecard.md：产品路线图评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - product-strategy-scorecard.md：产品策略判断评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - requirement-analysis-scorecard.md：需求分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - requirement-change-evaluation-scorecard.md：需求变更评估评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - requirement-pool-scorecard.md：需求池管理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - user-feedback-scorecard.md：用户反馈整理评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - user-story-scorecard.md：用户故事评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - version-planning-scorecard.md：版本规划评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - version-retrospective-scorecard.md：版本复盘评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-summary-template.md：项目记忆摘要
            职责：模板文件：提供可复用提示词骨架。
      - meta
          职责：元模板目录：存放用于生成、评审、提取和优化提示词资产的模板。
        - idea-to-input-generator.md：想法转输入生成器
            职责：用于把用户模糊想法整理成标准输入文档。
        - output-reviewer.md：输出评审器
            职责：用于评审 AI 输出质量。
      - product-manager
          职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
        - README.md：产品经理模板
            职责：说明当前目录的用途、使用方式和注意事项。
        - acceptance-criteria-template.md：验收标准模板
            职责：模板文件：提供可复用提示词骨架。
        - competitor-analysis-template.md：竞品分析模板
            职责：模板文件：提供可复用提示词骨架。
        - feature-planning-template.md：功能规划模板
            职责：模板文件：提供可复用提示词骨架。
        - prd-template.md：PRD 模板
            职责：模板文件：提供可复用提示词骨架。
        - priority-decision-template.md：优先级判断模板
            职责：模板文件：提供可复用提示词骨架。
        - product-roadmap-template.md：产品路线图模板
            职责：模板文件：提供可复用提示词骨架。
        - product-strategy-template.md：产品策略判断模板
            职责：模板文件：提供可复用提示词骨架。
        - requirement-analysis-template.md：需求分析模板
            职责：模板文件：提供可复用提示词骨架。
        - requirement-change-evaluation-template.md：需求变更评估模板
            职责：模板文件：提供可复用提示词骨架。
        - requirement-pool-template.md：需求池管理模板
            职责：模板文件：提供可复用提示词骨架。
        - user-feedback-template.md：用户反馈整理模板
            职责：模板文件：提供可复用提示词骨架。
        - user-story-template.md：用户故事模板
            职责：模板文件：提供可复用提示词骨架。
        - version-planning-template.md：版本规划模板
            职责：模板文件：提供可复用提示词骨架。
        - version-retrospective-template.md：版本复盘模板
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - idea-to-input-workflow.md：想法转输入工作流
            职责：用于把用户口头描述、模糊想法或零散需求整理成标准输入。
        - input-analysis-workflow.md：输入分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - iteration-memory-management-workflow.md：迭代记忆管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - output-review-workflow.md：输出评审工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
      - product-manager
          职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
        - README.md：产品经理工作流
            职责：说明当前目录的用途、使用方式和注意事项。
        - acceptance-criteria-workflow.md：验收标准生成工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - competitor-analysis-workflow.md：竞品分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - feature-planning-workflow.md：功能规划工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - prd-generation-workflow.md：PRD 生成工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - priority-decision-workflow.md：优先级判断工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - product-manager-workflow.md：产品经理总入口工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - product-roadmap-workflow.md：产品路线图工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - product-strategy-workflow.md：产品策略判断工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - requirement-analysis-workflow.md：需求分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - requirement-change-evaluation-workflow.md：需求变更评估工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - requirement-pool-workflow.md：需求池管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - user-feedback-workflow.md：用户反馈整理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - user-story-workflow.md：用户故事生成工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - version-planning-workflow.md：版本规划工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - version-retrospective-workflow.md：版本复盘工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - INSTALL.md：接入说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：产品经理能力包
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：product-manager-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - project-governance-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - quick-start-example.md：快速启动示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - standards
        职责：按上级目录规则归类的子目录。
      - project-governance-standard.md：项目治理标准
          职责：标准文件：定义某类内容的合格条件。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - project-governance-checklist-template.md：项目治理检查清单模板
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - project-governance-workflow.md：项目治理与开发前置工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - INSTALL.md：接入说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：project-governance-kit
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：project-governance-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - team-orchestration-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - quick-start-example.md：快速启动示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - knowledge
        职责：按上级目录规则归类的子目录。
      - agent-orchestration-standard.md：Agent 调度标准
          职责：标准文件：定义某类内容的合格条件。
      - role-kit-lifecycle-standard.md：角色能力包生命周期标准
          职责：标准文件：定义某类内容的合格条件。
    - scorecards
        职责：按上级目录规则归类的子目录。
      - team-orchestration-scorecard.md：跨角色团队总调度评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - agent-result-report-template.md：子 Agent 结果回报
            职责：模板文件：提供可复用提示词骨架。
        - agent-task-brief-template.md：子 Agent 任务简报
            职责：模板文件：提供可复用提示词骨架。
        - iteration-memory-summary-template.md：项目记忆摘要
            职责：模板文件：提供可复用提示词骨架。
      - mixed
          职责：跨角色项目目录：承载不属于单一角色的任务项目。
        - README.md：混合角色模板
            职责：说明当前目录的用途、使用方式和注意事项。
        - team-orchestration-template.md：跨角色团队总调度模板
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - agent-orchestration-workflow.md：Agent 调度工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - iteration-memory-management-workflow.md：迭代记忆管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
      - mixed
          职责：跨角色项目目录：承载不属于单一角色的任务项目。
        - README.md：混合角色工作流
            职责：说明当前目录的用途、使用方式和注意事项。
        - team-orchestration-workflow.md：跨角色团队总调度工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - INSTALL.md：安装说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：team-orchestration-kit
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：team-orchestration-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - tester-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - quick-start-example.md：tester-kit 快速示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - roles
        职责：按上级目录规则归类的子目录。
      - role-definition.md：测试工程师角色定义
          职责：定义该角色的职责、常见输入和常见输出。
    - scorecards
        职责：按上级目录规则归类的子目录。
      - acceptance-criteria-review-scorecard.md：验收标准检查评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - api-integration-test-scorecard.md：接口与集成测试评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - automation-test-planning-scorecard.md：自动化测试规划评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - compatibility-test-scorecard.md：兼容性测试评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - defect-reproduction-scorecard.md：缺陷复现评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - exploratory-test-scorecard.md：探索式测试评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - non-functional-risk-test-scorecard.md：非功能风险测试评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - regression-test-scorecard.md：回归测试评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - release-acceptance-scorecard.md：发布验收评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - test-case-scorecard.md：测试用例评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - test-data-environment-scorecard.md：测试数据与环境准备评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - test-execution-report-scorecard.md：测试执行报告评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - test-scope-analysis-scorecard.md：测试范围分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - test-strategy-planning-scorecard.md：测试策略规划评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - tester-scorecard.md：测试输出评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - testing-verification-scorecard.md：测试与验收评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - standards
        职责：按上级目录规则归类的子目录。
      - quality-checklists
          职责：质量检查清单目录：存放通用或角色专属检查清单。
        - tester-checklist.md：测试质量检查清单
            职责：检查清单文件：用于快速确认内容是否达标。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-summary-template.md：项目记忆摘要
            职责：模板文件：提供可复用提示词骨架。
      - tester
          职责：按上级目录规则归类的子目录。
        - README.md：测试工程师模板
            职责：说明当前目录的用途、使用方式和注意事项。
        - acceptance-criteria-review-template.md：验收标准检查模板
            职责：模板文件：提供可复用提示词骨架。
        - api-integration-test-template.md：接口与集成测试模板
            职责：模板文件：提供可复用提示词骨架。
        - automation-test-planning-template.md：自动化测试规划模板
            职责：模板文件：提供可复用提示词骨架。
        - compatibility-test-template.md：兼容性测试模板
            职责：模板文件：提供可复用提示词骨架。
        - defect-reproduction-template.md：缺陷复现模板
            职责：模板文件：提供可复用提示词骨架。
        - exploratory-test-template.md：探索式测试模板
            职责：模板文件：提供可复用提示词骨架。
        - non-functional-risk-test-template.md：非功能风险测试模板
            职责：模板文件：提供可复用提示词骨架。
        - regression-test-template.md：回归测试范围模板
            职责：模板文件：提供可复用提示词骨架。
        - release-acceptance-template.md：发布验收模板
            职责：模板文件：提供可复用提示词骨架。
        - test-case-template.md：测试用例模板
            职责：模板文件：提供可复用提示词骨架。
        - test-data-environment-template.md：测试数据与环境准备模板
            职责：模板文件：提供可复用提示词骨架。
        - test-execution-report-template.md：测试执行报告模板
            职责：模板文件：提供可复用提示词骨架。
        - test-plan-template.md：测试计划与用例模板
            职责：模板文件：提供可复用提示词骨架。
        - test-scope-analysis-template.md：测试范围分析模板
            职责：模板文件：提供可复用提示词骨架。
        - test-strategy-planning-template.md：测试策略规划模板
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-management-workflow.md：迭代记忆管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
      - tester
          职责：按上级目录规则归类的子目录。
        - README.md：测试工程师工作流
            职责：说明当前目录的用途、使用方式和注意事项。
        - acceptance-criteria-review-workflow.md：验收标准检查工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - api-integration-test-workflow.md：接口与集成测试工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - automation-test-planning-workflow.md：自动化测试规划工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - compatibility-test-workflow.md：兼容性测试工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - defect-reproduction-workflow.md：缺陷复现工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - exploratory-test-workflow.md：探索式测试工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - non-functional-risk-test-workflow.md：非功能风险测试工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - regression-test-workflow.md：回归测试范围工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - release-acceptance-workflow.md：发布验收工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - test-case-design-workflow.md：测试用例设计工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - test-data-environment-workflow.md：测试数据与环境准备工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - test-execution-report-workflow.md：测试执行报告工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - test-scope-analysis-workflow.md：测试范围分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - test-strategy-planning-workflow.md：测试策略规划工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - tester-workflow.md：测试工程师总入口工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - INSTALL.md：tester-kit 接入说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：tester-kit
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：tester-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：tester-kit 来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：tester-kit 使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - ui-designer-kit
      职责：按上级目录规则归类的子目录。
    - examples
        职责：按上级目录规则归类的子目录。
      - quick-start-example.md：ui-designer-kit 快速示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 使用说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - roles
        职责：按上级目录规则归类的子目录。
      - role-definition.md：UI 设计师角色定义
          职责：定义该角色的职责、常见输入和常见输出。
    - scorecards
        职责：按上级目录规则归类的子目录。
      - accessibility-usability-review-scorecard.md：可访问性与可用性检查评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - component-library-planning-scorecard.md：组件库规划评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-handoff-scorecard.md：设计交接评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-input-analysis-scorecard.md：设计输入分析评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-review-scorecard.md：设计评审评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-specification-scorecard.md：设计规范确认评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-system-audit-scorecard.md：设计系统检查评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-to-development-handoff-scorecard.md：设计到开发实现约束评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - design-token-scorecard.md：设计令牌与平台适配评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - information-architecture-scorecard.md：信息架构评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - interaction-optimization-scorecard.md：交互体验优化评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - interaction-state-scorecard.md：交互状态评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - page-type-pattern-scorecard.md：页面类型设计模式评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - responsive-adaptation-scorecard.md：响应式与多端适配评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - ui-design-scorecard.md：UI 设计输出评分表
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - standards
        职责：按上级目录规则归类的子目录。
      - quality-checklists
          职责：质量检查清单目录：存放通用或角色专属检查清单。
        - ui-designer-checklist.md：UI 设计质量检查清单
            职责：UI 设计师任务质量检查清单。
      - design-token-standard.md：设计令牌标准
          职责：标准文件：定义某类内容的合格条件。
      - interaction-quality-standard.md：交互质量标准
          职责：标准文件：定义某类内容的合格条件。
    - templates
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-summary-template.md：项目记忆摘要
            职责：模板文件：提供可复用提示词骨架。
      - ui-designer
          职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
        - README.md：UI 设计师模板
            职责：说明当前目录的用途、使用方式和注意事项。
        - accessibility-usability-review-template.md：可访问性与可用性检查模板
            职责：模板文件：提供可复用提示词骨架。
        - component-library-planning-template.md：组件库规划模板
            职责：模板文件：提供可复用提示词骨架。
        - design-handoff-template.md：设计交接模板
            职责：模板文件：提供可复用提示词骨架。
        - design-input-analysis-template.md：设计输入分析模板
            职责：模板文件：提供可复用提示词骨架。
        - design-review-template.md：设计评审模板
            职责：模板文件：提供可复用提示词骨架。
        - design-specification-template.md：设计规范确认模板
            职责：模板文件：提供可复用提示词骨架。
        - design-system-audit-template.md：设计系统检查模板
            职责：模板文件：提供可复用提示词骨架。
        - design-to-development-handoff-template.md：设计到开发实现约束模板
            职责：模板文件：提供可复用提示词骨架。
        - design-tokens-template.json
            职责：项目文件。
        - information-architecture-template.md：信息架构模板
            职责：模板文件：提供可复用提示词骨架。
        - interaction-optimization-template.md：交互体验优化方案模板
            职责：模板文件：提供可复用提示词骨架。
        - interaction-state-template.md：交互状态模板
            职责：模板文件：提供可复用提示词骨架。
        - page-type-pattern-template.md：页面类型设计模式模板
            职责：模板文件：提供可复用提示词骨架。
        - platform-adaptation-template.md：平台适配说明模板
            职责：模板文件：提供可复用提示词骨架。
        - responsive-adaptation-template.md：响应式与多端适配模板
            职责：模板文件：提供可复用提示词骨架。
        - ui-brief-template.md：UI Brief 模板
            职责：模板文件：提供可复用提示词骨架。
    - workflows
        职责：按上级目录规则归类的子目录。
      - common
          职责：通用内容目录：存放跨角色可复用内容。
        - iteration-memory-management-workflow.md：迭代记忆管理工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
      - ui-designer
          职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
        - README.md：UI 设计师工作流
            职责：说明当前目录的用途、使用方式和注意事项。
        - accessibility-usability-review-workflow.md：可访问性与可用性检查工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - component-library-planning-workflow.md：组件库规划工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-handoff-workflow.md：设计交接工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-input-analysis-workflow.md：设计输入分析工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-review-workflow.md：设计评审工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-specification-workflow.md：设计规范确认工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-system-audit-workflow.md：设计系统检查工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-to-development-handoff-workflow.md：设计到开发实现约束工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - design-token-workflow.md：设计令牌与平台适配工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - information-architecture-workflow.md：信息架构工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - interaction-optimization-workflow.md：交互体验优化工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - interaction-state-workflow.md：交互状态设计工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - page-type-pattern-workflow.md：页面类型设计模式工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - responsive-adaptation-workflow.md：响应式与多端适配工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - ui-designer-workflow.md：UI 设计总入口工作流
            职责：工作流文件：说明某类任务从输入到输出的处理步骤。
    - INSTALL.md：ui-designer-kit 接入说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：ui-designer-kit
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：ui-designer-kit
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - manifest.md：ui-designer-kit 来源清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：ui-designer-kit 使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - workflowproject-kit
      职责：按上级目录规则归类的子目录。
    - agents
        职责：按上级目录规则归类的子目录。
      - openai.yaml
          职责：项目文件。
    - examples
        职责：按上级目录规则归类的子目录。
      - quick-start-example.md：快速示例
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - integrations
        职责：按上级目录规则归类的子目录。
      - codex-usage.md：Codex 接入
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - cursor-usage.md：Cursor 接入
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - kits
        职责：按上级目录规则归类的子目录。
      - developer-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - README.md：示例区
              职责：说明当前目录的用途、使用方式和注意事项。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - developer-governance-capability-system.md：developer-kit 开发治理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - ponytail-minimal-change-principles.md：Ponytail 最小必要变更原则
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - minimal-change-guardian.md：最小必要变更守门人
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - role-definition.md：开发工程师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - ai-collaboration-retrospective-scorecard.md：AI 协作复盘评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - architecture-decision-record-scorecard.md：架构决策记录评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - change-risk-assessment-scorecard.md：变更风险评估评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - code-review-scorecard.md：代码评审评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - data-api-contract-scorecard.md：数据/API/状态契约评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - dependency-and-tech-debt-scorecard.md：依赖与技术债治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - documentation-sync-scorecard.md：文档同步评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - environment-config-governance-scorecard.md：环境与配置治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - impact-analysis-scorecard.md：影响范围分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - implementation-scorecard.md：代码实现执行评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - issue-diagnosis-scorecard.md：问题定位评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - minimal-change-governance-scorecard.md：最小必要变更治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - module-boundary-analysis-scorecard.md：模块边界分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - project-bootstrap-scorecard.md：新项目启动治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - project-understanding-scorecard.md：已有项目理解评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - release-and-rollback-scorecard.md：发布与回滚治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-to-architecture-scorecard.md：需求到架构影响分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - security-permission-scorecard.md：安全与权限治理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - testing-verification-scorecard.md：测试与验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - workflow-orchestration-scorecard.md：开发工作流协同编排评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - developer
              职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
            - README.md：开发工程师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - ai-collaboration-retrospective-template.md：AI 协作复盘报告模板
                职责：模板文件：提供可复用提示词骨架。
            - architecture-decision-record-template.md：ADR 模板
                职责：模板文件：提供可复用提示词骨架。
            - change-risk-assessment-template.md：变更风险评估报告模板
                职责：模板文件：提供可复用提示词骨架。
            - code-review-template.md：代码评审报告模板
                职责：模板文件：提供可复用提示词骨架。
            - data-api-contract-template.md：数据/API/状态契约报告
                职责：模板文件：提供可复用提示词骨架。
            - dependency-and-tech-debt-template.md：依赖与技术债治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - documentation-sync-template.md：文档同步报告模板
                职责：模板文件：提供可复用提示词骨架。
            - environment-config-governance-template.md：环境与配置治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - impact-analysis-template.md：影响范围分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - implementation-template.md：实现交付说明模板
                职责：模板文件：提供可复用提示词骨架。
            - issue-diagnosis-template.md：问题定位报告
                职责：模板文件：提供可复用提示词骨架。
            - minimal-change-governance-template.md：最小必要变更治理模板
                职责：模板文件：提供可复用提示词骨架。
            - module-boundary-analysis-template.md：模块边界分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - project-bootstrap-template.md：新项目启动治理模板
                职责：模板文件：提供可复用提示词骨架。
            - project-understanding-template.md：项目理解报告模板
                职责：模板文件：提供可复用提示词骨架。
            - release-and-rollback-template.md：发布与回滚治理报告模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-to-architecture-template.md：架构影响分析报告模板
                职责：模板文件：提供可复用提示词骨架。
            - security-permission-template.md：安全与权限治理报告
                职责：模板文件：提供可复用提示词骨架。
            - testing-verification-template.md：测试与验收报告模板
                职责：模板文件：提供可复用提示词骨架。
            - workflow-orchestration-template.md：开发工作流协同编排记录
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - developer
              职责：开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。
            - README.md：开发工程师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - ai-collaboration-retrospective-workflow.md：AI 协作复盘工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - architecture-decision-record-workflow.md：架构决策记录工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - change-risk-assessment-workflow.md：变更风险评估工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - code-review-workflow.md：代码评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - data-api-contract-workflow.md：数据/API/状态契约工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - dependency-and-tech-debt-workflow.md：依赖与技术债治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - developer-kit-workflow.md：开发治理总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - documentation-sync-workflow.md：文档同步工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - environment-config-governance-workflow.md：环境与配置治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - impact-analysis-workflow.md：影响范围分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - implementation-workflow.md：代码实现执行工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - issue-diagnosis-workflow.md：问题定位工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - minimal-change-governance-workflow.md：最小必要变更治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - module-boundary-analysis-workflow.md：模块边界分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - project-bootstrap-workflow.md：新项目启动治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - project-understanding-workflow.md：已有项目理解工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - release-and-rollback-workflow.md：发布与回滚治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-to-architecture-workflow.md：需求到架构影响分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - security-permission-workflow.md：安全与权限治理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - testing-verification-workflow.md：测试与验收工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - workflow-orchestration-guide.md：开发工作流协同编排指南
                职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：developer-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：developer-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - product-manager-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - README.md：示例说明
              职责：说明当前目录的用途、使用方式和注意事项。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - product-manager-capability-system.md：产品经理能力体系
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：产品经理角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - acceptance-criteria-scorecard.md：验收标准评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - competitor-analysis-scorecard.md：竞品分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - feature-planning-scorecard.md：功能规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - prd-scorecard.md：PRD 评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - priority-decision-scorecard.md：优先级判断评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - product-roadmap-scorecard.md：产品路线图评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - product-strategy-scorecard.md：产品策略判断评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-analysis-scorecard.md：需求分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-change-evaluation-scorecard.md：需求变更评估评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - requirement-pool-scorecard.md：需求池管理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - user-feedback-scorecard.md：用户反馈整理评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - user-story-scorecard.md：用户故事评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - version-planning-scorecard.md：版本规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - version-retrospective-scorecard.md：版本复盘评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - meta
              职责：元模板目录：存放用于生成、评审、提取和优化提示词资产的模板。
            - idea-to-input-generator.md：想法转输入生成器
                职责：用于把用户模糊想法整理成标准输入文档。
            - output-reviewer.md：输出评审器
                职责：用于评审 AI 输出质量。
          - product-manager
              职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
            - README.md：产品经理模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-template.md：验收标准模板
                职责：模板文件：提供可复用提示词骨架。
            - competitor-analysis-template.md：竞品分析模板
                职责：模板文件：提供可复用提示词骨架。
            - feature-planning-template.md：功能规划模板
                职责：模板文件：提供可复用提示词骨架。
            - prd-template.md：PRD 模板
                职责：模板文件：提供可复用提示词骨架。
            - priority-decision-template.md：优先级判断模板
                职责：模板文件：提供可复用提示词骨架。
            - product-roadmap-template.md：产品路线图模板
                职责：模板文件：提供可复用提示词骨架。
            - product-strategy-template.md：产品策略判断模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-analysis-template.md：需求分析模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-change-evaluation-template.md：需求变更评估模板
                职责：模板文件：提供可复用提示词骨架。
            - requirement-pool-template.md：需求池管理模板
                职责：模板文件：提供可复用提示词骨架。
            - user-feedback-template.md：用户反馈整理模板
                职责：模板文件：提供可复用提示词骨架。
            - user-story-template.md：用户故事模板
                职责：模板文件：提供可复用提示词骨架。
            - version-planning-template.md：版本规划模板
                职责：模板文件：提供可复用提示词骨架。
            - version-retrospective-template.md：版本复盘模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - idea-to-input-workflow.md：想法转输入工作流
                职责：用于把用户口头描述、模糊想法或零散需求整理成标准输入。
            - input-analysis-workflow.md：输入分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - output-review-workflow.md：输出评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - product-manager
              职责：产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。
            - README.md：产品经理工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-workflow.md：验收标准生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - competitor-analysis-workflow.md：竞品分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - feature-planning-workflow.md：功能规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - prd-generation-workflow.md：PRD 生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - priority-decision-workflow.md：优先级判断工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-manager-workflow.md：产品经理总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-roadmap-workflow.md：产品路线图工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - product-strategy-workflow.md：产品策略判断工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-analysis-workflow.md：需求分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-change-evaluation-workflow.md：需求变更评估工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - requirement-pool-workflow.md：需求池管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - user-feedback-workflow.md：用户反馈整理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - user-story-workflow.md：用户故事生成工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - version-planning-workflow.md：版本规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - version-retrospective-workflow.md：版本复盘工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：产品经理能力包
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：product-manager-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - project-governance-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - project-governance-standard.md：项目治理标准
              职责：标准文件：定义某类内容的合格条件。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - project-governance-checklist-template.md：项目治理检查清单模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - project-governance-workflow.md：项目治理与开发前置工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：project-governance-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：project-governance-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - team-orchestration-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：快速启动示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - knowledge
            职责：按上级目录规则归类的子目录。
          - agent-orchestration-standard.md：Agent 调度标准
              职责：标准文件：定义某类内容的合格条件。
          - role-kit-lifecycle-standard.md：角色能力包生命周期标准
              职责：标准文件：定义某类内容的合格条件。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - team-orchestration-scorecard.md：跨角色团队总调度评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - agent-result-report-template.md：子 Agent 结果回报
                职责：模板文件：提供可复用提示词骨架。
            - agent-task-brief-template.md：子 Agent 任务简报
                职责：模板文件：提供可复用提示词骨架。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - mixed
              职责：跨角色项目目录：承载不属于单一角色的任务项目。
            - README.md：混合角色模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - team-orchestration-template.md：跨角色团队总调度模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - agent-orchestration-workflow.md：Agent 调度工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - mixed
              职责：跨角色项目目录：承载不属于单一角色的任务项目。
            - README.md：混合角色工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - team-orchestration-workflow.md：跨角色团队总调度工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：安装说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：team-orchestration-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：team-orchestration-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - tester-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：tester-kit 快速示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：测试工程师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - acceptance-criteria-review-scorecard.md：验收标准检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - api-integration-test-scorecard.md：接口与集成测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - automation-test-planning-scorecard.md：自动化测试规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - compatibility-test-scorecard.md：兼容性测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - defect-reproduction-scorecard.md：缺陷复现评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - exploratory-test-scorecard.md：探索式测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - non-functional-risk-test-scorecard.md：非功能风险测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - regression-test-scorecard.md：回归测试评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - release-acceptance-scorecard.md：发布验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-case-scorecard.md：测试用例评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-data-environment-scorecard.md：测试数据与环境准备评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-execution-report-scorecard.md：测试执行报告评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-scope-analysis-scorecard.md：测试范围分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - test-strategy-planning-scorecard.md：测试策略规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - tester-scorecard.md：测试输出评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - testing-verification-scorecard.md：测试与验收评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - quality-checklists
              职责：质量检查清单目录：存放通用或角色专属检查清单。
            - tester-checklist.md：测试质量检查清单
                职责：检查清单文件：用于快速确认内容是否达标。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - tester
              职责：按上级目录规则归类的子目录。
            - README.md：测试工程师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-review-template.md：验收标准检查模板
                职责：模板文件：提供可复用提示词骨架。
            - api-integration-test-template.md：接口与集成测试模板
                职责：模板文件：提供可复用提示词骨架。
            - automation-test-planning-template.md：自动化测试规划模板
                职责：模板文件：提供可复用提示词骨架。
            - compatibility-test-template.md：兼容性测试模板
                职责：模板文件：提供可复用提示词骨架。
            - defect-reproduction-template.md：缺陷复现模板
                职责：模板文件：提供可复用提示词骨架。
            - exploratory-test-template.md：探索式测试模板
                职责：模板文件：提供可复用提示词骨架。
            - non-functional-risk-test-template.md：非功能风险测试模板
                职责：模板文件：提供可复用提示词骨架。
            - regression-test-template.md：回归测试范围模板
                职责：模板文件：提供可复用提示词骨架。
            - release-acceptance-template.md：发布验收模板
                职责：模板文件：提供可复用提示词骨架。
            - test-case-template.md：测试用例模板
                职责：模板文件：提供可复用提示词骨架。
            - test-data-environment-template.md：测试数据与环境准备模板
                职责：模板文件：提供可复用提示词骨架。
            - test-execution-report-template.md：测试执行报告模板
                职责：模板文件：提供可复用提示词骨架。
            - test-plan-template.md：测试计划与用例模板
                职责：模板文件：提供可复用提示词骨架。
            - test-scope-analysis-template.md：测试范围分析模板
                职责：模板文件：提供可复用提示词骨架。
            - test-strategy-planning-template.md：测试策略规划模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - tester
              职责：按上级目录规则归类的子目录。
            - README.md：测试工程师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - acceptance-criteria-review-workflow.md：验收标准检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - api-integration-test-workflow.md：接口与集成测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - automation-test-planning-workflow.md：自动化测试规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - compatibility-test-workflow.md：兼容性测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - defect-reproduction-workflow.md：缺陷复现工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - exploratory-test-workflow.md：探索式测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - non-functional-risk-test-workflow.md：非功能风险测试工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - regression-test-workflow.md：回归测试范围工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - release-acceptance-workflow.md：发布验收工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-case-design-workflow.md：测试用例设计工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-data-environment-workflow.md：测试数据与环境准备工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-execution-report-workflow.md：测试执行报告工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-scope-analysis-workflow.md：测试范围分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - test-strategy-planning-workflow.md：测试策略规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - tester-workflow.md：测试工程师总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：tester-kit 接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：tester-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：tester-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：tester-kit 来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：tester-kit 使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - ui-designer-kit
          职责：按上级目录规则归类的子目录。
        - examples
            职责：按上级目录规则归类的子目录。
          - quick-start-example.md：ui-designer-kit 快速示例
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - integrations
            职责：按上级目录规则归类的子目录。
          - codex-usage.md：Codex 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - cursor-usage.md：Cursor 使用说明
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - roles
            职责：按上级目录规则归类的子目录。
          - role-definition.md：UI 设计师角色定义
              职责：定义该角色的职责、常见输入和常见输出。
        - scorecards
            职责：按上级目录规则归类的子目录。
          - accessibility-usability-review-scorecard.md：可访问性与可用性检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - component-library-planning-scorecard.md：组件库规划评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-handoff-scorecard.md：设计交接评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-input-analysis-scorecard.md：设计输入分析评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-review-scorecard.md：设计评审评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-specification-scorecard.md：设计规范确认评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-system-audit-scorecard.md：设计系统检查评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-to-development-handoff-scorecard.md：设计到开发实现约束评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - design-token-scorecard.md：设计令牌与平台适配评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - information-architecture-scorecard.md：信息架构评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - interaction-optimization-scorecard.md：交互体验优化评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - interaction-state-scorecard.md：交互状态评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - page-type-pattern-scorecard.md：页面类型设计模式评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - responsive-adaptation-scorecard.md：响应式与多端适配评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
          - ui-design-scorecard.md：UI 设计输出评分表
              职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - standards
            职责：按上级目录规则归类的子目录。
          - quality-checklists
              职责：质量检查清单目录：存放通用或角色专属检查清单。
            - ui-designer-checklist.md：UI 设计质量检查清单
                职责：UI 设计师任务质量检查清单。
          - design-token-standard.md：设计令牌标准
              职责：标准文件：定义某类内容的合格条件。
          - interaction-quality-standard.md：交互质量标准
              职责：标准文件：定义某类内容的合格条件。
        - templates
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-summary-template.md：项目记忆摘要
                职责：模板文件：提供可复用提示词骨架。
          - ui-designer
              职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
            - README.md：UI 设计师模板
                职责：说明当前目录的用途、使用方式和注意事项。
            - accessibility-usability-review-template.md：可访问性与可用性检查模板
                职责：模板文件：提供可复用提示词骨架。
            - component-library-planning-template.md：组件库规划模板
                职责：模板文件：提供可复用提示词骨架。
            - design-handoff-template.md：设计交接模板
                职责：模板文件：提供可复用提示词骨架。
            - design-input-analysis-template.md：设计输入分析模板
                职责：模板文件：提供可复用提示词骨架。
            - design-review-template.md：设计评审模板
                职责：模板文件：提供可复用提示词骨架。
            - design-specification-template.md：设计规范确认模板
                职责：模板文件：提供可复用提示词骨架。
            - design-system-audit-template.md：设计系统检查模板
                职责：模板文件：提供可复用提示词骨架。
            - design-to-development-handoff-template.md：设计到开发实现约束模板
                职责：模板文件：提供可复用提示词骨架。
            - design-tokens-template.json
                职责：项目文件。
            - information-architecture-template.md：信息架构模板
                职责：模板文件：提供可复用提示词骨架。
            - interaction-optimization-template.md：交互体验优化方案模板
                职责：模板文件：提供可复用提示词骨架。
            - interaction-state-template.md：交互状态模板
                职责：模板文件：提供可复用提示词骨架。
            - page-type-pattern-template.md：页面类型设计模式模板
                职责：模板文件：提供可复用提示词骨架。
            - platform-adaptation-template.md：平台适配说明模板
                职责：模板文件：提供可复用提示词骨架。
            - responsive-adaptation-template.md：响应式与多端适配模板
                职责：模板文件：提供可复用提示词骨架。
            - ui-brief-template.md：UI Brief 模板
                职责：模板文件：提供可复用提示词骨架。
        - workflows
            职责：按上级目录规则归类的子目录。
          - common
              职责：通用内容目录：存放跨角色可复用内容。
            - iteration-memory-management-workflow.md：迭代记忆管理工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
          - ui-designer
              职责：UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。
            - README.md：UI 设计师工作流
                职责：说明当前目录的用途、使用方式和注意事项。
            - accessibility-usability-review-workflow.md：可访问性与可用性检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - component-library-planning-workflow.md：组件库规划工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-handoff-workflow.md：设计交接工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-input-analysis-workflow.md：设计输入分析工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-review-workflow.md：设计评审工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-specification-workflow.md：设计规范确认工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-system-audit-workflow.md：设计系统检查工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-to-development-handoff-workflow.md：设计到开发实现约束工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - design-token-workflow.md：设计令牌与平台适配工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - information-architecture-workflow.md：信息架构工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - interaction-optimization-workflow.md：交互体验优化工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - interaction-state-workflow.md：交互状态设计工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - page-type-pattern-workflow.md：页面类型设计模式工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - responsive-adaptation-workflow.md：响应式与多端适配工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
            - ui-designer-workflow.md：UI 设计总入口工作流
                职责：工作流文件：说明某类任务从输入到输出的处理步骤。
        - INSTALL.md：ui-designer-kit 接入说明
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - README.md：ui-designer-kit
            职责：说明当前目录的用途、使用方式和注意事项。
        - SKILL.md：ui-designer-kit
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - START-HERE.md：从这里开始
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - manifest.md：ui-designer-kit 来源清单
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
        - usage-guide.md：ui-designer-kit 使用指南
            职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - scripts
        职责：按上级目录规则归类的子目录。
      - install_project.py
          职责：辅助脚本：用于自动化生成或维护项目资产。
    - AGENTS.md：WorkflowProject AI 开发治理规则
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - AI-WORKFLOW-RULES.md：WorkflowProject AI 开发治理规则
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - INSTALL.md：安装说明
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - README.md：WorkflowProject 统一能力包
        职责：说明当前目录的用途、使用方式和注意事项。
    - SKILL.md：WorkflowProject 统一开发治理能力
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - START-HERE.md：WorkflowProject 统一能力包：从这里开始
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - cursor-rule-template.mdc
        职责：项目文件。
    - manifest.md：导出清单
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
    - usage-guide.md：使用指南
        职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - AGENTS.md：WorkflowProject AI 开发治理规则
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - AI-WORKFLOW-RULES.md：WorkflowProject AI 开发治理规则
      职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
  - README.md：能力导出区
      职责：说明当前目录的用途、使用方式和注意事项。
- 15-dashboard
    职责：可视化控制台层：用 React 展示项目总览、能力、流程、资产、风险和下一步。
  - src
      职责：按上级目录规则归类的子目录。
    - data.json
        职责：React 可视化控制台的数据源，由工具脚本自动生成。
    - main.jsx
        职责：项目文件。
    - styles.css
        职责：项目文件。
  - README.md：可视化控制台
      职责：说明当前目录的用途、使用方式和注意事项。
  - index.html
      职责：项目文件。
  - package-lock.json
      职责：项目文件。
  - package.json
      职责：项目文件。
- 99-archive
    职责：归档层：保存历史、废弃或不再参与日常使用的内容。
  - projects
      职责：按上级目录规则归类的子目录。
    - workflowproject-framework-bootstrap
        职责：按上级目录规则归类的子目录。
      - 00-progress
          职责：按上级目录规则归类的子目录。
        - decision-log.md：决策记录
            职责：记录项目执行过程中的重要决策和原因。
        - next-actions.md：下一步判断
            职责：记录当前项目状态、可选方向、推荐下一步和待确认问题。
        - progress-log.md：进度记录
            职责：记录项目执行过程中的进度、调度角色、工作流、模板和下一步。
      - 01-inputs
          职责：项目输入目录：存放本项目原始材料。
        - original-requirement.md：原始需求
            职责：记录项目原始需求和逐步明确的需求。
      - 02-analysis
          职责：项目分析目录：存放输入分析和需求整理结果。
        - input-analysis.md：输入分析
            职责：记录输入分析、任务类型、核心问题和关键决策。
      - 03-prompts
          职责：项目提示词目录：存放本项目正式提示词。
        - final-prompt.md：正式提示词
            职责：记录本项目使用的正式提示词。
      - 04-outputs
          职责：项目输出目录：存放本项目 AI 输出结果。
        - framework-output.md：框架输出
            职责：记录本项目实际产出的框架成果。
      - 05-review
          职责：项目评审目录：存放输出评审和评分记录。
        - output-review.md：输出评审
            职责：记录输出质量评审、评分和建议。
      - 06-lessons
          职责：项目复盘目录：存放经验、反模式和沉淀建议。
        - lessons.md：复盘经验
            职责：记录关键经验、可复用模式、反模式和后续改进。
        - promotion-notes.md：沉淀与提升记录
            职责：记录哪些内容已提升到全局，哪些暂不提升。
      - ARCHIVE-NOTE.md：归档说明
          职责：Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。
      - README.md：WorkflowProject 框架启动项目
          职责：说明当前目录的用途、使用方式和注意事项。
  - README.md：归档
      职责：说明当前目录的用途、使用方式和注意事项。
- tools
    职责：辅助脚本层：保存生成导图等自动化脚本。
  - create_project.py
      职责：快速创建新任务项目，并自动生成标准项目结构。
  - export_unified_kit.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - generate_asset_index.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - generate_dashboard_data.py
      职责：扫描项目目录并生成 React 可视化控制台使用的数据。
  - generate_file_responsibility_xmind.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - generate_operation_flow_xmind.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - generate_project_index.py
      职责：扫描 12-projects 并生成项目索引，帮助用户快速知道项目用途和下一步。
  - generate_xmind.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - install_project_kits.py
      职责：辅助脚本：用于自动化生成或维护项目资产。
  - refresh_maps.py
      职责：一键刷新控制台数据、全部 XMind 导图和对应 Markdown 大纲。
