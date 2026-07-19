# linxira-artwork

Linxira OS 官方美术资源仓库。包含品牌 Logo、壁纸、图标及欢迎横幅。

## 版权与商标

本仓库中的 Linxira、Linxira OS、Scale L、Logo、图标、壁纸、Plymouth
主题和欢迎横幅属于 Linxira OS 品牌资产，默认保留全部权利。未经书面许可，
不得将这些资产用于其他发行版、产品或组织的品牌标识，也不得暗示官方背书。
允许在未修改的 Linxira OS 镜像或未修改的 Linxira 软件包中随附分发，但必须保留
版权和商标声明。完整政策见 [`TRADEMARKS.md`](TRADEMARKS.md)。

## 品牌色

- 青绿 `#20B8B0` — 主标识与科学仪器感
- 珊瑚红 `#F36F5D` — 测量终点与强调色
- 深墨色 `#0E1417` — 参考轴与深色背景

## 文件结构

```
assets/
  logo/                  — Logo 源文件 (SVG)
    linxira-l.svg        — 单字符 L Logo (主标识)
    linxira-l-simple.svg — 简化版
    linxira-l-mono.svg   — 单色版
    linxira-logo.svg     — 完整 Logo (棱镜图形)
    linxira-icon.svg     — 图标
    linxira-lockup.svg   — Logo + 文字组合
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

## Logo 变体

| 文件 | 用途 | 说明 |
|------|------|------|
| `linxira-l.svg` | 主标识 | Scale L，带参考轴、刻度和测量终点 |
| `linxira-l-simple.svg` | 简化版 | 适合小尺寸，保留核心元素 |
| `linxira-l-mono.svg` | 单色版 | 适合单色场景 |
| `linxira-logo.svg` | 完整图形 | 棱镜图形，用于品牌展示 |

## 关键设计决策

1. **单字符 L** — 用紧凑、可独立识别的字母标识系统身份
2. **参考坐标轴** — 内部深色轴线代表可复现的测量框架
3. **科学刻度** — 竖向和横向刻度强化科研仪器与工程标尺语义
4. **测量终点** — 珊瑚色端点作为结果、边界和行动强调色
5. **文字使用通用 Linux 字体族** — 避免依赖 Windows 字体导致渲染失败

## 导出壁纸

```bash
./tools/export-png.sh
```

会自动将 SVG 壁纸导出为 1920x1080、2560x1440、3840x2160 三种分辨率的 PNG。
