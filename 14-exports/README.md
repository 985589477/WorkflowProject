# 能力导出区

这里存放从 WorkflowProject 中拆分出去的独立能力包。

能力包用于让某个角色或某组能力脱离当前项目独立使用，例如：

```text
14-exports/product-manager-kit/
14-exports/developer-kit/
14-exports/ui-designer-kit/
14-exports/tester-kit/
14-exports/team-orchestration-kit/
14-exports/project-governance-kit/
14-exports/workflowproject-kit/
```

## 它和其他目录的区别

| 目录 | 作用 |
| --- | --- |
| `04-workflows/` | 存放当前项目内部可复用工作流 |
| `06-templates/` | 存放当前项目内部可复用模板 |
| `11-evaluations/` | 存放当前项目内部评分表 |
| `12-projects/` | 存放一次具体项目的执行过程 |
| `14-exports/` | 存放可以离开当前项目单独使用的能力包 |

## 能力包建议结构

```text
{role}-kit/
├── START-HERE.md
├── README.md
├── usage-guide.md
├── INSTALL.md
├── SKILL.md
├── manifest.md
├── workflows/
├── templates/
├── scorecards/
├── knowledge/
├── examples/
└── integrations/
```

## 使用规则

- 不直接把整个 WorkflowProject 复制出去。
- 只导出目标角色或目标能力真正需要的文件。
- 导出包必须有独立 README，让外部使用者不需要理解完整项目也能使用。
- 导出包必须有 `START-HERE.md`，并使用统一格式，包含导出对象、导出时间、适用判断、一句话启动、外部自动读取配置、执行顺序、输出确认格式和使用原则。
- 导出包必须有 `manifest.md`，说明来源文件、用途、导出时间和适用范围。
- 导出包必须有 `INSTALL.md`，说明外部项目首次接入方式。
- 导出包必须有快速启动示例，例如 `examples/quick-start-example.md`。
- 导出包必须说明 Codex 和 Cursor 使用方式，例如 `integrations/codex-usage.md` 和 `integrations/cursor-usage.md`。
- 导出包必须有主入口工作流，且主入口必须是角色生命周期编排器，而不是单点任务分流器。
- 非角色专项能力包可以使用“能力生命周期编排器”，不应被强行设计成固定角色。
- 导出包必须包含执行状态格式和任务结束标准。
- 导出包如果会被长期使用，必须携带或说明迭代记忆管理方式。
- 导出包不使用复杂版本号，使用导出时间判断新旧。
- 导出包不应包含一次性项目过程材料，除非它们被整理成示例。
- 导出包新增或更新后，必须运行 `python3 tools/refresh_maps.py`，确保 `12-projects/asset-index.md` 能找到最新能力包。

## START-HERE 统一格式

所有导出包的 `START-HERE.md` 都必须包含：

```text
导出对象
导出时间
这个包能做什么
什么时候使用这个包
一句话启动
更短版本
外部自动读取配置
执行顺序
角色全链路原则
执行状态格式
外部项目输出目录策略
长期迭代记忆管理
输出确认格式
任务结束标准
使用原则
首次接入
```

其中“外部自动读取配置”用于告诉使用者：如果希望在其他项目里少输入启动话术，可以把规则复制到新项目根目录的默认读取文件，例如 `AI-WORKFLOW-RULES.md`。

## 长期迭代记忆管理

导出包如果会在外部项目中长期使用，应携带或说明：

```text
workflows/common/iteration-memory-management-workflow.md
templates/common/iteration-memory-summary-template.md
```

外部项目优先维护已有记忆文件，例如 `AGENTS.md`、`AI-WORKFLOW-RULES.md`、`docs/project-memory.md` 或 `docs/ai-context.md`。

如果没有合适文件，默认建议使用：

```text
docs/ai-memory-summary.md
```

具体标准见：

```text
05-standards/exported-kit-start-here-standard.md
05-standards/role-kit-lifecycle-standard.md
```

## 推荐工作流

```text
04-workflows/common/capability-export-workflow.md
```

## 当前能力包

### 统一安装包

- `workflowproject-kit/`：面向真实代码项目的一体化包，包含项目治理、跨角色调度、产品、UI、开发和测试能力。它是推荐给外部项目直接复制和安装的入口。

生成或刷新统一包：

```bash
python3 tools/export_unified_kit.py
```

复制统一包后，在目标项目执行：

```bash
python3 workflowproject-kit/scripts/install_project.py /目标代码项目
```

统一包根目录的 `SKILL.md` 可以作为 Codex Skill 使用，安装脚本会额外生成目标项目的 `AGENTS.md`、`AI-WORKFLOW-RULES.md` 和 Cursor 规则。

### 独立能力包

- `product-manager-kit/`：产品经理独立能力包，包含产品经理工作流、模板、评分表、角色定义和能力体系。
- `developer-kit/`：开发治理独立能力包，包含项目启动、项目理解、需求到架构、模块边界、代码实现、测试验收、评审、发布回滚和 AI 协作复盘等能力。
- `ui-designer-kit/`：UI 设计独立能力包，包含 UI brief、页面结构、组件状态、可用性检查和设计交接能力。
- `tester-kit/`：测试工程师独立能力包，包含测试计划、测试用例、回归范围、缺陷复现和发布验收能力。
- `team-orchestration-kit/`：跨角色团队总调度能力包，用于调度产品经理、UI 设计师、开发工程师和测试工程师，检查交接、互审和三方验收。
- `project-governance-kit/`：真实代码项目治理能力包，用于检查架构、模块、设计规范、任务列表和模块文档，并在缺失时引导补齐。

如果要从全局视角查看所有可用资产，优先看：

```text
12-projects/asset-index.md
```
