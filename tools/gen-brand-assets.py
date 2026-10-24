#!/usr/bin/env python3
"""从 G2「原点框(Origin Frame)」几何生成全部品牌矢量与字符画（确定性，纯标准库）。

单一真源: 512×512 视口内的三条几何 —— 框(参考框架) / 角(轴, 接缝) / 点(测量端点)。
线宽比例来自旧标沿用值: 框 7 : 角 15（×5.12 ⇒ 36 / 76 ≈ 2.1:1），端点 r8 ⇒ 41。

产出（覆盖写入同名文件，保持打包路径契约不变）:
  assets/logo/linxira-l.svg          主标（三色，透明底）
  assets/logo/linxira-l-mono.svg     单色（深墨，浅底用）
  assets/logo/linxira-l-simple.svg   简化（去端点，小尺寸用）
  assets/logo/favicon.svg            图标（深底圆角方块 + 标）
  assets/logo/linxira-icon.svg       同 favicon（打包 icon）
  assets/logo/linxira-logo.svg       横排组合（标 + 字标，通用 Linux 字体族）
  usr/share/linxira/linxira-logo.svg  同组合（系统路径契约）
  usr/share/linxira/linxira-icon.svg  同图标（系统路径契约）
  assets/ascii/logo-ascii.txt        字符画（24×12，Narrow 字符）
  assets/ascii/linxira-logo-braille60.ansi  盲文（30×15 = 60×60 点）

字符画与 SVG 同源: 框1格/角2格/臂长39%/点≈角厚；全部坐标落在字符格上，无半格碎点。
运行: python3 tools/gen-brand-assets.py [--site PATH]   # --site 额外写入站点 public/assets
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEAL, CORAL, INK = "#20B8B0", "#F36F5D", "#0E1417"
MONO_INK = "#FFFFFF"          # 单色档 = 白色（深色背景用；旧 mono 也是白色基底）
FRAME = "M215 72H440V440H72V215"
CORNER = "M72 215V72H215"
DOT = (164, 164, 41)


def mark(colors=(INK, TEAL, CORAL), dot=True) -> str:
    ink, teal, coral = colors
    parts = [
        f'  <path d="{FRAME}" fill="none" stroke="{ink}" stroke-width="36" stroke-linejoin="miter"/>',
        f'  <path d="{CORNER}" fill="none" stroke="{teal}" stroke-width="76" stroke-linejoin="miter"/>',
    ]
    if dot:
        parts.append(f'  <circle fill="{coral}" cx="{DOT[0]}" cy="{DOT[1]}" r="{DOT[2]}"/>')
    return "\n".join(parts)


def svg(label: str, body: str, size: int = 512) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
            f'width="{size}" height="{size}" role="img" aria-label="{label}">\n{body}\n</svg>\n')


def tile(rounded: int = 96) -> str:
    """图标：深底圆角方块 + 亮青/珊瑚标（深浅背景都成立）。"""
    return ("  <rect width=\"512\" height=\"512\" rx=\"{}\" fill=\"{}\"/>\n".format(rounded, INK)
            + "  <g transform=\"translate(51.2 51.2) scale(0.8)\">\n"
            + "\n".join("  " + line for line in mark(("#E9EFF0", "#2AC9C1", CORAL)).splitlines())
            + "\n  </g>")


def lockup() -> str:
    """横排：标 + 字标。字标用通用 Linux 字体族（旧设计决策 #5：不依赖 Windows 字体）。"""
    return (
        '  <g transform="translate(24 96) scale(0.62)">\n'
        + "\n".join("  " + line for line in mark().splitlines())
        + "\n  </g>\n"
        + '  <text x="392" y="252" font-family="system-ui, \'Noto Sans\', \'DejaVu Sans\', sans-serif" '
          'font-size="104" font-weight="600" letter-spacing="2" fill="' + INK + '">Linxira</text>\n'
        + '  <text x="394" y="310" font-family="system-ui, \'Noto Sans\', \'DejaVu Sans\', sans-serif" '
          'font-size="34" letter-spacing="9" fill="' + TEAL + '">OS</text>'
    )


# ---------------- 字符画（与 gen_art.py 同一构造） ----------------
BRAILLE_BITS = {(0, 0): 1, (0, 1): 2, (0, 2): 4, (0, 3): 64,
                (1, 0): 8, (1, 1): 16, (1, 2): 32, (1, 3): 128}


def art_ascii() -> str:
    cols, rows = 24, 12
    g = [[None] * cols for _ in range(rows)]

    def put(x0, y0, x1, y1, v):
        for y in range(max(0, y0), min(rows, y1)):
            for x in range(max(0, x0), min(cols, x1)):
                g[y][x] = v

    put(2, 1, 22, 2, "ink"); put(21, 1, 22, 11, "ink")
    put(2, 10, 22, 11, "ink"); put(2, 1, 3, 11, "ink")
    put(1, 0, 9, 2, "teal"); put(1, 0, 3, 4, "teal")
    put(6, 3, 10, 4, "coral"); put(7, 4, 9, 5, "coral")
    ch = {"ink": "#", "teal": "#", "coral": "@"}
    return "\n".join("".join(ch.get(c, " ") for c in row).rstrip() for row in g)


