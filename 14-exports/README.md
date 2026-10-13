# 能力导出区

这里存放从 WorkflowProject 中拆分出去的独立能力包。

能力包用于让某个角色或某组能力脱离当前项目独立使用，例如：

```text
14-exports/product-manager-kit/
14-exports/developer-kit/
14-exports/ui-designer-kit/
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
├── workflows/
├── templates/
├── scorecards/
├── examples/
└── manifest.md
```

## 使用规则

- 不直接把整个 WorkflowProject 复制出去。
- 只导出目标角色或目标能力真正需要的文件。
- 导出包必须有独立 README，让外部使用者不需要理解完整项目也能使用。
- 导出包必须有 `START-HERE.md`，并使用统一格式，包含导出对象、导出时间、适用判断、一句话启动、外部自动读取配置、执行顺序、输出确认格式和使用原则。
- 导出包必须有 `manifest.md`，说明来源文件、用途、导出时间和适用范围。
- 导出包不使用复杂版本号，使用导出时间判断新旧。
- 导出包不应包含一次性项目过程材料，除非它们被整理成示例。

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
输出确认格式
使用原则
```

其中“外部自动读取配置”用于告诉使用者：如果希望在其他项目里少输入启动话术，可以把规则复制到新项目根目录的默认读取文件，例如 `AI-WORKFLOW-RULES.md`。

具体标准见：

```text
05-standards/exported-kit-start-here-standard.md
```

## 推荐工作流

```text
04-workflows/common/capability-export-workflow.md
```

## 当前能力包

- `product-manager-kit/`：产品经理独立能力包，包含产品经理工作流、模板、评分表、角色定义和能力体系。
