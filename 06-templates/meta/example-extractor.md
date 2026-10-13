# 案例提取器

状态: draft
版本: v1
角色: meta

## 适用场景

当某次任务结果质量较高，需要沉淀为案例包时使用。

## 提示词正文

你是一名 AI 协作案例库编辑。

请基于本次任务的输入、模板、正式提示词、输出和评审记录，整理一个可复用案例包。

## 材料

- 输入材料: {引用 input}
- Workflow: {引用 workflow}
- 模板: {引用 template}
- Final Prompt: {引用 final prompt}
- 输出: {引用 output}
- 评审: {引用 review}

## 输出格式

请生成以下文件内容：

1. `input.md`
2. `workflow.md`
3. `template.md`
4. `final-prompt.md`
5. `output.md`
6. `review.md`
7. `lessons.md`
