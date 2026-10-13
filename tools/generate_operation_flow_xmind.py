import json
import uuid
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def node(title, children=None, notes=None):
    topic = {
        "id": uuid.uuid4().hex,
        "title": title,
    }
    if children:
        topic["children"] = {"attached": children}
    if notes:
        topic["notes"] = {"plain": {"content": notes}}
    return topic


root = node(
    "从材料到输出的 AI 协作操作流程",
    [
        node(
            "0. 创建任务项目",
            [
                node("复制 12-projects/project-template/"),
                node("填写项目 README：目标、角色、输入来源、状态"),
                node("确定任务类型：产品 / 开发 / UI / 跨角色"),
            ],
            "先把本次任务放进一个项目容器，避免材料、提示词、输出散落。",
        ),
        node(
            "1. 放入原始材料",
            [
                node("需求、会议纪要、参考资料、截图、代码、业务背景"),
                node("优先放入项目内 01-inputs/"),
                node("长期可复用资料再提升到全局 03-inputs/"),
            ],
            "这一阶段只负责收集，不急着写模板。",
        ),
        node(
            "2. 分析输入材料",
            [
                node("使用 04-workflows/common/input-analysis-workflow.md"),
                node("提取背景、目标、关键事实、限制条件"),
                node("标记不确定信息和待确认问题"),
                node("判断适用角色和后续工作流"),
            ],
            "把杂乱资料整理成 AI 能稳定理解的结构化输入。",
        ),
        node(
            "3. 选择或生成模板",
            [
                node(
                    "已有模板",
                    [
                        node("从 06-templates/{role}/ 选择"),
                        node("检查是否符合当前任务"),
                    ],
                ),
                node(
                    "没有模板",
                    [
                        node("使用 06-templates/meta/template-generator.md"),
                        node("从输入材料抽象模板"),
                        node("根据 05-standards/template-standard.md 检查"),
                    ],
                ),
            ],
            "模板是可复用骨架，不是本次最终提示词。",
        ),
        node(
            "4. 生成正式提示词",
            [
                node("使用 06-templates/meta/prompt-generator.md"),
                node("把结构化输入填入模板占位符"),
                node("补充输出格式、质量标准、未知信息处理规则"),
                node("保存到项目 03-prompts/ 或全局 07-prompts/"),
            ],
            "正式提示词必须可以直接交给 AI 执行。",
        ),
        node(
            "5. 执行 AI 任务",
            [
                node("将正式提示词交给 AI"),
                node("获得 AI 输出"),
                node("保存到项目 04-outputs/ 或全局 08-outputs/draft/"),
            ],
            "这一阶段产出的只是 AI 输出，不自动等于合格结果或优秀案例。",
        ),
        node(
            "6. 评审输出质量",
            [
                node("使用 06-templates/meta/output-reviewer.md"),
                node("对照输入材料检查准确性"),
                node("对照提示词检查完整性和格式"),
                node("按 11-evaluations/evaluation-rubrics/ 评分"),
                node("保存评审到项目 05-review/"),
            ],
            "评审决定输出进入 accepted、rejected，还是需要重新生成。",
        ),
        node(
            "7. 处理评审结果",
            [
                node(
                    "通过",
                    [
                        node("移动或复制到 08-outputs/accepted/"),
                        node("进入案例沉淀判断"),
                    ],
                ),
                node(
                    "需修改",
                    [
                        node("调整输入或正式提示词"),
                        node("重新执行 AI"),
                    ],
                ),
                node(
                    "不采纳",
                    [
                        node("保存到 08-outputs/rejected/"),
                        node("记录问题原因"),
                    ],
                ),
            ],
            "不要跳过这一关，否则后面案例库会变脏。",
        ),
        node(
            "8. 沉淀优秀案例",
            [
                node("使用 04-workflows/common/example-extraction-workflow.md"),
                node("使用 06-templates/meta/example-extractor.md"),
                node("整理输入材料、工作流、模板、正式提示词、输出、评审、复盘"),
                node("保存到 09-examples/{role}/"),
            ],
            "只有高质量、可复用、可复盘的任务才进入优秀案例库。",
        ),
        node(
            "9. 提炼知识资产",
            [
                node("成功模式 -> 10-knowledge-base/patterns/"),
                node("常见错误 -> 10-knowledge-base/anti-patterns/"),
                node("最佳实践 -> 10-knowledge-base/best-practices/"),
                node("可复用片段 -> 10-knowledge-base/reusable-blocks/"),
                node("经验复盘 -> 10-knowledge-base/lessons-learned/"),
            ],
            "案例是一次任务，知识是跨任务规律。",
        ),
        node(
            "10. 反向优化框架",
            [
                node("模板问题 -> 使用模板优化器处理"),
                node("流程问题 -> 更新 04-workflows/"),
                node("标准问题 -> 更新 05-standards/"),
                node("架构问题 -> 新增 decision-record"),
                node("过时内容 -> 移入 99-archive/"),
            ],
            "让每次任务都反哺框架，而不是只产生一次性结果。",
        ),
        node(
            "完整闭环",
            [
                node("材料"),
                node("结构化输入"),
                node("模板"),
                node("正式提示词"),
                node("AI 输出"),
                node("评审结果"),
                node("优秀案例"),
                node("知识沉淀"),
                node("模板 / 标准 / 工作流迭代"),
            ],
        ),
    ],
)


