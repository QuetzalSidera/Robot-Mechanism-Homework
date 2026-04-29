from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Circle, Polygon


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


def joint(ax, x, y, label_text=None, color="#111111", radius=0.08):
    ax.add_patch(Circle((x, y), radius, color=color, zorder=3))
    if label_text:
        ax.text(x + 0.08, y + 0.08, label_text, fontsize=10)


def setup(title: str):
    fig, ax = plt.subplots(figsize=(8, 5.2))
    ax.set_title(title, fontsize=16)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def draw_3rrr():
    fig, ax = setup("方案一：3-RRR 平面并联机构")

    base = [(0.6, 0.6), (5.4, 0.6), (3.0, 3.3)]
    platform = [(1.9, 1.45), (4.1, 1.45), (3.0, 2.25)]
    mids = [(1.2, 1.1), (4.8, 1.1), (3.0, 2.9)]

    ax.add_patch(Polygon(base, closed=True, facecolor="#93c5fd", edgecolor="#2563eb", linewidth=3, alpha=0.35))
    ax.add_patch(Polygon(platform, closed=True, facecolor="#fca5a5", edgecolor="#b91c1c", linewidth=3, alpha=0.35))
    ax.text(0.2, 0.2, "机架", color="#2563eb", fontsize=12)
    ax.text(4.35, 2.35, "动平台", color="#b91c1c", fontsize=12)

    for b, m, p in zip(base, mids, platform):
        ax.plot([b[0], m[0]], [b[1], m[1]], color="#333333", linewidth=3)
        ax.plot([m[0], p[0]], [m[1], p[1]], color="#333333", linewidth=3)
        joint(ax, *b, "R")
        joint(ax, *m, "R")
        joint(ax, *p, "R")

    ax.text(1.1, -0.2, "三条支链均为 R-R-R，采用平面视角表达拓扑关系", fontsize=11)
    ax.plot([], [], "ko", label="R副")
    ax.legend(loc="upper right", frameon=True)
    fig.tight_layout()
    RESULT_DIR.mkdir(exist_ok=True)
    fig.savefig(RESULT_DIR / "q1_3rrr.png", dpi=180)
    plt.close(fig)


def draw_3rpr():
    fig, ax = setup("方案二：3-RPR 平面并联机构（俯视）")

    r_base = 5.0
    r_platform = 2.1
    theta = np.array([0, 2 * np.pi / 3, 4 * np.pi / 3])
    theta_offset = np.pi / 6
    slider_ratio = np.array([0.35, 0.55, 0.75])

    base = np.column_stack((r_base * np.cos(theta), r_base * np.sin(theta)))
    platform = np.column_stack((r_platform * np.cos(theta + theta_offset), r_platform * np.sin(theta + theta_offset)))
    sliders = base + (platform - base) * slider_ratio[:, None]

    ax.add_patch(Polygon(base, closed=True, facecolor="#93c5fd", edgecolor="#2563eb", linewidth=3, alpha=0.35, label="机架（定平台）"))
    ax.add_patch(Polygon(platform, closed=True, facecolor="#fca5a5", edgecolor="#b91c1c", linewidth=3, alpha=0.35, label="动平台"))

    for i, (a, c, b) in enumerate(zip(base, sliders, platform), start=1):
        ax.plot([a[0], c[0]], [a[1], c[1]], color="#333333", linewidth=2.6)
        ax.plot([c[0], b[0]], [c[1], b[1]], color="#333333", linewidth=2.6)

        direction = b - a
        direction = direction / np.linalg.norm(direction)
        ax.arrow(
            c[0],
            c[1],
            0.75 * direction[0],
            0.75 * direction[1],
            head_width=0.18,
            head_length=0.24,
            color="#2563eb",
            length_includes_head=True,
            zorder=2,
        )

        joint(ax, a[0], a[1], f"A{i}", color="#dc2626", radius=0.11)
        joint(ax, c[0], c[1], None, color="#2563eb", radius=0.11)
        joint(ax, b[0], b[1], f"B{i}", color="#16a34a", radius=0.11)

    ax.plot([], [], "o", color="#dc2626", label="R副（定平台）")
    ax.plot([], [], "o", color="#2563eb", label="P副（移动副）")
    ax.plot([], [], "o", color="#16a34a", label="R副（动平台）")
    ax.plot([], [], color="#2563eb", linewidth=2.0, label="箭头表示P副移动方向")

    ax.grid(True, linestyle="--", alpha=0.35)
    ax.set_xlim(-6.3, 6.3)
    ax.set_ylim(-5.8, 5.8)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend(loc="upper right", frameon=True)
    fig.tight_layout()
    RESULT_DIR.mkdir(exist_ok=True)
    fig.savefig(RESULT_DIR / "q1_3rpr.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    configure_fonts()
    draw_3rrr()
    draw_3rpr()
