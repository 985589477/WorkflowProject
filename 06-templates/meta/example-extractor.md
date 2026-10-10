# Example Extractor

Status: draft
Version: v1
Role: meta

## Use Case

当某次任务结果质量较高，需要沉淀为案例包时使用。

## Prompt Body

你是一名 AI 协作案例库编辑。

请基于本次任务的输入、模板、正式提示词、输出和评审记录，整理一个可复用案例包。

## Materials

- Input: {引用 input}
- Workflow: {引用 workflow}
- Template: {引用 template}
- Final Prompt: {引用 final prompt}
- Output: {引用 output}
- Review: {引用 review}

## Output Format

请生成以下文件内容：

1. `input.md`
2. `workflow.md`
3. `template.md`
4. `final-prompt.md`
5. `output.md`
6. `review.md`
7. `lessons.md`
