#!/usr/bin/env python3
"""从现有独立能力包生成可携带的一体化 WorkflowProject Skill 包。"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "14-exports"
OUTPUT = EXPORTS / "workflowproject-kit"

SOURCE_KITS = [
    "project-governance-kit",
    "team-orchestration-kit",
    "product-manager-kit",
    "ui-designer-kit",
    "developer-kit",
    "tester-kit",
]


UNIFIED_SKILL = """---
name: workflowproject-kit
description: 用于已有或新建代码项目的 AI 协作开发。先检查项目治理、架构、模块、设计规范、任务、测试和记忆，再按需调度产品、UI、开发和测试能力。适用于需要从规划到验证的完整开发治理，而不是只回答一个孤立问题。
metadata:
  short-description: 从规划到验证治理 AI 开发
---

# WorkflowProject 统一开发治理能力

这是 WorkflowProject 面向真实代码项目的统一入口。

## 核心原则

目标代码项目是事实来源。本能力包提供可复用的方法和角色能力，但不替代目标项目的架构、约定、设计决策和业务事实。

## 必须遵守的生命周期

1. 先读取项目本地规则和已有文档。
2. 检查目标平台、主要语言、框架、运行时、构建方式、测试方式，以及架构、模块边界、设计规范、设备范围、任务列表、测试规则和项目记忆。
3. 区分已确认事实、AI 推断和需要确认的问题。
4. 缺少关键输入或存在歧义时，先询问用户，再做大范围决策。
5. 实现前先形成整体规划和有顺序的任务列表。
6. 一次执行一条任务，并在每条任务后验证。
7. 只调度当前任务真正需要的角色能力。
8. 跨角色工作时检查交接和验收。
9. 变更完成后同步受影响的项目文档和记忆。
10. 报告当前进度、当前负责人、验证证据、风险和下一步。

11. 简单任务直接使用 Skill，不创建子 Agent；组合任务才创建真实子 Agent。运行环境不支持时，先停下说明并询问是否降级。

新项目必须通过问询确认技术方案；已有项目新增模块时，先报告识别到的技术栈并询问是否沿用。没有确认前，不安装依赖、不创建工程骨架或新模块代码。

## 功能和组件开发问询门禁

当用户提出“开发一个组件”“做一个页面”或“增加一个功能”时，先问询：

```text
1. 这是已有项目中的功能，还是需要新建项目？
2. 如果是已有项目，应归属哪个模块？是扩展已有模块，还是规划新模块？
3. 当前是否已有架构、模块边界和开发规范？如果没有，是否先建立最小规范？
4. 当前是否已有 UI 设计系统、组件库、颜色、字体、间距和交互规范？如果没有，是否先建立本次功能需要的最小规范？
5. 目标端是什么：网页、移动端、iPad、桌面端还是多端？需要横屏、分屏或折叠屏适配吗？
6. 组件需要哪些状态和交互：默认、加载、空、错误、禁用、选中、悬停、聚焦、异常和权限？
7. 验收标准、测试范围和交付文档需要达到什么程度？
```

如果用户不知道如何制定规范，提供三个选择：沿用已有规范、建立本次功能的最小规范、先只输出整体方案暂不写代码。用户未确认项目归属、模块边界、UI 方向和适配范围前，不进入实现。

## 包含的能力包

只读取当前任务需要的能力包：

- `kits/project-governance-kit/SKILL.md`：项目治理和缺口检查。
- `kits/team-orchestration-kit/SKILL.md`：跨角色调度、交接和验收。
- `kits/product-manager-kit/SKILL.md`：产品和需求工作。
- `kits/ui-designer-kit/SKILL.md`：UI 结构、组件、设计规范和适配。
- `kits/developer-kit/SKILL.md`：架构、模块、实现、评审、发布和回滚。
- `kits/tester-kit/SKILL.md`：测试范围、用例、缺陷、回归和发布验收。

## 调度规则

项目开发请求先使用本统一入口。不要强制所有角色参与：需要多个角色或交接时使用团队总调度；其他情况完成治理检查后，使用最小范围的相关角色能力。

## Skill 与子 Agent 分流门禁

总入口先判断任务复杂度：

