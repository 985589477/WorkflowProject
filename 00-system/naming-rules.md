# 命名规则

## 基本规则

- 文件和目录使用小写英文、数字和连字符。
- 避免空格、中文标点和含糊缩写。
- 同类文件保持统一后缀，例如 `*-workflow.md`、`*-template.md`、`*-standard.md`。
- 文件路径优先保持英文稳定，文档正文优先使用中文。具体语言规则见 `00-system/language-rules.md`。

## 推荐命名

```text
角色：product-manager、developer、ui-designer
工作流：requirement-to-prd-workflow.md
模板：prd-generation-template.md
正式提示词：member-subscription-prd-prompt.md
输出：member-subscription-prd-output.md
评审：member-subscription-prd-review.md
案例目录：member-subscription-prd/
```

## 状态命名

正式提示词和输出优先通过目录表达状态：

```text
draft/
active/
reviewed/
deprecated/
accepted/
rejected/
```

如果必须在文件名表达版本或状态，使用：

```text
prd-generation-template.v1.md
prd-generation-template.v2.md
member-subscription-prd-prompt.reviewed.md
```
