# 复盘经验

来源项目：

```text
12-projects/mixed/capability-building/workflowproject-framework-bootstrap/06-lessons/lessons.md
```

## 关键经验

- 先搭建治理规范比先写大量模板更重要。
- 全局目录应保持稳定，具体任务应先放在 `12-projects/` 中运行。
- template、prompt、output、example 必须明确区分。
- meta templates 是项目的关键能力，因为用户并不总是知道如何从材料生成优秀模板。
- XMind 导图能显著降低文档框架的理解成本。
- quick-start、创建项目脚本、进度汇报规则和项目完成检查表，比继续扩展目录更能降低真实使用成本。
- 执行过程中必须记录“当前进度、调度角色、使用工作流、使用模板、下一步”。

## 可复用模式

```text
先做系统和治理
-> 再做通用工作流
-> 再做标准
-> 再做 meta templates
-> 再用一个真实项目验证框架
-> 补低成本入口和进度记录
-> 最后从项目中沉淀案例和知识
```

## 反模式

- 直接在全局目录中完成所有具体任务。
- 把未经评审的输出放入案例库。
- 把单次业务内容写进通用模板。
- README 承担过多细节规则。
- 只建目录，不定义晋级和评审规则。
- 只保存最终输出，不记录执行过程和调度角色。
- 过早补大量角色模板，但没有真实项目验证。

## 后续改进

- 已在正式案例基础上提炼框架搭建模式到 `10-knowledge-base/patterns/framework-bootstrap-pattern.md`。
- 已提炼框架启动提示词模板到 `06-templates/common/framework-bootstrap-template.md`。
- 已新增项目运行助手到 `06-templates/meta/project-runner.md`。
- 已新增全部导图刷新脚本 `tools/refresh_maps.py`。
- 已新增可解释项目运行助手到 `06-templates/meta/explainable-project-runner.md`。
- 已新增执行前说明规则、结果报告规则和理解检查表。
- 后续通过真实产品、开发、UI 项目补齐角色模板。
- 为每个 active 角色建立独立评分表。