- 单角色、单产出、无交接、无并行的简单任务：当前 Agent 直接调用一个最小范围的 Skill，不创建子 Agent。
- 多角色、多阶段、需要交接、联合验收、并行或用户明确要求父子 Agent 的组合任务：父 Agent 必须建立任务树并创建真实子 Agent。
- 组合任务如果运行环境没有真实子 Agent 工具：先报告能力限制并询问用户，未经确认不得降级，也不得把单 Agent 顺序执行描述为子 Agent 协作。

每次执行必须报告模式：

```text
执行模式：单 Agent + Skill / 父 Agent + 子 Agent / 单 Agent 降级模拟，不是真实子 Agent
```

子 Agent 必须获得明确的任务简报、文件边界和验收标准，并返回结构化结果。简单任务禁止为了形式创建子 Agent。

## 项目接入

包内的 `scripts/install_project.py` 可以把能力安装到目标项目，生成项目级 `.ai/kits/`、`AGENTS.md`、`AI-WORKFLOW-RULES.md` 和 Cursor 规则。除非明确使用 `--force`，否则已有文件不会被覆盖。

## 完成标准

不能因为代码已经写入就直接宣称完成。完成必须同时具备：需求行为已实现、相关验证已完成、项目文档已同步、风险或待确认问题已记录，以及未完成时明确下一步。
"""


OPENAI_YAML = """interface:
  display_name: "WorkflowProject 开发治理"
  short_description: "从需求到验证治理 AI 开发"
  default_prompt: "使用 $workflowproject-kit 先检查项目治理材料，再规划并逐条完成这项开发任务。"
policy:
  allow_implicit_invocation: true
"""


AGENTS_CONTENT = """# WorkflowProject AI 开发治理规则

本项目已接入 WorkflowProject 统一能力包。

开始任何开发任务前：

1. 先读取项目已有的 `AGENTS.md`、`README.md`、架构、模块、设计规范、任务列表、测试规则和项目记忆。
2. 检查目标平台、主要语言、框架、运行时、构建方式和测试方式。
3. 如果任务涉及页面、组件或新功能，先问询项目归属、模块划分、项目规范、UI 设计规范、目标端、适配范围、组件状态和验收测试。
4. 区分已确认事实、AI 推断和需要用户确认的问题。
5. 新项目先问询确认技术方案；新模块先确认是否沿用当前项目技术栈。
6. 缺少关键材料时，先列出缺口并询问用户。
7. 先形成整体规划和按优先级排列的任务列表，再开始写代码。
8. 一次只执行一条任务，完成后立即验证。
9. 根据任务需要调用产品、UI、开发或测试能力，不强制所有角色参与。
10. 代码、测试、架构、模块、设计规范或任务状态发生变化时同步项目文档。
11. 对话中持续报告当前进度、当前调度角色、使用的工作流、验证结果和下一步。

12. 简单任务直接使用 Skill；组合任务才创建真实子 Agent，并在无法创建时明确停下询问。

统一能力包位置：`.ai/kits/`
"""


CURSOR_RULE = """---
description: WorkflowProject 项目级 AI 开发治理规则
alwaysApply: true
---

开始任务前，先读取项目本地规则和已有文档，并执行：

任务类型识别 -> 技术方案问询 -> 功能/组件问询（如适用） -> 项目治理检查 -> 架构与模块检查 -> 设计规范检查 -> 整体规划 -> 任务列表 -> 逐条实现 -> 逐条验证 -> 文档与记忆同步

缺少关键项目事实、技术方案或功能/组件设计信息未确认时，先向用户确认，不要直接大范围改动代码。根据实际需要使用 `.ai/kits/` 中的具体能力包。

执行分流：简单单角色任务直接调用 Skill，不创建子 Agent；组合任务由父 Agent 创建真实子 Agent。运行环境没有真实子 Agent 工具时，必须明确说明，未经用户确认不得伪装成子 Agent 协作。
"""


INSTALLER = r'''#!/usr/bin/env python3
"""把 workflowproject-kit 安装到目标代码项目。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
KITS_ROOT = PACKAGE_ROOT / "kits"


