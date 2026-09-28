# 序言

> 原文：[Preface](../source/en/chapters/01-preface.md)  
> 原书页码：ix–xv  
> PDF 页码：8–14  
> 原始章节 PDF：[`01-preface.pdf`](../source/en/raw/01-preface.pdf)

这是《GPU 历史》三卷系列中的第一本书。

历史类书籍很难写，技术史书籍尤其难写。为什么？因为事情并不会按照整齐有序的顺序发生。人们也许会认为事件 A 导致事件 B，但实际情况往往是 A 导致 D，B 导致 C，而 C 又导致 G。

集成图形处理器（GPU）已经被应用于如此众多的系统（平台）中，并且自 1996 年以来不断演进。那么，如何在这样一本书中，以线性的形式讲述一个二维故事呢？

一种办法是完全按照时间顺序罗列一切。另一种办法是按平台列举。还有一种选择，则是按公司或应用分类。

我选择将这三种方式结合起来。

本系列的第一本书介绍通向集成 GPU 的各项发展，时间跨度从 20 世纪 60 年代初至 90 年代末。本书分为两大部分：PC 平台和其他平台。其他平台包括工作站和游戏机。

每一章都按照可以独立阅读来设计，因此章节之间可能会有一些重复。希望每一章都能讲述一个有趣的故事。

一般而言，我会在一家公司成立的年份介绍并讨论它。不过，如果某家公司的发展十分重要，或者对行业产生了重大影响，那么它也可能在不同章节中、以多个时期为背景被反复讨论。

## GPU 历史

| 迈向发明——第一卷 | 时代与环境——第二卷 | 新发展——第三卷 |
|---|---|---|
| 1. 序言 | 1. 序言 | 1. 序言 |
| 2. GPU 的历史 | 2. 争相制造第一款 GPU | 2. GPU 的第二时代（2001–2006） |
| 3. 1980–1990 年：其他平台上的图形控制器 | 3. GPU 的功能 | 3. GPU 的第三至第五时代 |
| 4. 1980–1989 年：PC 上的图形控制器 | 4. GPU 的主要时代 | 4. 移动 GPU |
| 5. 1990–1995 年：PC 上的图形控制器 | 5. GPU 的第一时代 | 5. 游戏机 GPU |
| 6. 1990–1999 年：其他平台上的图形控制器 | 6. GPU 环境——硬件 | 6. 计算 GPU |
| 7. 1996–1999 年：PC 上的图形控制器 | 7. 应用程序接口（API） | 7. 开放 GPU |
| 8. 什么是 GPU | 8. GPU 环境——软件扩展 | 8. GPU 的第六时代 |

### 《GPU 的历史——迈向发明》

我将 GPU 的问世定义为：第一款完全集成、并具备硬件几何处理能力——变换与光照——的单芯片产品。在 PC 领域，这一荣誉属于 NVIDIA：1999 年 10 月，该公司推出了基于 NV10 芯片的 GeForce 256。不过，Silicon Graphics 公司（SGI）早在 1996 年就已经在 Nintendo 64 中引入了集成 GPU；ArtX 则在 NVIDIA 之后一个月为 PC 开发出了集成 GPU。正如你将在本书中了解到的，GPU 这一概念并非由 NVIDIA 首次提出，最早实现变换与光照的硬件也不是 NVIDIA 开发的。

但 NVIDIA 是第一个将这些要素全部整合到量产单芯片设备中的公司。

GPU 的演变并没有因为加入变换与光照（T&L）引擎就停止，因为第一代此类 GPU 配备的是固定功能 T&L 处理器——它们只能执行这一项任务；不执行任务时，它们就会闲置并消耗功率。GPU 继续演进，至今已经经历了六个发展时代，最终成为一种几乎无所不能的通用计算机器。

然而，要充分认识——并希望能够理解——GPU 这一伟大发展，就必须了解它是在什么地方、出于什么原因、以什么方式开发出来的。为此，我将从 20 世纪 50 年代末和 60 年代的早期计算机讲起。

