# 机器人机构学作业 Agent 项目

本项目用于让 AI Agent 基于题目图片完成机器人机构学作业。仓库中包含三次作业，题目图片分别放在 `first/`、`second/`、`third/` 目录下，文件名按 `{index}.png` 编排。

## 项目目的

目标不是只做 OCR，而是让 Agent 完成完整作业流程：

1. 读取题图。
2. 理解题意并完成求解。
3. 对需要图示的题目生成机械简图。
4. 输出结构化答案文档。

## 当前目录结构

```text
homework1/
├── AGENT.md
├── README.md
├── first/
│   ├── 1.png
│   ├── 2.png
│   ├── answer.md
│   ├── drawings.py
│   ├── q5_axis.svg
│   └── q8_force_family.svg
├── second/
│   ├── 1.png
│   └── answer.md
└── third/
    ├── 1.png
    ├── 2.png
    ├── answer.md
    ├── drawings.py
    ├── q1_3rrr.svg
    └── q1_3rpr.svg
```

## AI 应如何操作本项目

1. 从根目录读取 `AGENT.md`。
2. 扫描 `first/`、`second/`、`third/` 下的题目图片。
3. 针对每次作业，在对应目录内维护 `answer.md`。
4. 若某题需要图示，则在对应目录内新增或更新 `drawings.py`。
5. 运行绘图脚本生成 `svg` 图片，并在 `answer.md` 中引用。

## 推荐工作方式

1. 先做题目内容识别，再统一规划解答结构。
2. 封闭题直接求解。
3. 对存在解释空间的题目，在答案开头写“说明与假设”。
4. 对自由度分析、约束旋量分析、机构综合题，优先给出课程常用结论与标准机构类型。
5. 交付前检查文档引用的图片是否真实存在。

## 绘图说明

本项目中的机械简图由 Python 脚本生成。为减少环境依赖，默认优先使用 Python 标准库直接输出 `svg` 文件，而不是依赖 `matplotlib`、`Pillow` 等第三方库。

运行示例：

```bash
python3 first/drawings.py
python3 third/drawings.py
```

## 交付要求

1. 每次作业的答案必须放在对应文件夹之下。
2. 需要图示的题目必须提供绘图 Python 代码。
3. 绘图代码必须运行过，结果图需插入答案文档。
4. 不要把多次作业的结果混在一个总文件里。
