import json
import uuid
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "13-visual-maps"

SKIP_DIRS = {".git", "__pycache__", "node_modules", "dist"}
SKIP_FILES = {".gitkeep", ".DS_Store"}
SKIP_SUFFIXES = {".xmind"}

TOP_LEVEL_DUTIES = {
    "00-system": "系统规则层：定义项目是什么、如何组织、如何运行。",
    "01-governance": "项目治理层：定义项目如何维护、变更、评审和管控。",
    "02-roles": "角色定义层：定义 AI 以什么角色参与任务。",
    "03-inputs": "全局输入资料层：存放可长期复用的原始资料。",
    "04-workflows": "工作流层：定义从材料到输出的处理步骤。",
    "05-standards": "标准层：定义什么样的输入、模板、提示词、输出和案例算合格。",
    "06-templates": "模板层：沉淀可复用提示词骨架和 meta 模板。",
    "07-prompts": "正式提示词层：保存可直接交给 AI 执行的提示词。",
    "08-outputs": "AI 输出层：保存 AI 生成结果并按状态管理。",
    "09-examples": "优秀案例层：保存经过评审且具备复用价值的案例。",
    "10-knowledge-base": "知识库层：沉淀跨任务的模式、反模式、最佳实践和经验。",
    "11-evaluations": "评估层：保存测试、评分、对比和评估方法。",
    "12-projects": "具体项目执行层：每次真实任务的工作现场。",
    "13-visual-maps": "可视化导图层：统一保存 XMind 导图和 Markdown 大纲。",
    "15-dashboard": "可视化控制台层：用 React 展示项目总览、能力、流程、资产、风险和下一步。",
    "99-archive": "归档层：保存历史、废弃或不再参与日常使用的内容。",
    "tools": "辅助脚本层：保存生成导图等自动化脚本。",
    "src": "前端源码目录：存放 React 组件和样式。",
}

DIR_DUTIES = {
    "common": "通用内容目录：存放跨角色可复用内容。",
    "meta": "元模板目录：存放用于生成、评审、提取和优化提示词资产的模板。",
    "product-manager": "产品经理目录：承载产品经理相关角色、工作流、模板、案例或项目。",
    "developer": "开发工程师目录：承载开发相关角色、工作流、模板、案例或项目。",
    "ui-designer": "UI 设计师目录：承载设计相关角色、工作流、模板、案例或项目。",
    "researcher": "研究员目录：预留研究相关角色、工作流或模板。",
    "marketer": "市场营销目录：预留营销相关角色、工作流或模板。",
    "mixed": "跨角色项目目录：承载不属于单一角色的任务项目。",
    "capability-building": "能力建设项目目录：承载用于建设 workflow、template、scorecard 和知识体系的项目。",
    "real-cases": "真实使用项目目录：承载使用已有能力处理具体业务需求的项目。",
    "experiments": "实验探索项目目录：承载不稳定想法和探索性任务。",
    "decision-records": "决策记录目录：记录重要架构或治理决策。",
    "quality-checklists": "质量检查清单目录：存放通用或角色专属检查清单。",
    "evaluation-rubrics": "评分规则目录：存放评估维度和评分规则。",
    "prompt-tests": "提示词测试目录：存放提示词测试记录。",
    "output-scorecards": "输出评分目录：存放 AI 输出评分表。",
    "comparison-reports": "对比报告目录：存放不同提示词或输出的对比结果。",
    "project-template": "项目模板目录：新项目优先复制这个骨架。",
    "01-inputs": "项目输入目录：存放本项目原始材料。",
    "02-analysis": "项目分析目录：存放输入分析和需求整理结果。",
    "03-prompts": "项目提示词目录：存放本项目正式提示词。",
    "04-outputs": "项目输出目录：存放本项目 AI 输出结果。",
    "05-review": "项目评审目录：存放输出评审和评分记录。",
    "06-lessons": "项目复盘目录：存放经验、反模式和沉淀建议。",
    "raw-materials": "原始材料目录：存放未加工资料。",
    "requirements": "需求资料目录：存放需求类输入。",
    "references": "参考资料目录：存放参考文档和参考信息。",
    "meeting-notes": "会议纪要目录：存放会议记录。",
    "screenshots": "截图资料目录：存放截图或截图说明。",
    "external-docs": "外部文档目录：存放来自外部的资料。",
    "draft": "草稿状态目录：存放尚未评审的内容。",
    "active": "可用状态目录：存放当前推荐使用的内容。",
    "reviewed": "已评审状态目录：存放已经检查过的内容。",
    "deprecated": "废弃状态目录：存放不再推荐使用但暂时保留的内容。",
    "accepted": "已采纳状态目录：存放确认可用的输出。",
    "rejected": "不采纳状态目录：存放不采用但保留原因的输出。",
    "cross-functional": "跨角色案例目录：存放跨多个角色的优秀案例。",
    "patterns": "成功模式目录：存放可复用成功规律。",
    "anti-patterns": "反模式目录：存放常见错误和应避免做法。",
    "best-practices": "最佳实践目录：存放稳定有效的做法。",
    "reusable-blocks": "可复用片段目录：存放可复用提示词片段或文档片段。",
    "lessons-learned": "经验复盘目录：存放跨项目复盘经验。",
}

