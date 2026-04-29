# first/source

本目录存放第 1 次作业相关的 Python 源码与依赖。

## 内容

1. `drawings.py`：用于生成第 5 题和第 8 题示意图。
2. `requirements.txt`：本目录绘图脚本所需依赖。
3. `.venv/`：如需安装第三方包，应创建在本目录下。

## 运行方法

```bash
cd first/source
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python drawings.py
```

运行完成后，输出图片应写入 `../result/`，供 `../result/answer.md` 引用。
