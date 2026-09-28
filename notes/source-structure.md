# 原文结构与页码记录

PDF 文件共 158 页，文件名为 `Peddie P. The History of the GPU - Steps to Invention 2022.pdf`。

## 已确认

- PDF 具有可提取的文本层；当前环境中 `pdftotext` 可读取文字。
- PDF 前置部分包含书名页、版权页、Foreword、Preface、Acknowledgments and Contributors。
- 原书同时显示印刷页码（罗马数字前置页码、阿拉伯数字正文页码）和 PDF 页序，翻译时应明确区分。
- 前言中说明本书是 GPU 历史三卷系列第一卷，内容覆盖通向集成 GPU 的发展，约从 20 世纪 60 年代至 20 世纪 90 年代末。
- 当前 PDF 是一个节选/部分文件：目录显示完整原书正文至第 393 页，但当前 PDF 在 PDF 第 158 页、印刷页码 131 附近仍处于第 3 章中段。因此不能把当前文件误标为完整 158 页原书。

## 当前文件中可见的章节范围

| 原书部分 | 译文文件 | 原书页码 | PDF 页码 | 状态 |
|---|---|---:|---:|---|
| Foreword | `translation/00-foreword.md` | v–vii | 5–7 | 初译完成 |
| Preface | `translation/01-preface.md` | ix–xv | 8–15 左右 | 待翻译 |
| Contents / List of Figures | `notes/source-structure.md` | xvii–xxv 及后续 | 约 15–24 | 已初步整理 |
| Introduction | 待定 | 1 起 | 约 25 起 | 待翻译 |
| 1980–1989, Graphics Controllers on Other Platforms | 待定 | 31 起 | 当前文件中可能未完整覆盖 | 待核对 |
| 1980–1989, Graphics Controllers on PCs | 待定 | 99 起 | 当前文件在第 3 章中段结束 | 待核对 |
| 后续章节 | 待定 | 147 起 | 当前 PDF 未覆盖完整内容 | 待核对 |

## 完整原书目录（根据 PDF 中的 Contents）

1. Introduction（引言），原书第 1 页
2. 1980–1989, Graphics Controllers on Other Platforms（1980–1989：其他平台上的图形控制器），原书第 31 页
3. 1980–1989, Graphics Controllers on PCs（1980–1989：PC 上的图形控制器），原书第 99 页
4. 1980–1995 the Progenitors: Graphics Controller on PCs（1980–1995：先驱——PC 上的图形控制器），原书第 147 页
5. 1990 to 1999 Graphics Controllers on Other Platform（1990–1999：其他平台上的图形控制器），原书第 203 页
6. 1996–1999, Graphics Controllers on PCs（1996–1999：PC 上的图形控制器），原书第 265 页
7. What is a GPU?（什么是 GPU？），原书第 333 页
8. Appendix A: Acronyms（附录 A：缩略语），原书第 347 页
9. Appendix B: Definitions（附录 B：定义），原书第 353 页
10. Index（索引），原书第 393 页

## 提取约定

推荐使用 `pdftotext -layout -f 起始页 -l 结束页` 进行批量提取，并在翻译文件开头记录对应范围。图表和复杂版式需要另行人工核对。PDF 页序与原书印刷页码必须分别记录。
