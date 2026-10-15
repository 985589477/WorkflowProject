import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "15-dashboard" / "src" / "data.json"


def rel(path):
    return path.relative_to(ROOT).as_posix()


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_title(path):
    if not path.exists() or path.suffix != ".md":
        return path.stem
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except UnicodeDecodeError:
        return path.stem
    return path.stem


def read_field(path, field):
    if not path.exists():
        return ""
    prefix = f"{field}:"
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith(prefix):
                return line.split(":", 1)[1].strip()
    except UnicodeDecodeError:
        return ""
    return ""


def section_text(markdown, heading):
    lines = markdown.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start = index + 1
            break
    if start is None:
        return ""

    collected = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        collected.append(line)
    return "\n".join(collected).strip()


def first_content_line(markdown, heading):
    content = section_text(markdown, heading)
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        if stripped.startswith("- "):
            return stripped[2:].strip()
        return stripped
    return "未填写"


def section_summary(markdown, heading, max_parts=3):
    content = section_text(markdown, heading)
    parts = []
    in_code = False
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        parts.append(stripped)
        if len(parts) >= max_parts and not in_code:
            break
    return " ".join(parts) if parts else "未填写"


def list_files(base, pattern="*.md"):
    if not base.exists():
        return []
    return sorted(path for path in base.rglob(pattern) if path.is_file() and path.name != ".gitkeep")


def project_items():
    projects_dir = ROOT / "12-projects"
    items = []
    if not projects_dir.exists():
        return items
    readmes = list(projects_dir.glob("*/*/*/README.md"))
    readmes.extend(projects_dir.glob("*/*/README.md"))
    for readme in sorted(set(readmes)):
        if "project-template" in readme.parts:
            continue
        project_dir = readme.parent
        relative_parts = project_dir.relative_to(projects_dir).parts
        if len(relative_parts) >= 3:
            role, project_type = relative_parts[0], relative_parts[1]
        elif len(relative_parts) == 2:
            role, project_type = relative_parts[0], "legacy"
        else:
            continue
        content = read_text(readme)
        next_actions = read_text(project_dir / "00-progress" / "next-actions.md")
        items.append(
            {
                "name": project_dir.name,
                "title": read_title(readme),
                "role": role,
                "type": read_field(readme, "项目类型") or project_type,
                "state": read_field(readme, "状态") or "unknown",
                "path": rel(project_dir),
                "duty": first_content_line(content, "项目职责") if section_text(content, "项目职责") else first_content_line(content, "目标"),
                "useWhen": section_summary(content, "何时使用", max_parts=4) if section_text(content, "何时使用") else "需要理解或继续这个项目时使用。",
                "deliverables": section_summary(content, "关键产物", max_parts=4) if section_text(content, "关键产物") else "查看项目 README、04-outputs、05-review 和 06-lessons。",
                "goal": first_content_line(content, "目标"),
                "current": first_content_line(content, "当前状态"),
                "next": section_summary(next_actions, "推荐下一步", max_parts=5),
            }
        )
    return items


def example_items():
    examples_dir = ROOT / "09-examples"
    items = []
    if not examples_dir.exists():
        return items
    for readme in sorted(examples_dir.glob("*/*/README.md")):
        example_dir = readme.parent
        items.append(
            {
                "name": example_dir.name,
                "title": read_title(readme),
                "type": example_dir.parent.name,
                "state": read_field(readme, "状态") or "unknown",
                "path": rel(example_dir),
            }
        )
    return items


def asset_items():
    assets = []
    groups = [
        ("快速入口", [ROOT / "00-system" / "quick-start.md"]),
        ("运行助手", list_files(ROOT / "06-templates" / "meta")),
        ("通用模板", list_files(ROOT / "06-templates" / "common")),
        ("工作流", list_files(ROOT / "04-workflows" / "common")),
        ("知识模式", list_files(ROOT / "10-knowledge-base" / "patterns")),
        ("评估工具", list_files(ROOT / "11-evaluations")),
        ("工具脚本", sorted((ROOT / "tools").glob("*.py")) if (ROOT / "tools").exists() else []),
    ]
    for asset_type, paths in groups:
        for path in paths:
            if not path.exists() or path.name == "README.md":
                continue
            assets.append(
                {
                    "type": asset_type,
                    "name": path.stem,
                    "title": read_title(path) if path.suffix == ".md" else path.stem,
                    "path": rel(path),
                    "state": read_field(path, "状态") or ("active" if asset_type in {"快速入口", "工具脚本", "知识模式"} else "draft"),
                }
            )
    return assets