def write_text(path: Path, content: str, force: bool, dry_run: bool, changed: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(f"已存在，未覆盖：{path}")
        return
    if dry_run:
        changed.append(f"将写入：{path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    changed.append(str(path))


def install(args: argparse.Namespace) -> int:
    project = Path(args.project).expanduser().resolve()
    selected = [p.name for p in sorted(KITS_ROOT.iterdir()) if p.is_dir() and not p.name.startswith(".")]
    missing = [name for name in selected if not (KITS_ROOT / name / "SKILL.md").is_file()]
    if missing:
        print("能力包缺少 SKILL.md：" + ", ".join(missing))
        return 2

    changed: list[str] = []
    skipped: list[str] = []
    destination_root = project / ".ai" / "kits"
    print(f"目标项目：{project}")
    print("安装能力：" + ", ".join(selected))
    if args.dry_run:
        print("模式：预览，不写入文件")
    elif args.create_project:
        project.mkdir(parents=True, exist_ok=True)

    for name in selected:
        source = KITS_ROOT / name
        destination = destination_root / name
        if destination.exists() and not args.force:
            skipped.append(f"已存在，未覆盖：{destination}")
            continue
        if args.dry_run:
            changed.append(f"将复制：{source} -> {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, dirs_exist_ok=True)
        changed.append(str(destination))

    agents = """# WorkflowProject AI 开发治理规则

本项目已接入 WorkflowProject 统一能力包。

开始任何开发任务前：

1. 先读取项目已有的 `AGENTS.md`、`README.md`、架构、模块、设计规范、任务列表、测试规则和项目记忆。
2. 区分已确认事实、AI 推断和需要用户确认的问题。
3. 如果任务涉及页面、组件或新功能，先询问项目归属、模块划分、项目规范、UI 设计规范、目标端、适配范围、组件状态和验收测试。
4. 新项目先问询确认技术方案；新模块先确认是否沿用当前项目技术栈。
5. 缺少关键材料时，先列出缺口并询问用户。
6. 先形成整体规划和按优先级排列的任务列表，再开始写代码。
7. 一次只执行一条任务，完成后立即验证。
8. 根据任务需要调用产品、UI、开发或测试能力，不强制所有角色参与。
9. 代码、测试、架构、模块、设计规范或任务状态发生变化时同步项目文档。
10. 对话中持续报告当前进度、当前调度角色、使用的工作流、验证结果和下一步。

11. 简单任务直接使用 Skill，不创建子 Agent；组合任务才创建真实子 Agent。运行环境不支持时，先停下说明并询问是否降级。

统一能力包位置：`.ai/kits/`
"""
    cursor_rule = """---
description: WorkflowProject 项目级 AI 开发治理规则
alwaysApply: true
---

开始任务前，先读取项目本地规则和已有文档，并执行：

任务类型识别 -> 技术方案问询 -> 功能/组件问询（如适用） -> 项目治理检查 -> 架构与模块检查 -> 设计规范检查 -> 整体规划 -> 任务列表 -> 逐条实现 -> 逐条验证 -> 文档与记忆同步

缺少关键项目事实、技术方案或功能/组件设计信息未确认时，先向用户确认，不要直接大范围改动代码。根据实际需要使用 `.ai/kits/` 中的具体能力包。

执行分流：简单单角色任务直接调用 Skill，不创建子 Agent；组合任务由父 Agent 创建真实子 Agent。运行环境没有真实子 Agent 工具时，必须明确说明，未经用户确认不得伪装成子 Agent 协作。
"""
    if not args.no_agents:
        write_text(project / "AGENTS.md", agents, args.force, args.dry_run, changed, skipped)
    if not args.no_rules:
        write_text(project / "AI-WORKFLOW-RULES.md", agents, args.force, args.dry_run, changed, skipped)
        write_text(project / ".cursor" / "rules" / "workflowproject-governance.mdc", cursor_rule, args.force, args.dry_run, changed, skipped)

    print("\n已创建或准备创建：")
    for item in changed:
        print(f"- {item}")
    if skipped:
        print("\n已跳过：")
        for item in skipped:
            print(f"- {item}")
    print("\n安装后的启动语句：")
    print("请先执行 WorkflowProject 项目治理检查，再处理我的任务：{写下任务}")
    return 0


parser = argparse.ArgumentParser(description="安装 WorkflowProject 统一能力包")
parser.add_argument("project", help="目标代码项目路径")
parser.add_argument("--dry-run", action="store_true", help="只预览，不写入")
parser.add_argument("--force", action="store_true", help="覆盖同名能力包和规则文件")
parser.add_argument("--no-agents", action="store_true", help="不生成 AGENTS.md")
parser.add_argument("--no-rules", action="store_true", help="不生成 AI-WORKFLOW-RULES.md 和 Cursor 规则")
parser.add_argument("--create-project", action="store_true", help="目标目录不存在时创建它")
raise SystemExit(install(parser.parse_args()))
'''


README = """# WorkflowProject 统一能力包

这是从 WorkflowProject 导出的可携带开发治理包。它把项目治理、跨角色调度、产品、UI、开发和测试能力放在一个 Skill 目录中，适合复制到其他代码项目后直接安装。

这个包不是另一套需要手工维护的文档。它由 WorkflowProject 的六个独立导出包生成，源项目中的能力更新后重新导出即可。

## 一句话安装

在目标项目外执行：

```bash
python3 /路径/workflowproject-kit/scripts/install_project.py /目标代码项目
```

安装器会把能力复制到目标项目的 `.ai/kits/`，并生成或补充：

- `AGENTS.md`
- `AI-WORKFLOW-RULES.md`
- `.cursor/rules/workflowproject-governance.mdc`

已有同名文件默认不会覆盖。确认要覆盖时再加 `--force`。

## Codex 使用

本目录本身就是一个可识别的 Codex Skill，入口是 `SKILL.md`。如果要作为个人全局 Skill 使用，把整个目录复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，然后重启 Codex。

如果只想约束某个代码项目，优先运行上面的项目安装器；这样能力和规则会跟着项目走，不依赖个人机器的全局配置。

## Cursor 使用

运行安装器后，Cursor 会通过目标项目的 `.cursor/rules/workflowproject-governance.mdc` 读取项目级规则。能力正文保存在 `.ai/kits/`，可随代码项目一起提交和评审。

## 统一入口

安装后可以直接对 AI 说：

```text
请使用 WorkflowProject 先检查当前项目，再规划并执行这个需求：{需求}
```

总入口会先检查项目事实和缺口，再决定是否调度产品、UI、开发或测试能力，不会为了形式强制所有角色参与。
"""


START_HERE = """# WorkflowProject 统一能力包：从这里开始

## 导出对象

面向 AI 协作开发项目的一体化治理能力包。

## 导出时间

以 `manifest.md` 中记录的导出时间为准。

## 这个包能做什么

它会先检查目标项目的规则、架构、模块、设计规范、任务、测试和项目记忆，再按需调度产品、UI、开发和测试能力，形成从规划、实施到验证的完整链路。

## 一句话安装

```bash
python3 scripts/install_project.py /目标代码项目
```

## 一句话使用

```text
请使用 WorkflowProject 先检查当前项目，再规划并执行这个需求：{需求}
```

## 更短版本

```text
用 WorkflowProject 治理并完成：{需求}
```

## 外部自动读取配置

如果希望目标项目自动读取治理规则，运行安装器。它会生成 `AGENTS.md`、`AI-WORKFLOW-RULES.md` 和 `.cursor/rules/workflowproject-governance.mdc`。

## 执行顺序

技术方案问询 -> 项目事实检查 -> 缺口确认 -> 整体规划 -> 任务列表 -> 逐条实现 -> 逐条验证 -> 交接与验收 -> 文档和记忆同步

## Skill 与子 Agent 分流

- 单角色、单产出、无交接、无并行：当前 Agent 直接调用对应 Skill，不创建子 Agent。
- 多角色、多阶段、需要交接、联合验收、并行或用户明确要求父子 Agent：父 Agent 创建真实子 Agent。
- 运行环境没有真实子 Agent 工具：先报告限制，未经用户确认不得降级，也不得把单 Agent 顺序执行描述为子 Agent 协作。

每次执行必须声明：`单 Agent + Skill`、`父 Agent + 子 Agent`，或`单 Agent 降级模拟，不是真实子 Agent`。

## 技术方案问询

新项目开始前，AI 会先询问：

```text
1. 目标平台是什么？
2. 主要使用什么语言？
3. 是否指定框架及版本？如果没有，需要我提供候选方案吗？
4. 运行、构建和部署环境是什么？
5. 测试希望使用什么工具或方式？
```

已有项目创建新模块时，AI 会先展示识别到的技术栈，并询问是否沿用；未确认前不会安装依赖或创建模块骨架。

## 功能或组件开发问询

开发页面、组件或功能前，还会确认：

```text
项目归属：新项目还是已有项目？
模块归属：扩展哪个模块，还是需要规划新模块？
项目规范：已有规范在哪里，是否需要先建立最小规范？
UI 规范：是否已有设计系统、组件库、颜色、字体、间距和交互规则？
目标端：Web、移动端、iPad、桌面端还是多端？是否需要分屏或折叠屏适配？
组件状态：默认、加载、空、错误、禁用、选中、聚焦和异常状态如何处理？
验收方式：验收标准、测试范围和交付文档需要达到什么程度？
```

如果你暂时不知道如何制定规范，可以选择：沿用已有规范、建立本次功能的最小规范、先只输出方案暂不写代码。

## 调度原则

总入口先接管。只有在确认任务不需要跨角色协作时，才使用单一角色能力；需要多个角色协作时，先使用团队总调度。

## 输出确认格式

每次执行结束至少说明：完成内容、当前调度角色、使用工作流、验证证据、未解决问题、下一步。

## 任务结束标准

代码完成不等于任务完成。必须同时确认需求行为、相关验证、文档同步、风险和后续动作。

## 使用边界

本包提供治理方法，不替代目标项目真实架构、业务事实、设计决策和安全要求。缺少关键事实时，先询问用户。

详细安装说明见 `INSTALL.md`，Skill 入口是根目录 `SKILL.md`。
"""


INSTALL = """# 安装说明

## 推荐：安装到代码项目

```bash
python3 scripts/install_project.py /目标代码项目
```

先预览变更：

```bash
python3 scripts/install_project.py /目标代码项目 --dry-run
```

只有明确希望覆盖目标项目同名文件时才使用：

```bash
python3 scripts/install_project.py /目标代码项目 --force
```

## 作为 Codex Skill

把整个 `workflowproject-kit` 目录复制到：

```text
$CODEX_HOME/skills/workflowproject-kit/
```

没有设置 `CODEX_HOME` 时，通常使用：

```text
~/.codex/skills/workflowproject-kit/
```

复制后重启 Codex。Skill 的真正入口是根目录的 `SKILL.md`，不是 `README.md` 或 `START-HERE.md`。

## 注意

- 不需要把 WorkflowProject 全仓库复制到新项目。
- 不需要手工逐个复制六个角色包。
- 目标项目已有规则文件时，安装器默认保留原文件并报告跳过。
- 本包的 `kits/` 是由源包生成的随包资源，更新能力后应在源项目重新导出。
"""


USAGE_GUIDE = """# 使用指南

## 推荐启动方式

安装后直接输入：

```text
请使用 WorkflowProject 先检查当前项目，再规划并执行这个需求：{需求}
```

总入口会先判断当前任务属于单角色还是跨角色，再选择具体能力。你不需要手工决定先调用产品、UI、开发还是测试。

总入口还会判断是否需要创建子 Agent：简单任务只调用 Skill；组合任务才创建真实子 Agent。若运行环境不支持子 Agent，必须先告知用户并等待是否降级的确认。

## 典型链路

项目理解 -> 缺口确认 -> 架构和模块规划 -> 任务拆解 -> 逐条实现 -> 逐条验证 -> 交接与验收 -> 文档和记忆同步

## 何时主动确认

以下信息缺失时，AI 应先询问：项目目标、现有架构、模块边界、设计规范、设备范围、数据或权限边界、验收标准和发布要求；如果是页面、组件或新功能，还要问清项目归属、模块归属、UI 规范、组件状态和适配范围。

## 迭代记录

优先维护目标项目已有的项目记忆文件。没有合适文件时，可使用 `docs/ai-memory-summary.md`，不要每次把全部历史记录塞进上下文。
"""


CODEX_USAGE = """# Codex 接入

## 作为 Skill

把整个 `workflowproject-kit` 目录复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，重启 Codex 后即可由 `SKILL.md` 作为统一入口使用。

## 作为项目治理规则

在目标项目中执行：

```bash
python3 workflowproject-kit/scripts/install_project.py .
```

这会生成项目级 `AGENTS.md`，适合让规则跟着项目走。

## 使用示例

```text
请使用 WorkflowProject 检查当前项目，先给出开发规划，再按任务列表逐条实现：增加用户头像上传功能。
```
"""


CURSOR_USAGE = """# Cursor 接入

在目标项目运行：

```bash
python3 workflowproject-kit/scripts/install_project.py .
```

安装器会生成：

- `.cursor/rules/workflowproject-governance.mdc`
- `.ai/kits/`
- `AGENTS.md`

之后在 Cursor 中直接描述任务即可。规则会要求先检查项目材料、规划任务、逐条实现和逐条验证。
"""


EXAMPLE = """# 快速示例

## 用户输入

```text
请使用 WorkflowProject 检查当前项目，规划并实现一个支持邮箱登录的功能。
```

## 期望的第一轮输出

AI 应先说明：

- 当前进度和当前调度角色
- 已读取的项目材料
- 缺少的关键材料
- 是否需要产品、UI、开发或测试参与
- 整体方案和任务列表
- 需要用户确认的决策

确认后，AI 才进入逐条实现和验证，不应直接跳过项目理解阶段。
"""


MANIFEST_TEMPLATE = """# 导出清单

导出对象：WorkflowProject 统一开发治理能力包
导出时间：{exported_at}
导出方式：`python3 tools/export_unified_kit.py`

## 包含能力

{kit_list}

## 使用边界

- 本包提供 AI 项目治理和角色协作方法，不替代目标项目的真实架构、业务事实和设计决策。
- 总入口负责检查、规划、调度和验收；具体角色能力按需使用。
- 修改源项目中的能力后，应重新运行导出脚本，不直接手工修改本包中的子能力。
"""


def copy_tree(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))


def export() -> Path:
    exported_at = datetime.now().astimezone().isoformat(timespec="minutes")
    # 统一包是可重复生成的导出物，重建前清理旧内容，避免源包删除后留下过期文件。
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    kit_root = OUTPUT / "kits"
    kit_root.mkdir(parents=True, exist_ok=True)

    for kit_name in SOURCE_KITS:
        source = EXPORTS / kit_name
        if not source.is_dir():
            raise FileNotFoundError(f"缺少源能力包：{source}")
        copy_tree(source, kit_root / kit_name)

    (OUTPUT / "agents").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "scripts").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "SKILL.md").write_text(UNIFIED_SKILL.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "agents" / "openai.yaml").write_text(OPENAI_YAML.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "scripts" / "install_project.py").write_text(INSTALLER.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "scripts" / "install_project.py").chmod(0o755)
    (OUTPUT / "START-HERE.md").write_text(START_HERE.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "README.md").write_text(README.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "INSTALL.md").write_text(INSTALL.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "usage-guide.md").write_text(USAGE_GUIDE.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "integrations").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "integrations" / "codex-usage.md").write_text(CODEX_USAGE.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "integrations" / "cursor-usage.md").write_text(CURSOR_USAGE.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "examples").mkdir(parents=True, exist_ok=True)
    (OUTPUT / "examples" / "quick-start-example.md").write_text(EXAMPLE.rstrip() + "\n", encoding="utf-8")
    kit_list = "\n".join(f"- `{name}/`：{label}" for name, label in [
        ("project-governance-kit", "项目治理检查"),
        ("team-orchestration-kit", "跨角色总调度"),
        ("product-manager-kit", "产品经理能力"),
        ("ui-designer-kit", "UI 设计能力"),
        ("developer-kit", "开发治理能力"),
        ("tester-kit", "测试与验收能力"),
    ])
    (OUTPUT / "manifest.md").write_text(MANIFEST_TEMPLATE.format(exported_at=exported_at, kit_list=kit_list), encoding="utf-8")
    (OUTPUT / "AGENTS.md").write_text(AGENTS_CONTENT.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "AI-WORKFLOW-RULES.md").write_text(AGENTS_CONTENT.rstrip() + "\n", encoding="utf-8")
    (OUTPUT / "cursor-rule-template.mdc").write_text(CURSOR_RULE.rstrip() + "\n", encoding="utf-8")
    return OUTPUT


def main() -> int:
    parser = argparse.ArgumentParser(description="生成可复制安装的 WorkflowProject 统一能力包")
    parser.parse_args()
    output = export()
    print(f"已生成：{output}")
    print(f"包含能力包：{', '.join(SOURCE_KITS)}")
    print("安装示例：python3 workflowproject-kit/scripts/install_project.py /目标代码项目")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
