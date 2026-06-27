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
| `linxira-l.svg` | 主标识 | 带棱镜切割感的 L，有光束和色散效果 |
| `linxira-l-simple.svg` | 简化版 | 适合小尺寸，保留核心元素 |
| `linxira-l-mono.svg` | 单色版 | 适合单色场景 |
| `linxira-logo.svg` | 完整图形 | 棱镜图形，用于品牌展示 |

## 关键设计决策

1. **单字符 L** — 像 Arch 的 "A"、CachyOS 的 "C" 一样，用单个字母作为标识
2. **棱镜切割感** — L 的转角处有三角棱镜，竖笔上有光谱折射线
3. **光束色散** — 从 L 的转角发出三道光束，代表科学光谱
4. **品牌色渐变** — 青绿→蓝色→紫色，契合 "Linux for Science" 定位
5. **文字使用通用 Linux 字体族** — 避免依赖 Windows 字体导致渲染失败

## 导出壁纸

```bash
./tools/export-png.sh
```

会自动将 SVG 壁纸导出为 1920x1080、2560x1440、3840x2160 三种分辨率的 PNG。