def capability_items():
    candidates = [
        ("想法转输入", "06-templates/meta/idea-to-input-generator.md", "可用", "把用户模糊想法整理成标准输入文档", "brain"),
        ("创建项目", "tools/create_project.py", "可用", "自动生成项目骨架、进度记录、决策记录和下一步判断", "play"),
        ("资产索引", "12-projects/asset-index.md", "可用", "按能力查找角色包、工作流、模板、评分表、标准和脚本", "library"),
        ("可解释执行", "06-templates/meta/explainable-project-runner.md", "可用", "执行前说明，执行后解释，帮助用户把控方向", "brain"),
        ("项目运行", "06-templates/meta/project-runner.md", "可用", "按项目规则推进下一步并汇报进度", "compass"),
        ("输出评审", "06-templates/meta/output-reviewer.md", "可用", "检查准确性、完整性、结构性和可执行性", "check"),
        ("案例沉淀", "04-workflows/common/example-extraction-workflow.md", "已验证", "将高质量项目整理成案例包", "library"),
        ("全局刷新", "tools/refresh_maps.py", "可用", "一键刷新项目索引、资产索引、控制台数据和 XMind 导图", "map"),
        ("知识提炼", "10-knowledge-base/patterns/framework-bootstrap-pattern.md", "已验证", "从案例提炼可复用模式", "boxes"),
    ]
    return [
        {"title": title, "path": path, "status": status, "note": note, "icon": icon}
        for title, path, status, note, icon in candidates
        if (ROOT / path).exists()
    ]


def risk_items(projects, examples):
    risks = [
        {
            "level": "中",
            "title": "角色模板仍需真实项目验证",
            "action": "先跑真实任务，再反向沉淀产品、开发、UI 模板。",
        },
        {
            "level": "中",
            "title": "规则继续增加会抬高使用成本",
            "action": "优先使用 quick-start、dashboard 和 project-runner。",
        },
    ]
    if len(projects) <= 1:
        risks.append(
            {
                "level": "中",
                "title": "真实业务项目还未启动",
                "action": "下一步建议创建第一个真实业务项目验证框架。",
            }
        )
    if not examples:
        risks.append(
            {
                "level": "高",
                "title": "还没有正式案例",
                "action": "先沉淀一个完整案例作为样板。",
            }
        )
    return risks


def next_actions(projects):
    return [
        {
            "title": "推荐",
            "text": "启动第一个真实业务项目",
            "reason": "基础设施已足够，真实任务能验证模板和流程。",
        },
        {
            "title": "可选",
            "text": "把 dashboard 继续升级为自动状态面板",
            "reason": "当前已自动生成数据，下一步可以增加筛选和详情视图。",
        },
        {
            "title": "暂缓",
            "text": "大量补角色模板",
            "reason": "没有真实任务验证时容易写空泛模板。",
        },
    ]


def main():
    projects = project_items()
    examples = example_items()
    assets = asset_items()
    workflows = list_files(ROOT / "04-workflows" / "common")
    templates = list_files(ROOT / "06-templates")

    data = {
        "updatedAt": "由 tools/generate_dashboard_data.py 生成",
        "stats": [
            {"label": "项目现场", "value": str(len(projects)), "detail": "12-projects", "tone": "green"},
            {"label": "正式案例", "value": str(len(examples)), "detail": "09-examples", "tone": "blue"},
            {"label": "模板文件", "value": str(len([p for p in templates if p.name != 'README.md'])), "detail": "06-templates", "tone": "violet"},
            {"label": "通用工作流", "value": str(len([p for p in workflows if p.name != 'README.md'])), "detail": "04-workflows/common", "tone": "amber"},
        ],
        "capabilities": capability_items(),
        "flow": ["材料", "输入分析", "模板", "正式提示词", "AI 输出", "评审", "案例", "知识"],
        "assets": assets[:16],
        "modules": [
            {"name": "系统规则", "scope": "00-system", "duty": "定义项目是什么、怎么运行、怎么让用户看懂 AI 执行过程"},
            {"name": "项目治理", "scope": "01-governance", "duty": "管理变更、评审、质量门禁和架构决策"},
            {"name": "工作流", "scope": "04-workflows", "duty": "规定从材料到输出、从项目到沉淀的处理路径"},
            {"name": "模板", "scope": "06-templates", "duty": "提供提示词骨架和项目运行助手"},
            {"name": "项目现场", "scope": "12-projects", "duty": "承载每一次真实任务"},
            {"name": "可视化", "scope": "13-visual-maps / 15-dashboard", "duty": "降低理解成本，形成全局视角"},
        ],
        "risks": risk_items(projects, examples),
        "nextActions": next_actions(projects),
        "projects": projects,
        "examples": examples,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