如今，GPU 已无处不在。

## 本书收录与不收录的内容

作为一名公众演讲者和前工程师，你从上面的图中就能看出，我喜欢框图。我试图用框图说明所有具有创新意义的 GPU，以及其中一些前身。在某些情况下，我找不到足够的数据来构建框图；另一些情况下，我能做到的最好结果，是绘制系统级框图，其中 GPU 只是一个方框。

在这几本书中，你不会看到公式（没有数学内容）、代码示例、应用程序操作示例、用户界面插图，也希望不会看到广告或宣传性内容。

重要的引语和较长的引文会采用缩进格式，以表明它们的重要性，并将其与正文区分开来。

书末附有术语表。书中使用的术语并不会全部收入术语表，因为其中许多术语已经在正文中得到解释。

此外，本书还附有缩略语列表。技术行业很喜欢使用缩略语；它们可以节省沟通时间，但也可能令人非常困惑。缩略语列表给出每个缩略语及其简要说明。

## 重要事件

撰写这几本书时，我的一个目标是找出那些我（也希望其他人）认为属于转折点、并产生颠覆性结果的发展——也就是推动行业前进或改变行业方向的事情。我用粗体斜体标出了这些里程碑。

GPU 的问世正是这样一件事情。它深刻而永久地改变了计算机的工作方式和使用方式。

## 作者

### 一生追逐像素

从 20 世纪 60 年代初开始，我就一直从事计算机图形学工作：起初是一名工程师，后来成为企业家（我创办过四家公司，也经营过另外三家公司），最终在 1982 年以行业顾问和咨询师的身份，开始了一次未能成功的退休尝试。多年来，我观察、建议、指导并报道不断发展的公司及其技术。我亲眼看到，设计或制造图形控制器的公司数量从寥寥几家增加到 45 家以上。此外，还有 30 多家公司在设计或制造移动设备图形控制器。

我还撰写或参与撰写过几本其他计算机图形学著作（以我个人名义出版的七本，以及合著的六本）。我曾在世界各地的多所大学演讲，写过数不清的文章，也获得过几项专利；贯穿这一切的，是同一条充满激情的主线——计算机图形学，以及创造能够讲述故事的美丽图像。本书中大量配有图片：芯片的框图、芯片本身的照片、芯片所安装的电路板和系统的照片，以及一些发明和创造这些非凡设备的人物照片。这些设备影响并改善了我们的日常生活；我很自豪地说，其中许多人都是我的好朋友。

我对本书的编排方式是这样的（至少我是这样希望的）：你可以随手翻到任何一页，开始了解这个故事。你可以按线性顺序阅读；如果这样读下去，你很可能会发现新的信息，也可能会发现多得超出你所需要的信息。本书的不同部分都写有我的电子邮件地址，我会尽量回复每一封邮件，希望能在 48 小时内回复。我很愿意听到你的评论、你的故事和你的建议。

下面按字母顺序列出所有帮助过我完成本项目的人（至少我希望没有遗漏任何人）。遗憾的是，其中有几位已经去世。希望本书能够帮助人们铭记他们以及他们所作出的贡献。

感谢阅读。  
Jon Peddie——追逐像素，发现珍宝

## 致谢与贡献者

以下人士在编辑、访谈、数据、照片以及最重要的鼓励方面帮助了我。无论从字面意义还是实际意义上说，没有他们，我都不可能完成这本书。

