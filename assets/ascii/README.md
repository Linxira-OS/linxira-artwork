# 终端字符画资产

## linxira-logo-braille60.ansi(正式终端字符画,2026-08-03 确认)

- **风格**:Chafa Braille 盲文点阵,60×16
- **来源矢量**:`../logo/linxira-l.svg`(Scale L 标记,基准色 #20B8B0)
- **生成命令**(Chafa 1.18.2):
  ```
  chafa --format symbols --colors full --size 60x16 --symbols braille linxira-l.svg > linxira-logo-braille60.ansi
  ```
- **用途**:fastfetch 终端 logo(`/usr/share/linxira/linxira-logo-braille60.ansi`,ISO 内 fastfetch 配置引用);含 ANSI 色码,终端支持时渲染青色
- **显示确认**:2026-08-03 用户在终端(等宽字体)确认形状后选定,取代旧版 `logo-ascii.txt`(手写 LL|--)

## 历史资产(保留存档,不再打包)

- `logo-ascii.txt` — 旧版手写 LL|-- 文本(RC17 起使用,已废弃)
- `logo-ascii.ansi` — 符号风格旧版(未使用,已废弃)
- `logo-ascii.svg` — 字符画参考 SVG
