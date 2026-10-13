# 输入分析

## 任务类型

这是通用能力建设项目。

本项目不是直接导出某个具体角色能力包，而是先建设“如何导出能力包”的通用方法。

## 为什么需要更新 WorkflowProject

当前项目已经有生产、沉淀、案例和可视化能力，但缺少“交付给外部使用”的结构层。

已有目录主要解决：

- 如何建设能力。
- 如何记录项目过程。
- 如何沉淀全局资产。
- 如何可视化项目状态。

但它们没有解决：

- 如何把某个角色能力独立拆出去。
- 如何让外部使用者不理解 WorkflowProject 也能使用。
- 如何记录导出包来源和版本。
- 如何评估导出包是否完整。

## 结构判断

需要新增：

```text
14-exports/
```

用于存放从当前项目导出的独立能力包。

## 能力边界

能力导出不等于归档，也不等于案例沉淀。

| 类型 | 作用 |
| --- | --- |
| 案例沉淀 | 把优秀项目结果变成参考案例 |
| 知识沉淀 | 把规律提炼成知识 |
| 能力导出 | 把稳定能力整理成外部可使用包 |
| 归档 | 保存历史或废弃内容 |

## 质量重点

- 导出包必须有独立入口。
- 导出包必须有来源清单。
- 导出包必须能独立使用。
- 不把内部过程材料原样塞出去。
- 导出能力前先判断资产依赖。

## 本轮导出分析：产品经理能力包

### 导出对象

```text
产品经理能力工作流
```

为了让能力包可独立使用，本轮不只导出 `04-workflows/product-manager/`，还需要导出其必要依赖。

### 使用对象

默认面向：

- 当前项目使用者本人。
- 未来需要单独使用产品经理能力的其他协作者。
- 可以阅读 Markdown 并与 AI 协作的人。

### 导出目标

```text
14-exports/product-manager-kit/
```

### 必须包含资产

| 类型 | 来源 | 导出位置 | 原因 |
| --- | --- | --- | --- |
| 产品经理工作流 | `04-workflows/product-manager/` | `workflows/product-manager/` | 核心能力 |
| 通用支撑工作流 | `04-workflows/common/idea-to-input-workflow.md` 等 | `workflows/common/` | 总入口依赖 |
| 产品经理模板 | `06-templates/product-manager/` | `templates/product-manager/` | 生成输出需要模板 |
| meta 模板 | `06-templates/meta/idea-to-input-generator.md` 等 | `templates/meta/` | 模糊想法和评审依赖 |
| 评分表 | `11-evaluations/output-scorecards/` 产品经理相关文件 | `scorecards/` | 输出质量评估 |
| 角色定义 | `02-roles/product-manager/role-definition.md` | `roles/` | 说明角色边界 |
| 能力体系 | `10-knowledge-base/patterns/product-manager-capability-system.md` | `knowledge/` | 帮助理解整体能力地图 |

### 暂不导出资产

| 类型 | 原因 |
| --- | --- |
| `12-projects/` 真实项目过程材料 | 上下文较重，容易混入一次性信息 |
| `15-dashboard/` | 属于 WorkflowProject 可视化系统，不是产品经理能力包必要依赖 |
| `13-visual-maps/` | 属于项目全局导图，不适合作为独立能力包主体 |
| 其他角色能力 | 本轮只导出产品经理能力 |

### 导出包结构

```text
14-exports/product-manager-kit/
├── README.md
├── usage-guide.md
├── manifest.md
├── workflows/
├── templates/
├── scorecards/
├── knowledge/
├── roles/
└── examples/
```

### 风险判断

- 当前导出包还没有完整真实案例样例。
- 部分工作流内部仍可能引用 WorkflowProject 原路径，但已通过包内目录保留相似结构降低理解成本。
- 后续如果产品经理全局资产继续变化，需要重新导出。
