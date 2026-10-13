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


mindmap = node(
    "WorkflowProject AI 工作流文档工程框架",
    [
        node(
            "1. 系统层：定义项目是什么",
            [
                node("00-system/project-vision.md：项目愿景"),
                node("00-system/architecture.md：总体架构"),
                node("00-system/terminology.md：核心术语"),
                node("00-system/naming-rules.md：命名规则"),
                node("00-system/document-lifecycle.md：文档生命周期"),
                node("00-system/operating-guide.md：操作指南"),
            ],
            "回答：这个项目是什么、如何组织、怎么运行。",
        ),
        node(
            "2. 治理层：管控项目怎么维护",
            [
                node("01-governance/contribution-rules.md：贡献规则"),
                node("01-governance/change-management.md：变更管理"),
                node("01-governance/versioning-rules.md：版本规则"),
                node("01-governance/review-process.md：评审流程"),
                node("01-governance/quality-gates.md：质量门禁"),
                node("01-governance/decision-records/：架构决策记录"),
            ],
            "回答：新增、修改、评审、升级时遵守什么规则。",
        ),
        node(
            "3. 角色层：定义 AI 协作身份",
            [
                node("02-roles/role-registry.md：角色注册表"),
                node("product-manager：产品经理"),
                node("developer：程序员 / 开发工程师"),
                node("ui-designer：UI 设计师"),
                node("researcher：研究员，预留"),
                node("marketer：市场营销，预留"),
                node("common：通用角色"),
            ],
            "回答：AI 应该以什么身份参与任务。",
        ),
        node(
            "4. 生产输入：收集原始资料",
            [
                node("03-inputs/raw-materials：原始材料"),
                node("03-inputs/requirements：需求资料"),
                node("03-inputs/references：参考资料"),
                node("03-inputs/meeting-notes：会议纪要"),
                node("03-inputs/screenshots：截图资料"),
                node("03-inputs/external-docs：外部文档"),
            ],
            "回答：任务开始前，资料放在哪里。",
        ),
        node(
            "5. 工作流层：定义怎么让 AI 协作",
            [
                node(
                    "common 通用链路",
                    [
                        node("input-analysis：输入分析"),
                        node("template-generation：模板生成"),
                        node("prompt-generation：正式提示词生成"),
                        node("output-review：输出评审"),
                        node("example-extraction：案例沉淀"),
                        node("template-iteration：模板迭代"),
                    ],
                ),
                node("product-manager：产品工作流"),
                node("developer：开发工作流"),
                node("ui-designer：设计工作流"),
                node("researcher / marketer：预留工作流"),
            ],
            "回答：从输入到模板、提示词、输出、案例，每一步怎么做。",
        ),
        node(
            "6. 标准层：定义什么是好的",
            [
                node("input-standard：输入标准"),
                node("role-standard：角色标准"),
                node("workflow-standard：工作流标准"),
                node("template-standard：模板标准"),
                node("prompt-standard：正式提示词标准"),
                node("output-standard：输出标准"),
                node("example-standard：案例标准"),
                node("project-standard：项目标准"),
                node("review-standard：评审标准"),
                node("quality-checklists：角色质量清单"),
            ],
            "回答：如何判断内容是否合格。",
        ),
        node(
            "7. 模板层：沉淀可复用提示词骨架",
            [
                node(
                    "meta：让 AI 生成和管理提示词资产",
                    [
                        node("template-generator：从资料生成模板"),
                        node("prompt-generator：从模板生成正式提示词"),
                        node("output-reviewer：评审 AI 输出"),
                        node("example-extractor：提取案例包"),
                        node("template-optimizer：优化模板"),
                    ],
                ),
                node("common：跨角色模板"),
                node("product-manager：产品模板"),
                node("developer：开发模板"),
                node("ui-designer：设计模板"),
                node("researcher / marketer：预留模板"),
            ],
            "回答：复用什么骨架来生成高质量提示词。",
        ),
        node(
            "8. 执行产物：保存本次任务结果",
            [
                node("07-prompts/draft：提示词草稿"),
                node("07-prompts/active：当前可执行提示词"),
                node("07-prompts/reviewed：已评审提示词"),
                node("07-prompts/deprecated：废弃提示词"),
                node("08-outputs/draft：未评审输出"),
                node("08-outputs/reviewed：已评审输出"),
                node("08-outputs/accepted：已采纳输出"),
                node("08-outputs/rejected：不采纳输出"),
            ],
            "回答：正式提示词和 AI 输出分别放哪里。",
        ),
        node(
            "9. 资产沉淀：让项目越用越强",
            [
                node("09-examples：优秀案例库"),
                node("10-knowledge-base/patterns：成功模式"),
                node("10-knowledge-base/anti-patterns：反模式"),
                node("10-knowledge-base/best-practices：最佳实践"),
                node("10-knowledge-base/reusable-blocks：可复用片段"),
                node("10-knowledge-base/lessons-learned：经验复盘"),
                node("11-evaluations：测试、评分、对比、评估标准"),
            ],
            "回答：哪些结果值得长期复用和学习。",
        ),
        node(
            "10. 项目执行：承载真实任务",
            [
                node("12-projects/project-template：项目模板"),
                node("12-projects/product-manager：产品任务"),
                node("12-projects/developer：开发任务"),
                node("12-projects/ui-designer：设计任务"),
                node("12-projects/mixed：跨角色任务"),
                node("99-archive：历史归档"),
            ],
            "回答：每次真实任务如何落地和归档。",
        ),
        node(
            "核心闭环",
            [
                node("原始资料"),
                node("AI 协作流程"),
                node("可复用模板"),
                node("正式提示词"),
                node("AI 输出"),
                node("质量评审"),
                node("优秀案例"),
                node("知识沉淀"),
                node("反向优化模板和标准"),
            ],
            "这是整个项目最重要的生产链路。",
        ),
    ],
)