- Anand Patel——Arm
- Andrew Wolfe——S3
- Ashraf Eassa——NVIDIA
- Atif Zafar——Pixilica
- Borger Ljosland——Falanx
- Brian Kelleher——DEC，后来加入 NVIDIA
- Bryan Del Rizzo——3dfx 与 NVIDIA
- Carrell Killebrew——TI/ATI/AMD
- Chris Malachowsky——NVIDIA
- Curtis Priem——NVIDIA
- Dado Banatao——S3
- Dan Vivoli——NVIDIA
- Dan Wood——Matrox、Intel
- Daniel Taranovsky——ATI
- Dave Erskine——ATI 与 AMD
- Dave Kasik——Boeing
- Dave Orton——SGI、ArtX、ATI 与 AMD
- David Harold——Imagination Technologies
- Edvaed Sergard——Falanx
- Emily Drake——Siggraph
- Eric Demers——AMD/Qualcomm
- Frank Paniagua——Video Logic
- Gary Tarolli——3dfx
- George Sidiropoulos——Think Silicon
- Gerry Stanley——Real3D
- Henry C. Lin——NVIDIA
- Henry Chow——Yamaha 与 Giga Pixel

- Henry Fuchs——UNC
- Henry Quan——ATI
- Hossain Yassaie——Imagination Technologies
- Iakovos Istamoulis——Think Silicon
- Ian Hutchinson——Arm
- Jay Eisenlohr——Rendition
- Jay Torborg——Microsoft
- Jeff Bush——Nyuzi
- Jeff Fischer——Weitek 与 NVIDIA
- Jem Davis——Arm
- Jensen Huang——NVIDIA
- Jim Pappas——Intel
- Joe Curley——Tseng/Intel
- John Poulton——UNC 与 NVIDIA
- Jonah Alben——NVIDIA
- Karl Guttag——TI
- Karthikeyan（Karu）Sankaralingam——威斯康星大学麦迪逊分校
- Kathleen Maher——JPA 与 JPR
- Ken Potashner——S3 与 SonicBlue
- Kristen Ray——Arm
- Lee Hirsch——NVIDIA
- Luke Kenneth Casson Leighton——Libre-GPU
- Mark Kilgard——NVIDIA（Iris GL）
- Mary Whitton——Iknoas
- Megan Zea——PCI SIG
- Melissa Scuse——Arm
- Mike Diehl——HP
- Mike Mantor——AND
- Mikko Alho——Siru
- Mikko Nurmi——Bitboys

- Neal Leavitt——编辑
- Neil Trevett——3Dlabs 与 Khronos
- Nick England——Iknoas
- Pedro Duarte——科英布拉大学
- Peter McGuinness——SGS Thompson
- Peter L. Segal——AT&T
- Petri Norlund——Bitboys
- Phil Roges——ATI
- Richard Huddy——ATI
- Richard Selvaggi——Tseng Labs
- Rick Bergman——ATI/AMD
- Robert Dow——JPR
- Ross Smith——3dfx
- Ruchika Saini——编辑
- Sasa Marinkovic——ATI 与 AMD
- Simon Fenny——Video Logic 与 Imagination Technologies
- Stefan Demetrescu——斯坦福大学
- Stephen Morein——Stellar
- Steve Brightfield——SiliconArts
- Steve Edelson——Edson Labs
- Tatsuo Yamamoto——Sega/DMP
- Tim Leland——Qualcomm
- Timothy Miller——Traversal Technology
- Tom Forsyth——3Dlabs
- Tony Tamasi——3dfx 与 NVIDIA
- Trevor Wing——Video Logic

---

## 译注

1. 原文目录将本书章节标题列为 `History of the GPU`，而当前 PDF 的正文目录将第一章列为 `Introduction`；本译文暂按正文目录和章节内容分别处理，待后续整理完整章节时统一核对。
2. 原文中的 `2D story` 是作者对线性叙事的比喻，本译文译为“二维故事”，以保留原文表达。
3. 原文 `fixed-function` 译为“固定功能”，与 GPU 技术领域的常用译法一致。
4. 原文 `inflection points` 译为“转折点”；`disruptive results` 译为“颠覆性结果”。
5. 原文作者将自己的退休描述为 `a failed attempt at retiring`，本译文保留其自嘲语气，译为“一次未能成功的退休尝试”。
