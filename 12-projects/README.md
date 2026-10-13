# 项目

具体任务项目放在这里。

## 先看项目索引

项目变多以后，不要先翻目录，先看：

```text
12-projects/project-index.md
```

它会列出：

- 每个项目是干什么的。
- 当前状态是什么。
- 下一步应该做什么。
- 下次如何启动这个项目。

项目索引由脚本自动生成：

```bash
python3 tools/generate_project_index.py
```

运行下面命令时也会同步刷新：

```bash
python3 tools/refresh_maps.py
```

创建新项目时，优先使用：

```bash
python3 tools/create_project.py product-manager my-task --type real-cases
```

默认路径：

```text
12-projects/{角色}/{项目类型}/{项目名}/
```

项目类型：

```text
capability-building   能力建设项目，用于建设 workflow、template、scorecard、知识体系
real-cases            真实使用项目，用于处理具体业务需求
experiments           实验探索项目，用于验证不稳定想法
```

如果需要指定项目根目录，使用：

```bash
python3 tools/create_project.py mixed ai-template-tool --output 12-projects/mixed/real-cases/ai-template-tool
```

`--output` 指定的是项目根目录，内部结构仍然固定。

推荐每个项目使用以下结构：

```text
project-name/
├── README.md
├── 00-progress/
├── 01-inputs/
├── 02-analysis/
├── 03-prompts/
├── 04-outputs/
├── 05-review/
└── 06-lessons/
```

当项目产物具备复用价值时，再提升到全局模板、案例或知识库。