FILE_DUTIES = {
    "README.md": "说明当前目录的用途、使用方式和注意事项。",
    "project-vision.md": "定义项目愿景、目标和非目标。",
    "architecture.md": "定义总体架构、分层关系和全局目录与项目目录的关系。",
    "terminology.md": "解释项目核心术语。",
    "naming-rules.md": "规定目录和文件命名方式，以及路径英文、正文中文原则。",
    "language-rules.md": "规定文档默认中文，必要技术标识保留英文。",
    "progress-reporting-rules.md": "规定项目执行过程中如何汇报当前进度、调度角色、使用工作流和下一步。",
    "execution-brief-rules.md": "规定 AI 执行前如何说明目标、原因、影响文件、调度角色和预计产出。",
    "result-report-rules.md": "规定 AI 执行后如何报告完成内容、文件变化、用途、下一步和风险。",
    "document-lifecycle.md": "定义文档生命周期和晋级规则。",
    "operating-guide.md": "说明如何创建任务、选择角色、使用工作流、生成模板、评审和沉淀。",
    "quick-start.md": "新用户快速入口：用最短路径说明如何从材料开始完成一次任务。",
    "contribution-rules.md": "规定新增内容前如何判断归属，以及贡献要求和禁止事项。",
    "change-management.md": "规定变更类型、变更要求和影响范围。",
    "versioning-rules.md": "规定模板、标准和工作流等内容的版本管理方式。",
    "review-process.md": "规定模板、正式提示词、输出和案例的评审流程。",
    "quality-gates.md": "规定进入正式状态或案例库前必须满足的质量门禁。",
    "role-registry.md": "登记当前活跃角色和计划支持角色。",
    "role-definition.md": "定义该角色的职责、常见输入和常见输出。",
    "input-standard.md": "定义输入资料必须包含的信息结构。",
    "role-standard.md": "定义角色文档和 active 角色的要求。",
    "workflow-standard.md": "定义工作流文档必须包含的结构。",
    "template-standard.md": "定义可复用模板必须包含的字段和禁止事项。",
    "prompt-standard.md": "定义正式提示词必须满足的要求。",
    "output-standard.md": "定义合格 AI 输出和不合格输出的表现。",
    "example-standard.md": "定义优秀案例包结构和进入条件。",
    "project-standard.md": "定义 12-projects 下任务项目的标准结构。",
    "review-standard.md": "定义评审维度和评分建议。",
    "common-checklist.md": "通用质量检查清单。",
    "product-manager-checklist.md": "产品经理任务质量检查清单。",
    "developer-checklist.md": "开发工程师任务质量检查清单。",
    "ui-designer-checklist.md": "UI 设计师任务质量检查清单。",
    "template-generator.md": "用于从原始资料生成可复用模板。",
    "idea-to-input-generator.md": "用于把用户模糊想法整理成标准输入文档。",
    "prompt-generator.md": "用于从模板和输入资料生成正式提示词。",
    "project-runner.md": "用于让 AI 按项目规则推进具体项目，并持续汇报进度和调度角色。",
    "explainable-project-runner.md": "用于让 AI 以可解释方式推进项目，帮助用户理解过程和把控方向。",
    "output-reviewer.md": "用于评审 AI 输出质量。",
    "example-extractor.md": "用于把高质量任务整理成案例包。",
    "template-optimizer.md": "用于根据案例和评审问题优化模板。",
    "framework-bootstrap-template.md": "用于搭建新的 AI 工作流文档框架。",
    "asset-promotion-workflow.md": "用于判断项目产物是否应提升为模板、案例、知识或评估方法。",
    "idea-to-input-workflow.md": "用于把用户口头描述、模糊想法或零散需求整理成标准输入。",
    "common-output-rubric.md": "通用 AI 输出评分规则。",
    "understanding-check-scorecard.md": "用于检查用户是否理解 AI 做了什么、为什么做以及下一步如何判断。",
    "original-requirement.md": "记录项目原始需求和逐步明确的需求。",
    "input-analysis.md": "记录输入分析、任务类型、核心问题和关键决策。",
    "final-prompt.md": "记录本项目使用的正式提示词。",
    "framework-output.md": "记录本项目实际产出的框架成果。",
    "output-review.md": "记录输出质量评审、评分和建议。",
    "progress-log.md": "记录项目执行过程中的进度、调度角色、工作流、模板和下一步。",
    "decision-log.md": "记录项目执行过程中的重要决策和原因。",
    "next-actions.md": "记录当前项目状态、可选方向、推荐下一步和待确认问题。",
    "lessons.md": "记录关键经验、可复用模式、反模式和后续改进。",
    "promotion-notes.md": "记录哪些内容已提升到全局，哪些暂不提升。",
    "create_project.py": "快速创建新任务项目，并自动生成标准项目结构。",
    "generate_dashboard_data.py": "扫描项目目录并生成 React 可视化控制台使用的数据。",
    "refresh_maps.py": "一键刷新控制台数据、全部 XMind 导图和对应 Markdown 大纲。",
    "generate_project_index.py": "扫描 12-projects 并生成项目索引，帮助用户快速知道项目用途和下一步。",
    "project-index.md": "自动生成的项目总览：列出每个项目的目标、状态、路径、下一步和启动方式。",
    "data.json": "React 可视化控制台的数据源，由工具脚本自动生成。",
    "framework-bootstrap-pattern.md": "从框架启动案例中提炼出的可复用搭建模式。",
}

