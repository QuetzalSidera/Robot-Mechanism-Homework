# AGENT.md

## 项目目标

本项目的目的，是让 AI Agent 读取机器人机构学作业题图，完成题目求解、机构分析、必要的机械简图绘制，以及结果文档整理。

## 推荐 Agent 能力要求

执行本项目的 Agent 至少应具备以下能力：

1. **OCR / 图像理解能力**：能够直接读取 `png` 题图中的中文题面、公式和示意图。
2. **数学与机构学推理能力**：能够处理自由度分析、旋量、互易、Plucker 坐标、机构综合等内容。
3. **代码生成能力**：能够为需要图示的题目编写 Python 绘图脚本。
4. **文档整理能力**：能够把结果规范写入各作业目录下的 `answer.md`。

推荐优先使用带图像输入能力的 Agent，例如：

1. `Codex CLI` 。
2. 其他具备 OCR 和多模态理解能力、且能直接修改本地工作区文件的 Agent。

## 目录约定

1. `first/`、`second/`、`third/`、`forth/` 分别对应第 1、2、3、4 次作业。
2. 每个作业目录内的题目图片按 `{index}.png` 命名。
3. 每个作业目录内应放置：
   - 根目录：仅放题目图片，如 `1.png`、`2.png`。
   - `source/`：该次作业相关的 Python 源码目录。
   - `source/requirements.txt`：该次作业所需的 Python 依赖。
   - `source/README.md`：该次作业源码侧的运行说明。
   - `source/*.py`：若该次作业需要补机械简图，则在此提供 Python 绘图代码。
   - `result/answer.md`：该次作业的正式作答。
   - `result/*`：绘图脚本生成并在 `answer.md` 中引用的图片。

## AI Agent 工作流程

1. 先扫描仓库，识别每次作业目录及图片页数。
2. 逐页读取题图，整理题目内容，不要跳题。
3. 先解封闭题，再处理开放题和综合题。
4. 若题目要求“画图”“图示”“机构简图”“轴线位置示意”，必须生成对应绘图代码。
5. 绘图代码优先使用 `matplotlib` 输出 `png`，视角以清晰表达机构拓扑关系为准，不强求 3D 视角。
6. 若使用第三方包，必须把虚拟环境创建在对应作业的 `source/.venv` 下，不要放在项目根目录，也不要污染系统 Python。
7. 运行绘图脚本，确认输出图片真实生成到 `result/`，再插入 `result/answer.md`。
8. 只在对应作业目录下写该作业的结果，不把四次作业混写到同一文件。

## 启动与使用方式

若使用 `Codex CLI`，推荐流程如下：

```bash
git clone <你的仓库地址>
cd RobotMechanismHomework
codex --full-auto --sandbox workspace-write "读取 first/ second/ third/ forth 下的题图，完成每次作业，并把答案写到各目录的 result/answer.md；若题目需要图示，则在各作业目录的 source/ 中编写 matplotlib 绘图代码，在 source/.venv 中安装依赖，运行后把生成的图片写入 result/。"
```

如果希望在启动时显式附加图片，可使用：

```bash
codex --full-auto --sandbox workspace-write \
  --image first/1.png \
  --image first/2.png \
  --image second/1.png \
  --image third/1.png \
  --image third/2.png \
  --image forth/1.png \
  --image forth/2.png \
  "根据这些题图完成机器人机构学作业，结果分别写入各目录。"
```

如果希望在交互模式下逐步处理，也可直接运行：

```bash
codex --sandbox workspace-write
```

进入会话后再输入任务说明。

## 解题约束

1. 计算题应给出关键推导，不只写结论。
2. 自由度、旋量、互易、约束分析应明确所用结论或公式。
3. 开放题允许合理假设，但必须在文档开头写清楚假设。
4. 机构综合题优先给出课程语境下常见、可解释的标准机构，不要凭空造复杂结构。

## 修改约束

1. 不要改动题目图片。
2. 不要删除用户原有资料，除非这些文件是本次 Agent 新生成且已被更合理的结果替代。
3. 新增文件命名应直接表达用途，避免模糊名称。

## 交付标准

1. 每个作业目录均有可直接阅读的 `result/answer.md`。
2. 所有需要图示的题目均有对应 `source/` 下的 `Python` 绘图代码与已生成图片。
3. 每个作业目录的 `source/` 下均有独立 `README.md`。
4. 根目录保留 `README.md` 和本文件，便于后续 Agent 继续工作。