def _braille_rows():
    """返回 15 行、每行 30 个 (字符, 颜色名|None)；坐标全对齐 2×4 点阵。"""
    dots = [[None] * 60 for _ in range(60)]

    def put(x0, y0, x1, y1, v):
        for y in range(y0, y1):
            for x in range(x0, x1):
                dots[y][x] = v

    put(20, 8, 52, 12, "ink"); put(48, 8, 52, 52, "ink")
    put(8, 48, 52, 52, "ink"); put(8, 20, 12, 52, "ink")
    put(4, 4, 20, 12, "teal"); put(4, 4, 12, 20, "teal")
    put(16, 16, 24, 20, "coral"); put(18, 20, 22, 24, "coral")
    rows = []
    for br in range(0, 60, 4):
        line = []
        for bc in range(0, 60, 2):
            mask, color = 0, None
            for dx in range(2):
                for dy in range(4):
                    c = dots[br + dy][bc + dx]
                    if c:
                        mask |= BRAILLE_BITS[(dx, dy)]
                        color = color or c
            line.append((chr(0x2800 + mask) if mask else " ", color))
        rows.append(line)
    return rows


def art_braille() -> str:
    """纯文本盲文（右裁剪；无颜色）。"""
    return "\n".join("".join(ch for ch, _ in row).rstrip() for row in _braille_rows())


# 深色终端调色板：墨要用亮色，否则框=背景色
ANSI_RGB = {"ink": (0xE9, 0xEF, 0xF0), "teal": (0x2A, 0xC9, 0xC1), "coral": (0xF3, 0x6F, 0x5D)}


def art_braille_ansi() -> str:
    """真彩盲文（fastfetch file-raw 用）：逐格 38;2;r;g;b，行尾右裁剪。"""
    out = []
    for row in _braille_rows():
        keep = len(row)
        while keep and row[keep - 1][0] == " ":
            keep -= 1
        parts = []
        for ch, color in row[:keep]:
            if color is None:
                parts.append(" ")
                continue
            r, g, b = ANSI_RGB[color]
            parts.append(f"\x1b[38;2;{r};{g};{b}m{ch}\x1b[0m")
        out.append("".join(parts))
    return "\n".join(out)


def write(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    site = None
    if "--site" in sys.argv:
        site = pathlib.Path(sys.argv[sys.argv.index("--site") + 1])

    label = "Linxira Origin Frame mark"
    files = {
        "assets/logo/linxira-l.svg": svg(label, mark()),
        "assets/logo/linxira-l-mono.svg": svg("Linxira Origin Frame mark (monochrome)",
                                             mark((MONO_INK, MONO_INK, MONO_INK))),
        "assets/logo/linxira-l-simple.svg": svg("Linxira Origin Frame mark (simplified)",
                                               mark(dot=False)),
        "assets/logo/favicon.svg": svg("Linxira icon", tile()),
        "assets/logo/linxira-icon.svg": svg("Linxira icon", tile()),
        "assets/logo/linxira-logo.svg": ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 512" '
                                         'width="1024" height="512" role="img" aria-label="Linxira logo">\n'
                                         + lockup() + "\n</svg>\n"),
        "usr/share/linxira/linxira-logo.svg": ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 512" '
                                               'width="1024" height="512" role="img" aria-label="Linxira logo">\n'
                                               + lockup() + "\n</svg>\n"),
        "usr/share/linxira/linxira-icon.svg": svg("Linxira icon", tile()),
        "assets/ascii/logo-ascii.txt": art_ascii() + "\n",
        "assets/ascii/linxira-logo-braille60.ansi": art_braille_ansi() + "\n",
    }
    print("写入艺术仓:")
    for rel, text in files.items():
        write(ROOT / rel, text)

    if site:
        print("写入站点 public/assets:")
        mapping = {
            "assets/logo/linxira-l.svg": "linxira-l.svg",
            "assets/logo/linxira-l-mono.svg": "linxira-l-mono.svg",
            "assets/logo/linxira-l-simple.svg": "linxira-l-simple.svg",
            "assets/logo/favicon.svg": "favicon.svg",
            "assets/lineup": None,
        }
        for rel, dst in mapping.items():
            if dst:
                write(site / "public" / "assets" / dst, files[rel])
        # 站点另有一份 linxira-logo.svg（横排）与 favicon.png/PNG 导出另行生成
        write(site / "public" / "assets" / "linxira-logo.svg", files["assets/logo/linxira-logo.svg"])
        write(site / "public" / "assets" / "linxira-logo-braille60.ansi",
              files["assets/ascii/linxira-logo-braille60.ansi"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
