# Document Lifecycle

## 标准生命周期

```text
raw
-> analyzed
-> draft
-> reviewed
-> active / accepted
-> example / knowledge
-> deprecated
-> archived
```

## 生命周期含义

- `raw`：未经处理的原始资料。
- `analyzed`：已被分析、拆解或标注的资料。
- `draft`：草稿状态，尚未评审。
- `reviewed`：已完成质量检查。
- `active`：当前推荐使用的模板或提示词。
- `accepted`：已确认可用的输出。
- `example`：具备复用价值的优秀案例。
- `knowledge`：从案例抽象出的长期知识。
- `deprecated`：不再推荐使用，但暂时保留。
- `archived`：历史保留，不参与日常使用。

## 晋级规则

模板从 `draft` 晋级到 `active` 前，必须通过模板质量门禁。

输出从 `draft` 晋级到 `accepted` 前，必须通过输出评审。

案例进入 `09-examples/` 前，必须包含完整生产链路：

```text
input
workflow
template
prompt
output
review
lessons
```
