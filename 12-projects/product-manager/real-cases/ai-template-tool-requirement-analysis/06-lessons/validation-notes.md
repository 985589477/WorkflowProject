# 验证记录

## 验证对象

- `04-workflows/product-manager/requirement-analysis-workflow.md`
- `06-templates/product-manager/requirement-analysis-template.md`
- `11-evaluations/output-scorecards/requirement-analysis-scorecard.md`

## 验证输入

一句话产品想法：

```text
我想做一个管理 AI 提示词模板的工具，可以保存、分类、复用和优化提示词。
```

## 验证结论

需求分析工作流可以把模糊想法整理成可进入 PRD 的结构化需求分析。

模板和评分表可以作为第一版全局资产继续保留。

## 发现的问题

- 当前需求分析模板适合生成单份分析文档，但还没有规定是否需要拆分多个中间分析文件。
- 评分表可以判断输出质量，但还没有要求评审者给出“是否沉淀为案例”的判断。
- 如果输入非常少，仍然需要先走 `idea-to-input-generator`。

## 后续优化建议

- 给需求分析模板补充“极简输入”和“完整输入”两种使用方式。
- 给评分表增加“案例沉淀价值”维度。
- 在项目索引中展示真实案例验证过哪些全局资产。
