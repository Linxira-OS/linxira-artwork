# linxira-artwork

Official artwork repository for Linxira OS. Contains brand logos, wallpapers, icons, and welcome banners.

## Copyright and Trademarks

Linxira, Linxira OS, Origin Frame, the Logo, icons, wallpapers, the Plymouth theme,
and welcome banners in this repository are Linxira OS brand assets; all rights
are reserved by default. Without written permission, these assets must not be
used for the branding of other distributions, products, or organizations, nor
in any way that implies official endorsement. Redistribution bundled with
unmodified Linxira OS images or unmodified Linxira packages is permitted,
provided the copyright and trademark notices are retained. See
[`TRADEMARKS.md`](TRADEMARKS.md) for the full policy.

## Brand Colors

- Teal `#20B8B0` — primary identity with a scientific-instrument feel
- Coral red `#F36F5D` — measurement endpoints and accent color
- Deep ink `#0E1417` — reference axes and dark backgrounds

## File Structure

```
assets/
  logo/                  — Logo source files (SVG)
    linxira-l.svg        — primary mark (Origin Frame)
    linxira-l-simple.svg — simplified (frame + corner, no endpoint)
    linxira-l-mono.svg   — monochrome version
    linxira-launcher-dark.svg  — launcher mark, light frame on transparent (dark panels)
    linxira-launcher-light.svg — launcher mark, deep frame on transparent (light panels)
    linxira-logo-on-dark.svg   — horizontal lockup with light ink (dark backgrounds)
    linxira-logo.svg     — horizontal lockup (mark + wordmark)
    linxira-icon.svg     — app icon (dark tile)
    favicon.svg          — favicon (dark tile)
    zeta-logo.svg       — Zeta sub-brand LZ mark (deep black base + bright teal + coral cursor)
    zeta-icon.ico       — Zeta icon (16/32/48/64/128/256 multi-size)
  wallpaper/             — wallpaper source files (SVG)
    linxira-wallpaper.svg      — dark wallpaper
    linxira-wallpaper-light.svg — light wallpaper
  welcome/               — welcome banners (SVG)
  ascii/                 — ASCII art
usr/share/
  linxira/               — system-level branding files
  backgrounds/linxira/   — GNOME backgrounds
  wallpapers/LinxiraOS/  — KDE wallpaper theme (dark)
  wallpapers/LinxiraOS-light/ — KDE wallpaper theme (light)
tools/
  export-png.sh          — SVG → PNG export script
```

## Logo Variants

| File | Purpose | Notes |
|------|---------|-------|
| `linxira-l.svg` | Primary mark | **Origin Frame**: reference frame + seamed origin corner + coral endpoint |
| `linxira-l-simple.svg` | Simplified | Frame + corner only (no endpoint), for very small sizes |
| `linxira-l-mono.svg` | Monochrome | White ink, for dark backgrounds |
| `linxira-logo.svg` | Lockup | Mark + "Linxira" wordmark (generic Linux font family) |
| `linxira-launcher-dark.svg` | Launcher mark (dark) | Transparent background, frame in `#E9EFF0`; teal/coral unchanged |
| `linxira-launcher-light.svg` | Launcher mark (light) | Transparent background, frame in `#0E1417`; teal/coral unchanged |
| `linxira-logo-on-dark.svg` | Lockup (dark) | Frame and "Linxira" in `#E9EFF0`; "OS" stays teal |
| `favicon.svg` / `linxira-icon.svg` | Icon | Mark on a deep-ink rounded tile (works on light and dark) |

All vector assets are generated from one geometry by `tools/gen-brand-assets.py`
(the same script also emits the terminal character art) — edit the script, not the files.

## Key Design Decisions

1. **Origin Frame** — a square reference frame with **one seamed corner**: the top-left corner is drawn as a
   thicker stroke (the axes) that completes the frame, so the frame and the axes are one continuous shape.
2. **The seam** — a deliberate ~2:1 weight step (36 vs 76 in the 512 viewBox) where the thick corner meets the
   thin frame; it is the mark's only "detail" and it survives down to 16 px.
3. **Measurement endpoint** — the coral dot sits inside the origin corner, at the documented "measurement
   endpoint" position (~32 % of the frame), not on a stroke, so monochrome rendering keeps all three elements.
4. **Three colour roles** — deep ink `#0E1417` = reference frame / teal `#20B8B0` = axes / coral `#F36F5D` =
   endpoint. On dark backgrounds the ink flips to `#E9EFF0` (the frame would otherwise equal the background).
