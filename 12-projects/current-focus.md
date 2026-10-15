# 当前工作区

这不是全部项目清单，只回答：现在应该先看什么、继续什么、暂时不要碰什么。

## 当前主线

### 1. 项目治理框架

当前主线已经从“继续细化角色”调整为“治理真实代码项目”。先看：

```text
00-system/project-governance-model.md
04-workflows/common/project-governance-workflow.md
14-exports/project-governance-kit/START-HERE.md
```

安装到真实代码项目：

```bash
python3 tools/install_project_kits.py /你的代码项目路径 --dry-run
python3 tools/install_project_kits.py /你的代码项目路径
```

### 2. 真实项目验证

下一步应找一个真实代码项目，验证 `project-governance-kit` 是否能在写代码前完成：

```text
项目规则检查
架构和模块检查
设计规范检查
任务列表生成
逐条执行和验证
文档同步
```

### 3. 角色能力维护

产品、UI、开发、测试角色已经作为可选专业能力保留。后续只有在真实验证中出现专业缺口或 badcase 时，才回到对应角色项目优化，不再继续无目标地扩展角色细分。

## 暂时不要做

- 不要重新打开所有已经完成的角色能力建设项目。
- 不要为了项目数量继续新建角色工作流。
- 不要把每一次真实需求都创建成能力建设项目。
- 不要删除历史项目；需要清理时先归档并保留索引。

## 三个入口

| 你想知道什么 | 先看哪里 |
| --- | --- |
| 当前应该做什么 | `12-projects/current-focus.md` |
| 有哪些可复用能力 | `12-projects/asset-index.md` |
| 所有历史和建设项目 | `12-projects/project-index.md` |

## 当前项目选择规则

- 建设或修改通用能力：使用 `capability-building`。
- 验证一个真实需求或真实项目：使用 `real-cases`。
- 验证不稳定想法：使用 `experiments`。
- 只是日常使用已完成能力：直接使用导出包或全局工作流，不新建能力建设项目。
