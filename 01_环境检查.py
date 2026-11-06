# -*- coding: utf-8 -*-
"""环境自检：确认 Python 和常用库都装好了，顺便画一张中文图表。"""

import sys
import platform

print("=" * 46)
print("Python 版本 :", sys.version.split()[0])
print("解释器路径  :", sys.executable)
print("操作系统    :", platform.system(), platform.release())
print("=" * 46)

import numpy as np
import pandas as pd
import matplotlib

matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
matplotlib.rcParams["axes.unicode_minus"] = False
import matplotlib.pyplot as plt

print(f"numpy       : {np.__version__}")
print(f"pandas      : {pd.__version__}")
print(f"matplotlib  : {matplotlib.__version__}")
print("=" * 46)

# 一元二次方程 y = x^2 - 4x + 3 的图像
x = np.linspace(-1, 5, 200)
y = x**2 - 4 * x + 3

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, y, linewidth=2, color="#c0392b", label="y = x² − 4x + 3")
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.grid(alpha=0.3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("环境检查通过 · 中文显示正常")
ax.legend()

out = "环境检查结果.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"\n图表已保存: {out}")
print("环境检查完成，可以开始写作业了。")
