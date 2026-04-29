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
        '<marker id="bluearrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,0 L8,4 L0,8 Z" fill="#1d4ed8"/>'
        '</marker>'
        '<marker id="redarrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        '<path d="M0,0 L8,4 L0,8 Z" fill="#b91c1c"/>'
        '</marker>'
        '</defs>'
    )


def svg_footer() -> str:
    return "</svg>"


def draw_q5() -> None:
    width, height = 640, 420
    ox, oy = 160, 250
    scale = 70

    def pt(x: float, y: float) -> tuple[float, float]:
        return ox + x * scale, oy - y * scale

    x1, y1 = pt(-1.3, -1)
    x2, y2 = pt(4.2, -1)
    px, py = pt(0, -1)
    hx, hy = pt(3.7, 0.8)
    vx, vy = pt(0, 2.0)

    parts = [svg_header(width, height)]
    parts.append('<rect width="100%" height="100%" fill="white"/>')
    parts.append('<text x="24" y="34" font-size="24" font-family="Arial">第5题：运动旋量轴线示意</text>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{hx}" y2="{hy}" stroke="#333" stroke-width="2.5" marker-end="url(#arrow)"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{vx}" y2="{vy}" stroke="#333" stroke-width="2.5" marker-end="url(#arrow)"/>')
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1d4ed8" stroke-width="4" marker-end="url(#bluearrow)"/>')
    parts.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#b91c1c"/>')
    parts.append(f'<text x="{hx + 8}" y="{hy + 2}" font-size="18" font-family="Arial">x</text>')
    parts.append(f'<text x="{vx - 10}" y="{vy - 10}" font-size="18" font-family="Arial">z</text>')
    parts.append(f'<text x="{px + 10}" y="{py - 10}" font-size="18" font-family="Arial">r=(0,-1,0)</text>')
    parts.append(f'<text x="{x2 - 20}" y="{y2 - 12}" font-size="18" fill="#1d4ed8" font-family="Arial">轴线方向 ω=(1,0,0)</text>')
    parts.append('<text x="300" y="330" font-size="18" font-family="Arial">轴线: (x,y,z)=(0,-1,0)+t(1,0,0)</text>')
    parts.append(svg_footer())
    (ROOT / "q5_axis.svg").write_text("".join(parts), encoding="utf-8")


def draw_q8() -> None:
    width, height = 640, 420
    ox, oy = 150, 290
    scale = 90

    def pt(x: float, y: float) -> tuple[float, float]:
        return ox + x * scale, oy - y * scale

    px, py = pt(0, 1)
    xh, yh = pt(4, 0)
    zhx, zhy = pt(0, 2.2)

    parts = [svg_header(width, height)]
    parts.append('<rect width="100%" height="100%" fill="white"/>')
    parts.append('<text x="24" y="34" font-size="24" font-family="Arial">第8题：过 P 的互易力旋量族</text>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{xh}" y2="{yh}" stroke="#333" stroke-width="2.5" marker-end="url(#arrow)"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{zhx}" y2="{zhy}" stroke="#333" stroke-width="2.5" marker-end="url(#arrow)"/>')
    parts.append(f'<text x="{xh + 8}" y="{yh + 4}" font-size="18" font-family="Arial">x</text>')
    parts.append(f'<text x="{zhx - 8}" y="{zhy - 10}" font-size="18" font-family="Arial">y</text>')
    parts.append('<line x1="60" y1="200" x2="520" y2="200" stroke="#ddd" stroke-width="1.5" stroke-dasharray="6,6"/>')
    parts.append('<text x="530" y="206" font-size="16" fill="#666" font-family="Arial">z=0 平面</text>')

    angles = [-70, -35, 0, 30, 65]
    for angle in angles:
        import math
        length = 180
        dx = length * math.cos(math.radians(angle))
        dy = length * math.sin(math.radians(angle))
        x2 = px + dx
        y2 = py - dy
        parts.append(f'<line x1="{px}" y1="{py}" x2="{x2}" y2="{y2}" stroke="#b91c1c" stroke-width="3" marker-end="url(#redarrow)"/>')

    parts.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#111"/>')
    parts.append(f'<text x="{px + 8}" y="{py - 10}" font-size="18" font-family="Arial">P(0,1,0)</text>')
    parts.append('<text x="285" y="360" font-size="18" fill="#b91c1c" font-family="Arial">所有作用线均过 P，且位于 z=0 平面</text>')
    parts.append(svg_footer())
    (ROOT / "q8_force_family.svg").write_text("".join(parts), encoding="utf-8")


if __name__ == "__main__":
    draw_q5()
    draw_q8()