content = [
    {
        "id": uuid.uuid4().hex,
        "class": "sheet",
        "title": "WorkflowProject",
        "rootTopic": mindmap,
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

outline = """# WorkflowProject AI 工作流文档工程框架

- 1. 系统层：定义项目是什么
  - 00-system/project-vision.md：项目愿景
  - 00-system/architecture.md：总体架构
  - 00-system/terminology.md：核心术语
  - 00-system/naming-rules.md：命名规则
  - 00-system/document-lifecycle.md：文档生命周期
  - 00-system/operating-guide.md：操作指南
- 2. 治理层：管控项目怎么维护
  - 01-governance/contribution-rules.md：贡献规则
  - 01-governance/change-management.md：变更管理
  - 01-governance/versioning-rules.md：版本规则
  - 01-governance/review-process.md：评审流程
  - 01-governance/quality-gates.md：质量门禁
  - 01-governance/decision-records/：架构决策记录
- 3. 角色层：定义 AI 协作身份
  - 02-roles/role-registry.md：角色注册表
  - product-manager：产品经理
  - developer：程序员 / 开发工程师
  - ui-designer：UI 设计师
  - researcher：研究员，预留
  - marketer：市场营销，预留
  - common：通用角色
- 4. 生产输入：收集原始资料
  - raw-materials：原始材料
  - requirements：需求资料
  - references：参考资料
  - meeting-notes：会议纪要
  - screenshots：截图资料
  - external-docs：外部文档
- 5. 工作流层：定义怎么让 AI 协作
  - input-analysis：输入分析
  - template-generation：模板生成
  - prompt-generation：正式提示词生成
  - output-review：输出评审
  - example-extraction：案例沉淀
  - template-iteration：模板迭代
- 6. 标准层：定义什么是好的
  - input-standard
  - role-standard
  - workflow-standard
  - template-standard
  - prompt-standard
  - output-standard
  - example-standard
  - project-standard
  - review-standard
  - quality-checklists
- 7. 模板层：沉淀可复用提示词骨架
  - meta：template-generator、prompt-generator、output-reviewer、example-extractor、template-optimizer
  - common
  - product-manager
  - developer
  - ui-designer
  - researcher / marketer
- 8. 执行产物：保存本次任务结果
  - 07-prompts：draft、active、reviewed、deprecated
  - 08-outputs：draft、reviewed、accepted、rejected
- 9. 资产沉淀：让项目越用越强
  - 09-examples：优秀案例库
  - 10-knowledge-base：模式、反模式、最佳实践、复用片段、经验复盘
  - 11-evaluations：测试、评分、对比、评估标准
- 10. 项目执行：承载真实任务
  - 12-projects/project-template：项目模板
  - product-manager、developer、ui-designer、mixed
  - 99-archive：历史归档
- 核心闭环
  - 原始资料 -> AI 协作流程 -> 可复用模板 -> 正式提示词 -> AI 输出 -> 质量评审 -> 优秀案例 -> 知识沉淀 -> 反向优化
"""


def main():
    output_dir = ROOT / "13-visual-maps"
    output_dir.mkdir(exist_ok=True)
    xmind_path = output_dir / "WorkflowProject.xmind"
    outline_path = output_dir / "WorkflowProject-mindmap-outline.md"

    with zipfile.ZipFile(xmind_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.json", json.dumps(content, ensure_ascii=False, indent=2))
        zf.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    outline_path.write_text(outline, encoding="utf-8")

    print(xmind_path)
    print(outline_path)


if __name__ == "__main__":
    main()
