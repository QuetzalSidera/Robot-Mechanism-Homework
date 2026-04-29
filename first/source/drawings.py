from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


HOMEWORK_DIR = Path(__file__).resolve().parents[1]
RESULT_DIR = HOMEWORK_DIR / "result"


def configure_fonts():
    font_candidates = [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]
    for font_path in font_candidates:
        path = Path(font_path)
        if path.exists():
            font_manager.fontManager.addfont(str(path))
            font_name = font_manager.FontProperties(fname=str(path)).get_name()
            plt.rcParams["font.family"] = [font_name]
            plt.rcParams["axes.unicode_minus"] = False
            return
    plt.rcParams["axes.unicode_minus"] = False


def setup_axes(title: str):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(title, fontsize=16)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.35)
    return fig, ax


def draw_q5():
    fig, ax = setup_axes("第5题：运动旋量轴线示意")
    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-2.2, 2.2)

    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.annotate("", xy=(4.3, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(0, 2.0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(4.35, -0.15, "x", fontsize=12)
    ax.text(0.08, 2.02, "z", fontsize=12)

    x = np.linspace(-1.2, 4.2, 100)
    y = np.full_like(x, -1.0)
    ax.plot(x, y, color="#2563eb", linewidth=3, label=r"axis: $(x,y,z)=(0,-1,0)+t(1,0,0)$")
    ax.scatter([0], [-1], color="#b91c1c", s=50, zorder=3)
    ax.text(0.08, -0.82, r"$r=(0,-1,0)$", color="#b91c1c", fontsize=12)
    ax.annotate(r"$\omega=(1,0,0)$", xy=(3.2, -1.0), xytext=(2.3, -1.55),
                arrowprops=dict(arrowstyle="->", color="#2563eb"), color="#2563eb")

    ax.legend(loc="lower right")
    fig.tight_layout()
    RESULT_DIR.mkdir(exist_ok=True)
    fig.savefig(RESULT_DIR / "q5_axis.png", dpi=180)
    plt.close(fig)


def draw_q8():
    fig, ax = setup_axes("第8题：过 P 的互易力旋量族")
    ax.set_xlim(-2.2, 4.2)
    ax.set_ylim(-1.2, 3.4)

    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.annotate("", xy=(4.0, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(0, 3.1), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.text(4.02, -0.15, "x", fontsize=12)
    ax.text(0.08, 3.12, "y", fontsize=12)

    ax.fill_between([-2.1, 4.0], 0, 0.02, color="#e5e7eb", alpha=0.8)
    ax.text(3.15, 0.18, r"$z=0$ plane", color="#6b7280", fontsize=11)

    p = np.array([0.0, 1.0])
    ax.scatter([p[0]], [p[1]], color="black", s=40, zorder=3)
    ax.text(p[0] + 0.08, p[1] + 0.08, r"$P(0,1,0)$", fontsize=12)

    angles = np.deg2rad([-70, -35, 0, 30, 65])
    for angle in angles:
        direction = np.array([np.cos(angle), np.sin(angle)])
        end = p + 2.2 * direction
        ax.annotate("", xy=end, xytext=p, arrowprops=dict(arrowstyle="->", lw=2, color="#b91c1c"))

    ax.text(1.1, 2.6, "all force lines pass through P\nand stay in the z=0 plane",
            color="#b91c1c", fontsize=11)
    fig.tight_layout()
    RESULT_DIR.mkdir(exist_ok=True)
    fig.savefig(RESULT_DIR / "q8_force_family.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    configure_fonts()
    draw_q5()
    draw_q8()
