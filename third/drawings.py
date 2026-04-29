from pathlib import Path


ROOT = Path(__file__).resolve().parent


def svg_header(width: int, height: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        '<defs>'
        '<marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,0 L8,4 L0,8 Z" fill="#333"/>'
        '</marker>'
        '</defs>'
    )


def svg_footer() -> str:
    return "</svg>"


def circle(x: int, y: int, r: int = 7, color: str = "#111") -> str:
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


def label(x: int, y: int, text: str, size: int = 18, color: str = "#111") -> str:
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-family="Arial">{text}</text>'


def line(x1: int, y1: int, x2: int, y2: int, color: str = "#333", width: int = 3) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>'


def draw_3rrr() -> None:
    width, height = 720, 420
    parts = [svg_header(width, height), '<rect width="100%" height="100%" fill="white"/>']
    parts.append(label(24, 34, "方案一：3-RRR 平面并联机构", 24))

    b1, b2, b3 = (110, 310), (610, 310), (360, 120)
    p1, p2, p3 = (250, 250), (470, 250), (360, 180)
    m1, m2, m3 = (170, 260), (550, 260), (360, 150)

    base_color = "#2563eb"
    platform_color = "#b91c1c"
    leg_color = "#333"

    parts.append(line(*b1, *b2, base_color, 4))
    parts.append(line(*b2, *b3, base_color, 4))
    parts.append(line(*b3, *b1, base_color, 4))
    parts.append(label(70, 345, "机架", 18, base_color))

    parts.append(line(*p1, *p2, platform_color, 4))
    parts.append(line(*p2, *p3, platform_color, 4))
    parts.append(line(*p3, *p1, platform_color, 4))
    parts.append(label(500, 210, "动平台", 18, platform_color))

    for a, b, c in [(b1, m1, p1), (b2, m2, p2), (b3, m3, p3)]:
        parts.append(line(*a, *b, leg_color, 4))
        parts.append(line(*b, *c, leg_color, 4))
        parts.append(circle(*a))
        parts.append(circle(*b))
        parts.append(circle(*c))
        parts.append(label(b[0] + 8, b[1] - 8, "R", 16))
        parts.append(label(a[0] + 8, a[1] - 8, "R", 16))
        parts.append(label(c[0] + 8, c[1] - 8, "R", 16))

    parts.append(label(180, 390, "三条支链均为 R-R-R，机构工作于同一平面", 18))
    parts.append(svg_footer())
    (ROOT / "q1_3rrr.svg").write_text("".join(parts), encoding="utf-8")


def draw_3rpr() -> None:
    width, height = 720, 440
    parts = [svg_header(width, height), '<rect width="100%" height="100%" fill="white"/>']
    parts.append(label(24, 34, "方案二：3-RPR 平面并联机构", 24))

    b1, b2, b3 = (120, 330), (600, 330), (360, 120)
    p1, p2, p3 = (250, 255), (470, 255), (360, 190)

    base_color = "#2563eb"
    platform_color = "#b91c1c"
    leg_color = "#333"

    parts.append(line(*b1, *b2, base_color, 4))
    parts.append(line(*b2, *b3, base_color, 4))
    parts.append(line(*b3, *b1, base_color, 4))
    parts.append(label(70, 365, "机架", 18, base_color))

    parts.append(line(*p1, *p2, platform_color, 4))
    parts.append(line(*p2, *p3, platform_color, 4))
    parts.append(line(*p3, *p1, platform_color, 4))
    parts.append(label(500, 220, "动平台", 18, platform_color))

    for base, plat, offset in [(b1, p1, -1), (b2, p2, 1), (b3, p3, 0)]:
        mx = (base[0] + plat[0]) // 2
        my = (base[1] + plat[1]) // 2
        parts.append(line(base[0], base[1], mx - 24, my - 10 * offset, leg_color, 4))
        parts.append(f'<rect x="{mx - 24}" y="{my - 14}" width="48" height="28" fill="#f8fafc" stroke="#333" stroke-width="3"/>')
        parts.append(label(mx - 8, my + 6, "P", 18))
        parts.append(line(mx + 24, my + 10 * offset, plat[0], plat[1], leg_color, 4))
        parts.append(circle(*base))
        parts.append(circle(*plat))
        parts.append(label(base[0] + 8, base[1] - 8, "R", 16))
        parts.append(label(plat[0] + 8, plat[1] - 8, "R", 16))

    parts.append(label(150, 405, "三条支链均为 R-P-R，中间移动副位于工作平面内", 18))
    parts.append(svg_footer())
    (ROOT / "q1_3rpr.svg").write_text("".join(parts), encoding="utf-8")


if __name__ == "__main__":
    draw_3rrr()
    draw_3rpr()
