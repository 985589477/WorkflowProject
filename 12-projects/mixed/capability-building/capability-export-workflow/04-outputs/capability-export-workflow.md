# 能力导出工作流

本项目已将能力导出工作流沉淀到：

```text
04-workflows/common/capability-export-workflow.md
```

并新增导出包统一入口标准：

```text
05-standards/exported-kit-start-here-standard.md
```

核心职责：

- 识别要导出的角色或能力。
- 收集相关 workflow、template、scorecard、knowledge 和 example。
- 判断依赖和排除范围。
- 生成独立能力包。
- 评审导出包是否能脱离 WorkflowProject 使用。

推荐导出目录：

```text
14-exports/
```

## 本轮导出结果：产品经理能力包

已完成第一次真实导出。

导出目标：

```text
14-exports/product-manager-kit/
```

## 导出包结构

```text
14-exports/product-manager-kit/
├── README.md
├── START-HERE.md
├── usage-guide.md
├── manifest.md
├── workflows/
│   ├── product-manager/
│   └── common/
├── templates/
│   ├── product-manager/
│   └── meta/
├── scorecards/
├── knowledge/
├── roles/
└── examples/
```

## 导出资产清单

| 类型 | 导出位置 | 来源 | 用途 |
| --- | --- | --- | --- |
| 产品经理工作流 | `workflows/product-manager/` | `04-workflows/product-manager/` | 产品经理核心能力 |
| 通用支撑工作流 | `workflows/common/` | `04-workflows/common/` | 想法转输入、输入分析、输出评审 |
| 产品经理模板 | `templates/product-manager/` | `06-templates/product-manager/` | 输出格式和提示词模板 |
| meta 模板 | `templates/meta/` | `06-templates/meta/` | 模糊想法整理和输出评审 |
| 评分表 | `scorecards/` | `11-evaluations/output-scorecards/` | 输出质量评估 |
| 角色定义 | `roles/` | `02-roles/product-manager/` | 产品经理角色边界 |
| 能力体系 | `knowledge/` | `10-knowledge-base/patterns/` | 产品经理能力地图 |

## 独立入口

最快入口：

```text
14-exports/product-manager-kit/START-HERE.md
```

`START-HERE.md` 已升级为所有导出包的统一入口格式，必须包含：

```text
导出对象
导出时间
这个包能做什么
什么时候使用这个包
一句话启动
更短版本
外部自动读取配置
执行顺序
输出确认格式
使用原则
```

其中“外部自动读取配置”用于指导使用者在新项目根目录创建默认规则文件，例如 `AI-WORKFLOW-RULES.md`，从而减少每次输入启动话术的成本。

能力包入口：

```text
14-exports/product-manager-kit/README.md
```

使用指南：

```text
14-exports/product-manager-kit/usage-guide.md
```

来源清单：

```text
14-exports/product-manager-kit/manifest.md
```

## 导出时间管理

本能力包不使用版本号。

后续判断新旧只看：

```text
导出时间：2026-10-13
```

导出时间记录在：

```text
START-HERE.md
README.md
usage-guide.md
manifest.md
```

## 未导出内容

- 未直接导出 `12-projects/` 中真实项目过程材料。
- 未导出 dashboard、XMind、归档文件。
- 未导出其他角色能力。

## 后续建议

下一步建议使用 `product-manager-kit` 跑一个真实任务，验证它是否真的能脱离 WorkflowProject 使用。