5. **Supersedes Scale L** (2026-10) — the previous single-character `L` mark is retired; the assets keep their
   historical file names so packaging paths and site references stay valid.
6. **Generic Linux font families for text** — avoids rendering failures caused by depending on Windows fonts.

## Zeta Sub-brand Mark

Zeta is Linxira's terminal coding agent. Its LZ two-letter mark (L = Linxira,
Z = Zeta) reuses the Origin Frame design language of the main site:

- **Deep black base** `#0E1417`: a self-contained icon that holds up on both light and dark backgrounds
- **Bright teal strokes** `#2AC9C1`: slightly brightened from the primary brand teal `#20B8B0` to improve contrast on dark UIs
- **Coral block cursor** `#F36F5D`: echoes the terminal identity and the measurement-endpoint accent color

The two-letter design avoids clashing with products that use a single-letter Z
mark (such as the GLM desktop CLI / Desktop).

| File | Purpose | Notes |
|------|---------|-------|
| `zeta-logo.svg` | Zeta mark | Two-letter LZ, deep black base + bright teal + coral cursor |
| `zeta-icon.ico` | Zeta icon | 16/32/48/64/128/256 multi-size, for favicon and desktop icons |

Source files live in `assets/logo/`, kept in sync with the site's
`public/assets/zeta-logo.*` and `zeta-logo.ico`.

## Exporting Wallpapers

```bash
./tools/export-png.sh
```

Automatically exports the SVG wallpapers to PNG at three resolutions:
1920x1080, 2560x1440, and 3840x2160.

---

## 简体中文

Linxira OS 官方美术资源仓库。包含品牌 Logo、壁纸、图标及欢迎横幅。

### 版权与商标

本仓库中的 Linxira、Linxira OS、原点框（Origin Frame）、Logo、图标、壁纸、Plymouth
主题和欢迎横幅属于 Linxira OS 品牌资产，默认保留全部权利。未经书面许可，
不得将这些资产用于其他发行版、产品或组织的品牌标识，也不得暗示官方背书。
允许在未修改的 Linxira OS 镜像或未修改的 Linxira 软件包中随附分发，但必须保留
版权和商标声明。完整政策见 [`TRADEMARKS.md`](TRADEMARKS.md)。

### 品牌色

- 青绿 `#20B8B0` — 主标识与科学仪器感
- 珊瑚红 `#F36F5D` — 测量终点与强调色
- 深墨色 `#0E1417` — 参考轴与深色背景

### 文件结构

```
assets/
  logo/                  — Logo 源文件 (SVG)
    linxira-l.svg        — 主标识（原点框 Origin Frame）
    linxira-l-simple.svg — 简化版（框 + 角，无端点）
    linxira-l-mono.svg   — 单色版
    linxira-launcher-dark.svg  — 启动器标，白框透明底（深色面板）
    linxira-launcher-light.svg — 启动器标，深框透明底（浅色面板）
    linxira-logo-on-dark.svg   — 横排组合深底版（白墨）
    linxira-logo.svg     — 横排组合（标 + 字标）
    linxira-icon.svg     — 应用图标（深色底）
    favicon.svg          — 站点图标（深色底）
    zeta-logo.svg       — Zeta 子品牌 LZ 标识 (深黑底 + 亮青绿 + 珊瑚光标)
    zeta-icon.ico       — Zeta 图标 (16/32/48/64/128/256 多尺寸)
  wallpaper/             — 壁纸源文件 (SVG)
    linxira-wallpaper.svg      — 深色壁纸
    linxira-wallpaper-light.svg — 浅色壁纸
  welcome/               — 欢迎横幅 (SVG)
  ascii/                 — ASCII 艺术
usr/share/
  linxira/               — 系统级品牌文件
  backgrounds/linxira/   — GNOME 背景
  wallpapers/LinxiraOS/  — KDE 壁纸主题 (深色)
  wallpapers/LinxiraOS-light/ — KDE 壁纸主题 (浅色)
tools/
  export-png.sh          — SVG → PNG 导出脚本
```

### Logo 变体

| 文件 | 用途 | 说明 |
|------|------|------|
| `linxira-l.svg` | 主标识 | 原点框：参考框架 + 接缝原点角 + 珊瑚端点 |
| `linxira-l-simple.svg` | 简化版 | 适合小尺寸，保留核心元素 |
| `linxira-l-mono.svg` | 单色版 | 白色单色，用于深色背景 |
| `linxira-logo.svg` | 横排组合 | 标 + 字标（通用 Linux 字体族），用于品牌展示 |
| `linxira-launcher-dark.svg` | 启动器标（深底） | 透明底，外框 `#E9EFF0`；青与红不变 |
| `linxira-launcher-light.svg` | 启动器标（浅底） | 透明底，外框 `#0E1417`；青与红不变 |
| `linxira-logo-on-dark.svg` | 横排组合（深底） | 外框与 "Linxira" 用 `#E9EFF0`，"OS" 保持青绿 |
| `favicon.svg` / `linxira-icon.svg` | 图标 | 深墨圆角底 + 标（深浅背景都成立） |

