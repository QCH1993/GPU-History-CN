# 原文结构与页码记录

PDF 文件共 158 页，文件名为 `Peddie P. The History of the GPU - Steps to Invention 2022.pdf`。

## 已确认

- PDF 具有可提取的文本层；当前环境中 `pdftotext` 可读取文字。
- PDF 前置部分包含书名页、版权页、Foreword、Preface、Acknowledgments and Contributors。
- 原书同时显示印刷页码（罗马数字前置页码、阿拉伯数字正文页码）和 PDF 页序，翻译时应明确区分。
- 前言中说明本书是 GPU 历史三卷系列第一卷，内容覆盖通向集成 GPU 的发展，约从 20 世纪 60 年代至 20 世纪 90 年代末。

## 初步章节

| 原书部分 | 译文文件 | 原书页码 | PDF 页码 | 状态 |
|---|---|---:|---:|---|
| Foreword | `translation/00-foreword.md` | v–vii | 待完整核对 | 待翻译 |
| Preface | `translation/01-preface.md` | ix–xiii | 待完整核对 | 待翻译 |
| Graphics Controllers on Other Platforms, 1980–1990 | 待定 | 待核对 | 待核对 | 待翻译 |
| Graphics Controllers on PCs, 1980–1989 | 待定 | 待核对 | 待核对 | 待翻译 |
| Graphics Controllers on PCs, 1990–1995 | 待定 | 待核对 | 待核对 | 待翻译 |
| Graphics Controllers on Other Platforms, 1990–1999 | 待定 | 待核对 | 待核对 | 待翻译 |
| Graphics Controller on PCs, 1996–1999 | 待定 | 待核对 | 待核对 | 待翻译 |
| What Is a GPU | 待定 | 待核对 | 待核对 | 待翻译 |
| Glossary | 待定 | 待核对 | 待核对 | 待翻译 |
| Acronyms | 待定 | 待核对 | 待核对 | 待翻译 |

## 提取约定

推荐使用 `pdftotext -layout -f 起始页 -l 结束页` 进行批量提取，并在翻译文件开头记录对应范围。图表和复杂版式需要另行人工核对。
