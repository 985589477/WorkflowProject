# WorkflowProject 框架刷新报告

## 刷新背景

WorkflowProject 已经从最初的框架搭建阶段，进入到角色能力建设、真实项目验证、可视化管理和能力导出的阶段。

早期 `workflowproject-framework-bootstrap` 记录了从 0 到 1 的搭建过程，但已经不能完整代表当前框架。

## 当前框架结构

当前框架由以下层组成：

| 层级 | 目录 | 职责 |
| --- | --- | --- |
| 系统规则层 | `00-system/` | 项目愿景、架构、术语、生命周期和操作指南 |
| 治理层 | `01-governance/` | 变更管理、评审流程、质量门禁和决策记录 |
| 角色层 | `02-roles/` | AI 协作角色定义 |
| 输入层 | `03-inputs/` | 原始资料和参考材料 |
| 工作流层 | `04-workflows/` | 从输入到输出的处理流程 |
| 标准层 | `05-standards/` | 输入、模板、提示词、输出和项目标准 |
| 模板层 | `06-templates/` | 可复用提示词模板 |
| 提示词层 | `07-prompts/` | 已填充输入的正式提示词 |
| 输出层 | `08-outputs/` | AI 输出结果 |
| 案例层 | `09-examples/` | 经过评审的优秀案例 |
| 知识层 | `10-knowledge-base/` | 可复用模式、反模式和经验 |
| 评估层 | `11-evaluations/` | 评分表、测试和评估方法 |
| 项目执行层 | `12-projects/` | 具体任务和能力建设记录 |
| 可视化导图层 | `13-visual-maps/` | XMind 和 Markdown 大纲 |
| 能力导出层 | `14-exports/` | 可独立使用的角色能力包或专项能力包 |
| 可视化控制台层 | `15-dashboard/` | React 项目状态控制台 |
| 归档层 | `99-archive/` | 历史、废弃或不再作为当前入口的内容 |

## 相比 bootstrap 的关键变化

- 新增 `13-visual-maps/`，统一管理 XMind 和导图大纲。
- 新增 `15-dashboard/`，提供 React 可视化控制台。
- 新增 `14-exports/`，支持把角色能力拆成独立能力包。
- 项目执行方式已经形成 `00-progress` 到 `06-lessons` 的标准链路。
- 产品经理能力体系已经从想法输入到版本复盘闭环。
- 已安装 `workflowproject-executor` skill，用于规范后续项目执行。

## 旧 bootstrap 处理建议

旧 bootstrap 不建议删除，建议归档。

推荐位置：

```text
99-archive/projects/workflowproject-framework-bootstrap/
```

归档后，它的职责变为：

```text
历史来源记录
```

不再作为当前框架说明或后续项目入口。

## 当前框架是否自洽

当前框架整体自洽。

原因：

- 全局资产和项目记录已经分离。
- 能力建设、真实案例、实验探索已经分层。
- 可视化导图和 dashboard 能提供全局视图。
- 能力导出层补齐了“对外交付能力包”的场景。
- 产品经理能力体系已经能验证角色能力建设模式。

## 风险与待补充

- `project-index.md` 中部分“推荐下一步”存在重复文字，后续可以优化生成脚本。
- `14-exports/` 已有规则，但还没有真实导出包验证。
- 产品经理能力已经完整，但开发、UI、测试等角色能力仍待建设。
- 后续如果能力包越来越多，需要考虑导出包版本管理。

## 后续维护建议

优先做一次真实导出验证：

```text
14-exports/product-manager-kit/
```

然后再根据使用体验决定是否增加自动导出脚本。

后续框架更新时，优先维护：

- `README.md`
- `00-system/architecture.md`
- `05-standards/project-standard.md`
- `12-projects/project-index.md`
- `13-visual-maps/`
- `15-dashboard/src/data.json`