SUFFIX_DUTIES = {
    "-workflow.md": "工作流文件：说明某类任务从输入到输出的处理步骤。",
    "-template.md": "模板文件：提供可复用提示词骨架。",
    "-standard.md": "标准文件：定义某类内容的合格条件。",
    "-checklist.md": "检查清单文件：用于快速确认内容是否达标。",
    "-rubric.md": "评分规则文件：用于对输出或提示词进行评分。",
    "-outline.md": "导图大纲文件：用于快速预览 XMind 内容。",
}


def make_node(title, children=None, notes=None):
    topic = {"id": uuid.uuid4().hex, "title": title}
    if children:
        topic["children"] = {"attached": children}
    if notes:
        topic["notes"] = {"plain": {"content": notes}}
    return topic


def should_skip(path):
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    if path.name in SKIP_FILES:
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    return False


def read_title(path):
    if path.suffix != ".md":
        return None
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    except UnicodeDecodeError:
        return None
    return None


def directory_duty(path):
    rel = path.relative_to(ROOT)
    if len(rel.parts) == 1:
        return TOP_LEVEL_DUTIES.get(path.name, "项目目录。")
    return DIR_DUTIES.get(path.name, "按上级目录规则归类的子目录。")


def file_duty(path):
    name = path.name
    if name in FILE_DUTIES:
        return FILE_DUTIES[name]
    for suffix, duty in SUFFIX_DUTIES.items():
        if name.endswith(suffix):
            return duty
    if path.suffix == ".py":
        return "辅助脚本：用于自动化生成或维护项目资产。"
    if path.suffix == ".md":
        return "Markdown 文档：记录项目说明、规则、流程、模板或复盘内容。"
    return "项目文件。"


def display_name(path, root_path):
    if path == root_path:
        return path.name
    title = read_title(path)
    if title:
        return f"{path.name}：{title}"
    return path.name


def build_tree(path, root_path=None):
    root_path = root_path or path
    if path.is_dir():
        children = []
        for child in sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name)):
            if should_skip(child):
                continue
            children.append(build_tree(child, root_path=path))
        if not children and path != ROOT:
            return make_node(f"{path.name}：空目录", notes=directory_duty(path))
        return make_node(display_name(path, root_path), children=children, notes=directory_duty(path))

    return make_node(display_name(path, root_path), notes=file_duty(path))


def top_level_nodes():
    nodes = []
    readme = ROOT / "README.md"
    if readme.exists():
        nodes.append(make_node("README.md：项目总入口", notes=file_duty(readme)))

    for child in sorted(ROOT.iterdir(), key=lambda item: item.name):
        if should_skip(child) or child.name == "README.md":
            continue
        nodes.append(build_tree(child))
    return nodes


def outline(topic, level=0):
    prefix = "# " if level == 0 else "  " * (level - 1) + "- "
    lines = [prefix + topic["title"]]
    notes = topic.get("notes", {}).get("plain", {}).get("content")
    if notes:
        lines.append("  " * level + "  职责：" + notes)
    for child in topic.get("children", {}).get("attached", []):
        lines.extend(outline(child, level + 1))
    return lines


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    root_topic = make_node(
        "WorkflowProject 当前文件与职责（自动扫描）",
        children=top_level_nodes(),
        notes="本导图由脚本自动扫描当前项目目录生成；新增文件后重新运行脚本即可更新。",
    )

    content = [
        {
            "id": uuid.uuid4().hex,
            "class": "sheet",
            "title": "文件职责图",
            "rootTopic": root_topic,
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

    xmind_path = OUTPUT_DIR / "WorkflowProject-file-responsibility.xmind"
    outline_path = OUTPUT_DIR / "WorkflowProject-file-responsibility-outline.md"

    with zipfile.ZipFile(xmind_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.json", json.dumps(content, ensure_ascii=False, indent=2))
        zf.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    outline_path.write_text("\n".join(outline(root_topic)) + "\n", encoding="utf-8")

    print(xmind_path)
    print(outline_path)


if __name__ == "__main__":
    main()