content = [
    {
        "id": uuid.uuid4().hex,
        "class": "sheet",
        "title": "Operation Flow",
        "rootTopic": root,
        "topicPositioning": "fixed",
    }
]

metadata = {
    "creator": {"name": "Codex", "version": "1.0"},
    "activeSheetId": content[0]["id"],
}

manifest = {
    "file-entries": {
        "content.json": {},
        "metadata.json": {},
        "manifest.json": {},
    }
}

outline = """# 从材料到输出的 AI 协作操作流程

- 0. 创建任务项目
  - 复制 `12-projects/project-template/`
  - 填写项目 README：目标、角色、输入来源、状态
  - 确定任务类型：产品 / 开发 / UI / 跨角色
- 1. 放入原始材料
  - 需求、会议纪要、参考资料、截图、代码、业务背景
  - 优先放入项目内 `01-inputs/`
  - 长期可复用资料再提升到全局 `03-inputs/`
- 2. 分析输入材料
  - 使用 `04-workflows/common/input-analysis-workflow.md`
  - 提取背景、目标、关键事实、限制条件
  - 标记不确定信息和待确认问题
  - 判断适用角色和后续工作流
- 3. 选择或生成模板
  - 已有模板：从 `06-templates/{role}/` 选择
  - 没有模板：使用 `06-templates/meta/template-generator.md`
  - 根据 `05-standards/template-standard.md` 检查
- 4. 生成正式提示词
  - 使用 `06-templates/meta/prompt-generator.md`
  - 把结构化输入填入模板占位符
  - 补充输出格式、质量标准、未知信息处理规则
  - 保存到项目 `03-prompts/` 或全局 `07-prompts/`
- 5. 执行 AI 任务
  - 将正式提示词交给 AI
  - 获得 AI 输出
  - 保存到项目 `04-outputs/` 或全局 `08-outputs/draft/`
- 6. 评审输出质量
  - 使用 `06-templates/meta/output-reviewer.md`
  - 对照输入材料检查准确性
  - 对照提示词检查完整性和格式
  - 按 `11-evaluations/evaluation-rubrics/` 评分
  - 保存评审到项目 `05-review/`
- 7. 处理评审结果
  - 通过：进入 `08-outputs/accepted/`，再判断是否沉淀案例
  - 需修改：调整输入或正式提示词，重新执行 AI
  - 不采纳：保存到 `08-outputs/rejected/`，记录问题原因
- 8. 沉淀优秀案例
  - 使用 `04-workflows/common/example-extraction-workflow.md`
  - 使用 `06-templates/meta/example-extractor.md`
  - 整理输入材料、工作流、模板、正式提示词、输出、评审、复盘
  - 保存到 `09-examples/{role}/`
- 9. 提炼知识资产
  - 成功模式 -> `10-knowledge-base/patterns/`
  - 常见错误 -> `10-knowledge-base/anti-patterns/`
  - 最佳实践 -> `10-knowledge-base/best-practices/`
  - 可复用片段 -> `10-knowledge-base/reusable-blocks/`
  - 经验复盘 -> `10-knowledge-base/lessons-learned/`
- 10. 反向优化框架
  - 模板问题 -> 使用模板优化器处理
  - 流程问题 -> 更新 `04-workflows/`
  - 标准问题 -> 更新 `05-standards/`
  - 架构问题 -> 新增 decision-record
  - 过时内容 -> 移入 `99-archive/`
- 完整闭环
  - 材料 -> 结构化输入 -> 模板 -> 正式提示词 -> AI 输出 -> 评审结果 -> 优秀案例 -> 知识沉淀 -> 模板 / 标准 / 工作流迭代
"""


def main():
    output_dir = ROOT / "13-visual-maps"
    output_dir.mkdir(exist_ok=True)
    xmind_path = output_dir / "WorkflowProject-operation-flow.xmind"
    outline_path = output_dir / "WorkflowProject-operation-flow-outline.md"

    with zipfile.ZipFile(xmind_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.json", json.dumps(content, ensure_ascii=False, indent=2))
        zf.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    outline_path.write_text(outline, encoding="utf-8")

    print(xmind_path)
    print(outline_path)


if __name__ == "__main__":
    main()
