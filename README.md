# 机器人机构学作业 Agent 项目

本项目用于让 AI Agent 基于题目图片完成机器人机构学作业。仓库中包含四次作业，题目图片分别放在 `first/`、`second/`、`third/`、`forth/`
目录下，文件名按 `{index}.png` 编排。

## 前置要求

这个项目需要能够处理纯图像的 Agent。推荐的 Agent 至少应具备：

1. OCR 或图像理解能力，能够读取题目图片中的中文、公式和结构图。
2. 本地代码执行能力，能够运行 Python 绘图脚本。
3. 工作区写入能力，能够直接生成 `result/answer.md`、`source/*.py` 和输出图片。
4. 数学推导与机构学分析能力，能够处理旋量、自由度、约束分析与机构综合。

推荐使用带图像输入能力的 `Codex CLI`，因为它既能读图，也能直接在本地仓库中改文件。

如果 Agent 本身不具备稳定的 OCR / 图像理解能力，则应接入相应的视觉 MCP。一个可选方案是智谱视觉 MCP：

- 文档：<https://docs.bigmodel.cn/cn/coding-plan/mcp/vision-mcp-server>

## 快速开始

推荐按下面 3 步使用本项目：

1. 将作业题目截图放在对应目录下。
   例如：`first/1.png`、`first/2.png`、`second/1.png`、`third/1.png`、`third/2.png`、`forth/1.png`、`forth/2.png`。
2. 启动 Agent，并明确告诉 Agent 按照本项目的目录约定、`AGENT.md` 与 `README.md` 要求完成对应作业。
3. 在对应作业目录的 `result/` 下查找结果。
   例如：`first/result/answer.md`、`third/result/q1_3rrr.png`。

示例命令：

```bash
git clone https://github.com/QuetzalSidera/Robot-Mechanism-Homework.git
cd RobotMechanismHomework
codex "读取 first/ second/ third/ forth 下的题图，完成机器人机构学作业；每次作业的答案写入对应目录 result/answer.md；若需要机械简图，则在各作业目录的 source/ 中编写 matplotlib 绘图代码，在 source/.venv 中安装依赖、运行并把输出图片写入 result/。"
```

如果你使用的 Agent 不自带 OCR / 图像理解，可以先为客户端接入视觉 MCP，再让 Agent 工作。以智谱视觉 MCP 为例，官方文档给出的
Claude Code 一键安装命令是：

```bash
claude mcp add -s user zai-mcp-server --env Z_AI_API_KEY=your_api_key -- npx -y "@z_ai/mcp-server"
```

该方案需要：

1. `Node.js 18+`
2. 智谱 `API Key`
3. 兼容 MCP 的客户端

接入完成后，再按本项目要求把题图放在本地目录中，并通过对话让 Agent 读取这些图片路径。

如果希望在启动时就把题图明确传给 Agent，可使用：

```bash
codex --full-auto --sandbox workspace-write \
  --image first/1.png \
  --image first/2.png \
  --image second/1.png \
  --image third/1.png \
  --image third/2.png \
  --image forth/1.png \
  --image forth/2.png \
  "根据这些题图完成作业，并整理输出。"
```

如果你更希望以交互方式逐步推进，可运行：

```bash
codex --sandbox workspace-write
```

然后在交互会话中输入任务要求。

## 项目目的

目标不是只做 OCR，而是让 Agent 完成完整作业流程：

1. 读取题图。
2. 理解题意并完成求解。
3. 对需要图示的题目生成机械简图。
4. 输出结构化答案文档。

## 当前目录结构

```text
RobotMechanismHomework/
├── AGENT.md
├── README.md
├── first/
│   ├── 1.png
│   ├── 2.png
│   ├── source/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── drawings.py
│   └── result/
│       ├── answer.md
│       ├── q5_axis.png
│       └── q8_force_family.png
├── second/
│   ├── 1.png
│   ├── source/
│   │   ├── README.md
│   │   └── requirements.txt
│   └── result/
│       └── answer.md
├── third/
    ├── 1.png
    ├── 2.png
    ├── source/
    │   ├── README.md
    │   ├── requirements.txt
    │   └── drawings.py
    └── result/
        ├── answer.md
        ├── q1_3rrr.png
        └── q1_3rpr.png
└── forth/
    ├── 1.png
    ├── 2.png
    ├── source/
    │   ├── README.md
    │   └── requirements.txt
    └── result/
        └── answer.md
```

## AI 应如何操作本项目

1. 从根目录读取 `AGENT.md`。
2. 扫描 `first/`、`second/`、`third/`、`forth/` 下的题目图片。
3. 针对每次作业，在对应目录内维护 `result/answer.md`。
4. 若某题需要图示，则在对应目录内新增或更新 `source/` 下的绘图代码。
5. 运行绘图脚本后，将输出图片写入 `result/`，并在 `result/answer.md` 中引用。

建议 Agent 首次进入仓库后，先阅读根目录的 [AGENT.md](/Users/qianshuang/Desktop/homework1/AGENT.md) 再开始工作。

## 推荐工作方式

1. 先做题目内容识别，再统一规划解答结构。
2. 封闭题直接求解。
3. 对存在解释空间的题目，在答案开头写“说明与假设”。
4. 对自由度分析、约束旋量分析、机构综合题，优先给出课程常用结论与标准机构类型。
5. 交付前检查文档引用的图片是否真实存在。

## 绘图说明

本项目中的机械简图优先由 `matplotlib` 生成，并输出为 `png` 文件。视角以清晰表达机构拓扑关系为准，不强求使用 3D 视角。

若使用第三方包，必须先创建项目内虚拟环境，再安装依赖。

运行示例：

```bash
cd first/source
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python drawings.py

cd ../../third/source
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python drawings.py
```

## 交付要求

1. 每次作业的题目图片必须放在该作业根目录之下。
2. 需要图示的题目必须提供绘图 Python 代码。
3. 绘图代码必须放在对应作业目录的 `source/` 下。
4. `requirements.txt` 必须放在对应作业目录的 `source/` 下。
5. 若使用第三方包，虚拟环境必须放在对应作业目录的 `source/.venv` 下。
6. 作答文档与输出图片必须放在对应作业目录的 `result/` 下。
7. 每个 `source/` 下都必须提供一个独立 `README.md`，说明如何运行。
8. 绘图代码必须运行过，结果图需插入答案文档。
9. 不要把多次作业的结果混在一个总文件里。
