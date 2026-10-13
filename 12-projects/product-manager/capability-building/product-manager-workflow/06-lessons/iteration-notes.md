# 迭代记录

## 本次为什么重做

上一版产品经理工作流已经可用，但它默认用户已经能提供相对清晰的输入。

用户随后指出：

```text
生成 input 本身也需要成本。
```

因此本次重新执行，是为了验证新加入的 `idea-to-input-generator` 能否把一句模糊描述转换成标准 input。

## 本次链路变化

上一版链路：

```text
原始需求
-> 输入分析
-> 正式提示词
-> 输出
-> 评审
-> 沉淀
```

新版链路：

```text
模糊想法
-> idea-to-input-generator
-> 标准 input
-> 输入分析
-> 正式提示词
-> 输出
-> 评审
-> 沉淀
```

## 本次验证结论

`idea-to-input-generator` 是必要的。

它让用户不必一开始就写完整 input，只需要先说出想法，AI 就能帮助整理成后续流程可用的标准输入。

## 新发现的痛点

### 痛点 1：项目启动应默认支持“想法模式”

现在快速开始已经补充了想法转输入，但项目创建脚本仍然只创建空目录，不会提示用户进入想法模式。

后续可考虑：

```text
tools/create_project.py 支持 --idea 参数
```

### 痛点 2：标准 input 生成后还缺少自动检查

目前 input 是否合格主要靠人工判断。

后续可考虑增加：

```text
06-templates/meta/input-reviewer.md
```

或：

```text
11-evaluations/output-scorecards/input-quality-scorecard.md
```

### 痛点 3：用户需要知道“现在是想法阶段还是执行阶段”

后续可在 React 控制台里增加项目阶段：

```text
想法整理
输入分析
提示词生成
输出生成
评审
沉淀
```
