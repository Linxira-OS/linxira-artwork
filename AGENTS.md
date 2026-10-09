# linxira-artwork · Agent 开发规范

> **档位**:A 档 · 系统源仓(品牌美术资源,带 `VERSION` + `.github/workflows/release.yml`)。
> **本仓职责**:Linxira OS 官方美术资源(brand / wallpaper / icon / Plymouth 主题 / 欢迎横幅 / ASCII)的唯一来源。
> 通用条款见工作区总纲 `f:\Linxira-OS\AGENTS.md`;发布/测试口径见 `linxira-os/docs/RELEASE_STANDARD.md`。本文件只写本仓特有约定。

## 职责与边界

- **负责**:品牌 Logo 源文件(`assets/logo/`)、壁纸(`assets/wallpaper/`)、Plymouth 主题、欢迎横幅、ASCII 美术,以及系统级安装路径 `usr/share/`(GNOME backgrounds、KDE wallpaper 主题、`usr/share/linxira/`)。
- **不负责**:Plymouth 的打包/安装逻辑(`linxira-plymouth-theme` 仓);GNOME/KDE 桌面配置(`gnome-settings` / `kde-settings`)。本仓只出**素材与安装镜像路径**。
- 品牌色与设计语言以 `README.md` 为准(青绿 `#20B8B0`、珊瑚红 `#F36F5D`、深墨 `#0E1417`)。

## 目录布局

```
assets/logo/        品牌 Logo 源文件 (SVG) 及 Zeta LZ 标识
assets/wallpaper/   壁纸源文件 (SVG,深色/浅色)
assets/welcome/     欢迎横幅 (SVG)
assets/ascii/       终端 ASCII 美术
assets/plymouth/    Plymouth 主题资源 (PNG 帧 + watermark)
assets/concepts/    设计概念稿(非发布产物)
usr/share/          随包安装的系统级品牌文件路径
tools/              export-png.sh 等构建/预览脚本
TRADEMARKS.md       商标政策(英文 + 中文)
```

## 本地校验

无 Python/编译步骤,CI 只做**资产存在性校验**(见 `.github/workflows/ci.yml`):

```sh
test -f assets/ascii/linxira-logo-braille60.ansi
test -f usr/share/linxira/linxira-logo.svg
test -f TRADEMARKS.md
test -f assets/plymouth/linxira-plymouth-theme/watermark.png
```

导出壁纸为 PNG(1920x1080 / 2560x1440 / 3840x2160):

```sh
./tools/export-png.sh
```

## 版本与发布

- 版本唯一来源是根目录 `VERSION`(当前 1.0.3)。
- 提交 `VERSION` 变更即触发 `.github/workflows/release.yml` 建 `v<VERSION>` Release,再由 `packages/auto-bump.yml` 走全自动发布链。**禁止手工 bump 或手工改 PKGBUILD**。
- 本仓默认分支为 `master`(以工作区总纲第 3 节为准)。

## 禁区

- **版权/商标**:`TRADEMARKS.md` 为默认保留版权;不得将品牌资产用于非 Linxira 产品的标识或暗示官方背书。
- 不改 `usr/share/` 下的既有安装路径契约(会破坏 GNOME/KDE 引用与打包清单)。
- 不提交 PNG 之外的构建临时产物;`.mimosa/` 等工具态不入仓。
- 破坏性操作(批量删除素材、重命名稳定文件名)先确认。