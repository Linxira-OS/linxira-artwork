# linxira-artwork

Linxira OS 官方美术资源仓库。包含品牌 Logo、壁纸、图标及欢迎横幅。

## 品牌色

- 青绿 `#14b8a6` / `#22c7da` — 物理、生物
- 紫色 `#6366f1` / `#8b5cf6` — 化学、计算
- 暗蓝 `#020617` / `#0f172a` — 背景、深空

## 文件结构

```
assets/
  logo/                  — Logo 源文件 (SVG)
  wallpaper/             — 壁纸源文件 (SVG)
  welcome/               — 欢迎横幅 (SVG)
  ascii/                 — ASCII 艺术
usr/share/
  linxira/               — 系统级品牌文件
  backgrounds/linxira/   — GNOME 背景
  wallpapers/LinxiraOS/  — KDE 壁纸主题
tools/
  export-png.sh          — SVG → PNG 导出脚本
```

## 关键设计决策

1. **棱镜 (Prism)** 作为核心图形 — 科学光谱折射，契合 "Linux for Science" 定位。
2. **文字使用通用 Linux 字体族** — 避免依赖 Windows 字体导致渲染失败。

## 导出壁纸

```bash
./tools/export-png.sh
```

会自动将 SVG 壁纸导出为 1920x1080、2560x1440、3840x2160 三种分辨率的 PNG。
