# Plymouth 启动动画主题资产

本目录为 Linxira OS 的 Plymouth 启动动画主题 `linxira`(two-step 模块)。

## 内容

- `linxira.plymouth` — 主题定义(Name=linxira, ModuleName=two-step, ImageDir=/usr/share/plymouth/themes/linxira)
- `watermark.png` — 启动动画中央 logo(256x256)
- `animation-0001..0036.png` — 旋转 spinner 动画帧(36 个)
- `throbber-*.png` — throbber 进度帧(30 个)
- `box.png` / `entry.png` / `bullet.png` / `capslock.png` / `keyboard.png` / `keymap-render.png` / `lock.png` — two-step 界面元素

## 来源与备份

- 2026-08-03 从 Hyper-V 构建机 `/home/linxira-builder/rc6-work/linxira-plymouth-theme` 备份入库(此前仅存在于构建机,无仓库副本)
- 构建机路径为 ISO 构建时 `build-direct-iso.sh --plymouth-theme-directory` 的输入
- 启动动画 logo 以 `linxira-logo.svg`(Scale L 标记)为基准,与 UEFI/GRUB 视觉体系一致

## 使用

- ISO 构建:`./build-direct-iso.sh ... --plymouth-theme-directory <本目录路径>`
- 安装位置(目标系统):`/usr/share/plymouth/themes/linxira/`
