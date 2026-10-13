# 下一步判断

## 使用说明

这里用于帮助用户判断项目下一步该往哪里走。

## 当前项目状态

已完成第一轮验证，并已补充评审扣分点解决方案。

本项目已经用一句话产品想法生成了结构化需求分析，并完成评分评审。

扣分点解决方案位置：

```text
02-analysis/review-gap-resolution.md
```

## 可选方向

### 方向 A：继续推进当前项目

- 价值：可以继续把需求分析扩展为 PRD。
- 风险：如果边界未确认，PRD 会把“模板管理”和“AI 协作资产管理”混在一起。
- 建议：先确认产品边界，再进入 PRD。

### 方向 B：先补输入或上下文

- 价值：可以提升 PRD 质量。
- 风险：补充过多会拖慢验证节奏。
- 建议：只补关键问题，例如是否集成到 dashboard、是否管理 workflow 和案例。

### 方向 C：暂停并沉淀

- 价值：当前案例已经验证需求分析工作流第一版可用。
- 风险：不继续跑 PRD，就无法验证下游链路。
- 建议：可以先沉淀验证结果，再择机启动 PRD。

## 推荐下一步

推荐创建 PRD 项目，并把 `02-analysis/review-gap-resolution.md` 作为 PRD 输入材料之一：

```bash
python3 tools/create_project.py product-manager ai-template-tool-prd --type real-cases --title "AI 提示词模板工具 PRD 项目"
```

启动话术：

```text
请参考 12-projects/product-manager/real-cases/ai-template-tool-requirement-analysis 的需求分析结果，
尤其是 02-analysis/requirement-analysis.md 和 02-analysis/review-gap-resolution.md，
继续生成 AI 提示词模板工具的 PRD 初稿。
```

## 待确认问题

- 第一版是否采用“AI 协作资产导航层”定位。
- 第一版是否优先集成到 `15-dashboard`。
- 第一版是否纳入 workflow、template、scorecard 和 example。
- 是否需要一键创建项目。
- 是否记录模板使用次数、评分和复盘。
