# 终端字符画资产

两档，均由 `../tools/gen-brand-assets.py` 从同一份「原点框」几何**确定性生成**（不是采样）。

## `logo-ascii.txt` — ASCII 档（24×12，安全档）

- **只含 `#` `@` 和空格**：全部是 **Narrow** 字符 ⇒ 中文终端、任何 `ambiguous width` 设置下都不会错位。
- 比例与矢量一致：框 1 格 / 角 2 格（外凸 1 格）/ 臂长 39% / 端点 ≈ 角厚（4+2 阶梯）。
- 行尾已右裁剪（避免渲染器吞尾随空格导致"某行少一格"的错觉）。
- 自检：每行都是 24 字符；见 `tools/gen-brand-assets.py` 的构造（矩形填充，无半格）。

## `linxira-logo-braille60.ansi` — 盲文档（30×15 = 60×60 点，高密度）

- 用 ANSI 真彩（`38;2;r;g;b`）标记三色：框深墨 / 角青绿 / 端点珊瑚（终端主题见下）。
- **只用整字符**：所有坐标对齐 2×4 点阵，没有半格碎点。
- ⚠️ 盲文属 **East Asian Width = Ambiguous**：终端若把 ambiguous 当双宽渲染，会整块错位。
  用网页校验器（`term.html`）可以量化看到（30×15 档启用双宽后 12/15 行宽度变化）。
- 深色终端里"墨"要用亮色画（`#E9EFF0`），否则框与背景同色、看起来像缺了一块。

## 生成

```sh
python3 tools/gen-brand-assets.py            # 写艺术仓
python3 tools/gen-brand-assets.py --site ../Linxira-OS.github.io   # 额外写站点 public/assets
```

## 历史资产（保留存档，不再打包）

- `logo-ascii.ansi` — 旧版符号风格（已废弃）
- `logo-ascii.svg` — 旧版字符画参考 SVG

早期盲文档由 `chafa --symbols braille` 采样生成（2026-08）；采样会糊边、且无法保住"接缝"，
现已改为按格构造，`chafa` 不再是构建依赖。