### 应用图标族（App icon family）

规则：**共用同一个框（身份），框内图形区分功能（细节）**。例外只有门面 ——
`linxira-icon` / `linxira`（welcome、开始菜单、系统标识）用裸标，不画内部图形；
其余系统软件不得复用同一个标，否则启动器里会"全都长一样"。

| 图标（主题名） | 框内图形 | 语义 |
|---|---|---|
| `org.linxira.CrashWatch` | 心电脉冲 | 监视/心跳 |
| `org.linxira.RecoveryDiagnostics` | 回卷箭头 | 恢复 |
| `linxira-update` | 向下箭头 | 安装/落地 |
| `linxira-update-updates-available` | 珊瑚箭头 + 右下角徽标 | 有更新（徽标不与原点珊瑚点混淆） |
| `linxira-package-center` | 2×2 网格 | 软件集合 |
| `linxira-config-hub` | 三条滑杆 | 可调配置 |
| `linxira-components` | 六边形 | 组件引擎 |
| `linxira-completion-agent` | 四角星 | 生成 |
| `linxira-gaming-manager` | 十字键 | 手柄 |
| `linxira-hwd-detector` | 芯片 | 硬件检测 |
| `linxira-kernel-manager` | 分层 | 内核/模块 |

全部由 `tools/gen-brand-assets.py` 的 `APP_GLYPHS` 生成（深墨圆角底 + 标 + 图形），
输出到 `usr/share/icons/hicolor/scalable/apps/`，随包安装（`cp -a usr`）。

### 关键设计决策

1. **原点框（Origin Frame）** — 方形参考框架 + **一个接缝角**：左上角画成更粗的笔画（轴），由它补全方框，
   框与轴是一个连续形状。
2. **接缝** — 粗角与细框交接处保留约 2:1 的线宽台阶（512 视口内 76 vs 36）；这是全标唯一的"细节"，
   且能一直保留到 16px。
3. **测量终点** — 珊瑚点落在原点角内侧（框架的 ~32% 处），**不压在笔画上** ⇒ 单色渲染时三个元素都还在。
4. **三色分工** — 深墨 `#0E1417` = 参考框架 / 青绿 `#20B8B0` = 轴 / 珊瑚 `#F36F5D` = 端点。
   深色底上"墨"反转为 `#E9EFF0`（否则框与背景同色而消失）。
5. **取代 Scale L**（2026-10）— 旧的单字符 `L` 标退役；文件保留历史文件名，保证打包路径与站点引用不变。
6. **文字使用通用 Linux 字体族** — 避免依赖 Windows 字体导致渲染失败。

全部矢量由 `tools/gen-brand-assets.py` 从同一份几何生成（该脚本同时产出终端字符画）——改脚本，不要手改文件。

### Zeta 子品牌标识

Zeta 是 Linxira 旗下终端编码代理。其 LZ 双字母标识（L = Linxira，Z = Zeta）复用主站原点框设计语言：

- **深黑底** `#0E1417`：图标自包含，深浅背景均成立
- **亮青绿笔画** `#2AC9C1`：在主品牌青绿 `#20B8B0` 基础上略提亮，优化深色 UI 对比
- **珊瑚色块光标** `#F36F5D`：呼应终端身份与测量终点强调色

采用双字母是为避免与单字母 Z 的产品（如 GLM 桌面 CLI / Desktop）撞标。

| 文件 | 用途 | 说明 |
|------|------|------|
| `zeta-logo.svg` | Zeta 标识 | LZ 双字母，深黑底 + 亮青绿 + 珊瑚光标 |
| `zeta-icon.ico` | Zeta 图标 | 16/32/48/64/128/256 多尺寸，用于 favicon 与桌面图标 |

源文件位于 `assets/logo/`，与站点 `public/assets/zeta-logo.*` 及 `zeta-logo.ico` 保持一致。

### 导出壁纸

```bash
./tools/export-png.sh
```

会自动将 SVG 壁纸导出为 1920x1080、2560x1440、3840x2160 三种分辨率的 PNG。
