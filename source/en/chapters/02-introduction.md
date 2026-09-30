# Chapter 1

# Introduction

> Source: *The History of the GPU – Steps to Invention*  
> Printed pages: 1–29  
> PDF pages in the complete source: 29–58  
> Raw chapter PDF: [`../raw/02-introduction.pdf`](../raw/02-introduction.pdf)

## 1.1 Introduction

Over the years, the computer’s central processing unit (CPU) eventually incorporated every coprocessor developed to augment and add to its function except for one major processor, the GPU. A GPU is a specialized processor developed initially to accelerate graphics rendering and geometry transformations.

The CPU has even incorporated graphics processing. However, the CPU has not terminated the GPU’s stand-alone value as it did with floating-point processors, digital signal processors (DSPs), video codecs, and other accelerators. The GPU survives as a stand-alone coprocessor because it scales almost infinitely—adding transistors to create thousands of processor cores. The only asymptote a GPU might face is inter-processor communications. Clustering groups of processors (shaders) overcomes that barrier. Coherent caches have also scaled well and address the GPU’s inter-processor communications bottleneck. GPUs have been a significant beneficiary of Moore’s law [3], which postulates that the number of transistors on a chip doubles and cuts the price in half approximately every 1.5 to 2 years.

The GPU is a wonderful device and has made tremendous contributions to the computer’s capabilities.

GPUs can process data simultaneously, which is known as parallel processing. As a result, GPUs are used in applications beyond gaming and simulation. Applications as far-ranging as artificial intelligence (AI), machine learning (ML), CAD, and compute-intensive tasks use GPUs. GPUs have been used as accelerators for photo and video editing and high-performance computers (HPC) and supercomputers.

GPUs were initially stand-alone discrete hardware units (dGPU). Later, in 2010, they were added to the CPU (iGPU) but still held their place as a stand-alone device. GPUs can contain specialized AI elements and multimedia accelerators for video and audio, and ray-tracing accelerators. As the GPU advanced beyond its original role as a graphics processor and found use in pure computing applications not requiring a display, its additional capabilities have been called General-Purpose GPU (GPGPU), or GPU compute (cGPU). It is a false term because there is nothing general-purpose about a GPU. It cannot run an operating system, manage disk drives and peripherals, or boot up a system, nor is there anything general-purpose about a parallel processor. Those are the jobs of the CPU. GPUs are specialized devices with specific and specialized parallel-processing capabilities.

The terms semiconductor, integrated circuit (IC), and chip will be used interchangeably in this book and should be considered synonyms.

What does a GPU do? It is almost everything needed to calculate in parallel, from geometry processing to image processing to AI training and accelerated computing. Computer graphics is about geometry; as Pixar cofounder Alvy Ray Smith says in his book *A Biography of the Pixel*, “Computer graphics is geometry in, pixels out” [4]. There is much more to the GPU, however. Image processing is pixels in, pixels out, whereas AI training and compute acceleration are data in, data out—and a GPU does all of that and more.

And David Kasik of Boeing says:

> I consider computer graphics to be about creating, displaying, and modifying visual content to communicate to others. The sources are much broader than geometry: cameras, simulations, brain waves, sounds, etc. All forms of data can have a visual manifestation.

The integration of the rendering engine and the transformation and lighting (T&L) engine into a graphics controller, converting it into a GPU, was done to solve a geometry problem. Therefore, you will find a lot of discussion about geometry but no math in this book.

Transformation and lighting are critical components of computer graphics and the GPU. Transform means converting the coordinates of a 3D model to the coordinates of the viewing or display device. The coordinates are described by the vertices of objects in a scene. Lighting refers to the simulation of light in a scene—on the objects in a scene—and the effect of light from one object on another and on the scene. It is a complicated process.

As will be explained in later chapters, the GPU will find its way into general compute applications as a parallel processor, totally devoid of any graphics functions. Graphics processing units were developed for three-dimensional (3D) computer-graphics applications, first for CAD and then for games. The historical development of computer graphics gives an overview of the influences that heralded the development and invention of the GPU. The following is an overview of those developments, which will provide a foundation for appreciating the GPU’s development and evolution.

## Displays and Pixels

In computer graphics and digital imaging, a pixel is the smallest addressable element in a raster image, or the smallest addressable element in a digital display such as an LCD. A pixel is not addressable in geometry. Geometry is at the front end of a processing pipeline and the output is a raster scan, sized to a specific physical display and measured in pixels.

A GPU’s primary function is to drive a display, although GPUs used for compute acceleration do not drive a display. GPUs and graphics controllers before them deliver pixel information to a display in a serial manner, a few bits at a time. Displays used for graphics evolved from stroke or vector writers, also known as calligraphic displays, to TV-like raster-scan displays, and then to digital displays in flat panels.

Vector displays drew straight lines from one point to another on a screen. With the introduction of low-cost computers, scan-line cathode-ray-tube (CRT) TV displays were adopted. They sweep a beam across the screen and turn the beam on or off to make the screen light up. When the beam reached the right side, it snapped back to the left, moved slightly lower, and began the next scan line. Thus, a CRT’s resolution was measured by how many scan lines it could display. When digital computers began using CRTs, the beam was turned on or off at specific intervals across the scan line, corresponding to data in a frame buffer. That became known as raster graphics, and the operation became known as a raster scan.

The term raster is used to describe the display process and the construction of an image; the latter is referred to as raster graphics or bitmapped graphics. A bitmapped image is a digital image whose usually square pixels form a quantized display, as illustrated in Fig. 1.1.

A raster-display resolution is measured by the number of pixels in a row multiplied by the number of rows. Thus, a high-definition display has dimensions of 1920 pixels per row by 1080 rows, or 2.07 million pixels (commonly called two megapixels, written as 2 Mpix).

The output stage of a GPU is referred to as a rasterizer.

<div align="center">

![Fig. 1.1 A raster graphics display consists of quantized elements known as pixels](../images/chapter-01-fig-02.jpeg)

*Fig. 1.1 A raster graphics display consists of quantized elements known as pixels*

</div>
## 1.2 First Computer Graphics System (1949)

Most people attribute the start of interactive 3D graphics in computers to the Sketchpad project at MIT in 1963 by Ivan Sutherland. However, General Motors started DAC-1 in 1959–1960 as an interactive surface-design system. Sketchpad itself was a 2D system that introduced concepts still in use today, such as constraint-based sketching and masters and instances. Tim Johnson developed a 3D version, Sketchpad III, in 1964 [5].

The first electronic stored-program computer built was the Small-Scale Experimental Machine (SSEM), called Baby. Frederic C. Williams, Tom Kilburn, and Geoff Tootill constructed it at the University of Manchester. The first program ran on it on June 21, 1948 [6]. Baby was designed to use and demonstrate data stored on a cathode-ray tube (CRT), which became known as a Williams tube. The tube could remember 2048 bits. The system proved that it was practical to read and write data reliably at a speed suitable for use in a computer.

### The First Digital Display was in 1948

Baby had a small oscilloscope-like display tube that could display alphanumeric data. It did not draw lines at any angle, but clever graphics images were created with the dot-matrix screen.

In the United States, the Office of Naval Research and the U.S. Air Force funded the Whirlwind project to develop a large-scale digital machine for arduous real-time calculations such as aircraft simulation and air-traffic control.

<div align="center">

![Fig. 1.2 The small-scale experimental machine (SSEM), called Baby, was built at the University of Manchester in June 1948](../images/chapter-01-fig-03.jpeg)

*Fig. 1.2 The small-scale experimental machine (SSEM), called Baby, was built at the University of Manchester in June 1948*

</div>
<div align="center">

![Fig. 1.3 Baby’s dot-matrix display](../images/chapter-01-fig-04.jpeg)

*Fig. 1.3 Baby’s dot-matrix display*

</div>
### The First Animated Computer Graphic (1949)

Begun at the Servomechanisms Laboratory at MIT in 1944 under the direction of Jay Forrester, Whirlwind and Forrester were moved to the Digital Computer Laboratory and began focusing on using the computer for air-traffic-control and gunfire-control graphics displays. Forrester’s project became part of the government’s Semi-Automatic Ground Environment (SAGE) program. SAGE, in turn, was part of the Navy’s Airplane Stability and Control Analyzer (ASCA) project. The system was planned as a programmable flight-simulation environment and demonstrated in 1951 [7].

### Programmable Flight Simulation (1951)

Construction of the Whirlwind computer began in 1948 and employed 175 people, including seventy engineers and technicians. By the third quarter of 1949, the computer was advanced enough to solve an equation and display its solution on an oscilloscope; it was even used for the first animated and interactive computer-graphics game, *Blackjack* [8].

### The Whirlwind was the First Digital Computer Used for Computer Graphics

Whirlwind was the first to use video displays for output and operate in real time. It was not merely an electronic replacement for older mechanical systems [9]. Whirlwind used new core memory for random-access memory (RAM), making it the first computer to do so. The SAGE air-defense system became operational in 1958 with more advanced display capabilities.

<div align="center">

![Fig. 1.4 Whirlwind—the first interactive digital computer. Stephen Dodd (sitting), Jay Forrester, Robert Everett, and Ramona Ferenz at Whirlwind I, test-control display in the Barta Building, 1950 (Courtesy of The MITRE Corporation)](../images/chapter-01-fig-05.jpeg)

*Fig. 1.4 Whirlwind—the first interactive digital computer. Stephen Dodd (sitting), Jay Forrester, Robert Everett, and Ramona Ferenz at Whirlwind I, test-control display in the Barta Building, 1950 (Courtesy of The MITRE Corporation)*

</div>
The SAGE air-defense system, which drew heavily on experience with Whirlwind, also incorporated interactive graphics consoles and light “guns” in the 1950s to simulate and track the position of enemy bombers [10]. Robert Everett designed an input device that he called a light gun or light pen. It gave operators a means of obtaining identification information about an aircraft. When the light gun was pointed at a screen icon representing a plane, the pen detected the light from the screen and sent an interrupt to Whirlwind. Whirlwind then displayed text about the plane’s identification, speed, and direction [11].

### First 3D Perspective Computer-Generated Images in 1960

William Fetter at Boeing produced a 3D perspective drawing in 1960 and made an animation of an airplane cockpit. He also coined the term *computer graphics* along with Verne Hudson [12]. In Fetter’s book *Computer Graphics in Communication*, he describes drawing a series of x and y positions and having the computer connect them as straight-line segments [13]. 2D line drawings were made on large 30-inch screens derived from oscilloscopes and radar screens.

### Straight Lines (1962)

In early 1962, a senior technical staff member at IBM, Jack Elton Bresenham (PhD, Stanford University, 1964), developed the line-drawing algorithm named after him [14]. Its original application was x-y pen plotters such as Calcomp. Unlike interactive calligraphic displays, pen plotters could move or draw to one of eight positions using stepper motors that moved a small, fixed distance. The problem was computing the direction in which to move the pen for each step.

Early versions were slow and expensive because they required multiplication and division. Bresenham’s algorithm worked in integer coordinates and did not require multiplication or division, making it faster than other approaches. Drawing lines on a plotter using Bresenham’s algorithm was a significant accomplishment. The same technique applies to today’s raster displays.

In 1963, while a graduate student at MIT, Ivan Sutherland developed and demonstrated a 2D drawing program named Sketchpad. Sketchpad was a 2D drawing system for constraint-based engineering drawings. It was not 3D, but it showed how effective interactive computer graphics could be [15].

<div align="center">

![Fig. 1.5 Using a light gun on a SAGE air-defense screen to pick a target aircraft (Courtesy of IBM)](../images/chapter-01-fig-06.jpeg)

*Fig. 1.5 Using a light gun on a SAGE air-defense screen to pick a target aircraft (Courtesy of IBM)*

</div>
<div align="center">

![Fig. 1.6 3D perspective drawing created by William Fetter at Boeing (Courtesy of McGraw-Hill)](../images/chapter-01-fig-07.jpeg)

*Fig. 1.6 3D perspective drawing created by William Fetter at Boeing (Courtesy of McGraw-Hill)*

</div>
<div align="center">

![Fig. 1.7 Ivan Sutherland demonstrating Sketchpad (Courtesy of Wikipedia)](../images/chapter-01-fig-08.jpeg)

*Fig. 1.7 Ivan Sutherland demonstrating Sketchpad (Courtesy of Wikipedia)*

</div>
Computers had had calligraphic screens since the 1950s, when MIT developed the first real-time Whirlwind computer. In the early 1960s, RMS, a small test-equipment company, ventured into developing and manufacturing a completely transistorized character generator. That led the company to change its name to Information Displays, Inc. (IDI). At IDI, Carl Machover, Kenneth King, and Alfred Pestone developed the IDIIOM system for Britain’s National Engineering Laboratories (NAL) in 1963.

The IDIIOM was the first stand-alone CAD platform. According to the company, it was the first general-purpose design workstation, the first commercial CADD platform, and the first software drafting package to operate on its own computer without communication links to a mainframe. Unlike today’s GPU-based systems that rapidly generate bitmaps, IDI display systems employed vector controls. Machover commented:

> In the early 1960s, we operated in a vector world. Raster was not a common computer graphics display: the cost of memory to store the bitmap was enormous. Most early computer graphics systems were all stroke writers, or vector writers. Not raster. Raster did not become a broadly used technology until the late 1960s and early 1970s when the cost of storing bitmaps went down. Until that point, the deflection amplifiers, which you used with stroke writers, were very powerful and needed kilowatts to operate. They also needed high speeds. And the resulting cost of monitors was consistently too high [17].

Calligraphic screens dominated until the mid-1980s, when raster devices became the primary interactive-display technique. By 1968, systems such as Adage and Vector General, with general-purpose 4 × 4 matrix-transformation capabilities, clipping, and perspective divide, became available. Shortly afterward, IBM, Evans and Sutherland, and other companies announced commercial systems with real-time manipulation of 3D wireframe models with perspective.

<div align="center">

![Fig. 1.8 The first stand-alone workstation, IDI’s IDIIOM, with calligraphic screen and light pen (Courtesy of IEEE)](../images/chapter-01-fig-09.jpeg)

*Fig. 1.8 The first stand-alone workstation, IDI’s IDIIOM, with calligraphic screen and light pen (Courtesy of IEEE)*

</div>
<div align="center">

![Fig. 1.9 An engineer using a light pen on a Control Data 274 Digigraphics vector-display terminal, circa 1965 (Courtesy of the Charles Babbage Institute Archives, University of Minnesota Libraries)](../images/chapter-01-fig-10.jpeg)

*Fig. 1.9 An engineer using a light pen on a Control Data 274 Digigraphics vector-display terminal, circa 1965 (Courtesy of the Charles Babbage Institute Archives, University of Minnesota Libraries)*

</div>
The displays evolved too, and lower-cost raster displays based on TV technology replaced the large, expensive vectorscopes. Raster, also known as scan-line screens, created a foundation for graphics controllers and established a standard image method. Raster displays came into prominence in the late 1970s and early 1980s and received their most significant boost with the introduction of the IBM PC in 1981.

### The Term Pixel Introduced (1965)

Frederic Crockett Billingsley [18], an American engineer, developed digital image-processing techniques to support U.S. space probes to the Moon, Mars, and other planets. In 1965, Billingsley published two papers using the word *pixel* and may have been the first to publish the neologism for picture element (pix-el) [19, 20].

### First Tablet and Workstation (1972)

The Alto handheld-computer project began in late 1972. Alan Kay led the project at Xerox’s Palo Alto Research Center (PARC). Alto was a test bed for Kay’s ideas for the now-famous Dynabook tablet design [21]. However, Kay realized that the technology did not yet exist to develop a complete tablet computer. He correctly forecast that the technology would not be available until the end of the century. Kay saw Alto as a vision or rallying call for others who might later evolve it into a fully fledged Dynabook.

Most technology historians agree that the first workstation was developed at Xerox PARC in 1972, when Project Alto launched a personal computer for research.

### Game Console Introduced (1972)

Magnavox’s Odyssey was the first commercially available home video-game console. It set the stage for Atari and others. A small team at Sanders Associates led by Ralph H. Baer [22] designed the Odyssey for Magnavox. It was completed and released in the United States in September 1972. The Odyssey consisted of a central console, known as the Brown Box, connected to a television and two rectangular controllers.

### The Personal Computer (1975)

Lamont Wood traces the introduction of the first PC to 1970 with the Datapoint 2200 [23]. It was a small, stand-alone office computer and was not intended for consumers. The Mark-8 microcomputer, designed by Jonathan Titus in 1974, was the first computer consumers could play with. It used the Intel 8008 processor. Shortly afterward, MIT completed its prototype, the Altair 8800 microcomputer. Titus’s original name for the computer was PE-8, in honor of *Popular Electronics* magazine.

### The Genesis of the GPU—Pixel Planes (1980–2000)

The Pixel Planes project in 1980 was the foundation project that led to the GPU. The need to generate 3D images for protein research led to the development of a system called Pixel Planes at the University of North Carolina (UNC) in 1980. It was a new concept for designing graphics hardware that allocated one processor per pixel, meaning that many parts of the images on the screen could be generated simultaneously, vastly improving the speed at which programs could produce graphics. Work on Pixel Planes, under the direction of Henry Fuchs, continued at UNC through 1997, when the project’s final iteration, PixelFlow, was developed.

Calligraphic graphics terminals were the primary devices for displaying CAD drawings and other line-art images through the late 1970s and early 1980s. Microcomputer-based raster displays from companies such as Commodore, Radio Shack, and others lacked computing power.

The story of the GPU begins with the introduction of the first very-large-scale-integration (VLSI) graphics controller, developed by Nippon Electric Company (NEC) in 1982. This VLSI semiconductor chip lit up the industry and was used in CAD terminals, PCs, and client-server display systems. Before its arrival, graphics controllers used in terminals were large circuit boards with dozens of discrete logic and memory chips.

One of the most popular graphics terminals of the time was the Tektronix 4014. It was designed and built before the venerable NEC 7220 chip. Like its peers, it had circuit boards with dozens of logic chips and memory. The 4014 did not perform computation on the terminal; all projections and transformations were done on an attached minicomputer or mainframe.

<div align="center">

![Fig. 1.10 A Tektronix graphics-terminal system board (Courtesy of Legalizeadulthood)](../images/chapter-01-fig-11.jpeg)

*Fig. 1.10 A Tektronix graphics-terminal system board (Courtesy of Legalizeadulthood)*

</div>
### 3D Graphics in Games (1983)

The 3D polygonal game *I, Robot* [24, 25], released by Atari in 1983, was the first to be produced and sold commercially. The shaded 3D-game genre emerged in 1992 with *Wolfenstein 3D*. Inspired by Muse Software’s 2D video games *Castle Wolfenstein* and *Beyond Castle Wolfenstein*, the PC DOS version was released on May 5, 1992. Critics and game journalists widely regard it as popularizing the genre on the PC and establishing the basic run-and-shoot archetype for subsequent first-person-shooter (FPS) games.

<div align="center">

![Fig. 1.11 Wolfenstein 3D was the first PC-based 3D first-person shooter (Courtesy of Software & Apogee Software 1992 id)](../images/chapter-01-fig-12.jpeg)

*Fig. 1.11 Wolfenstein 3D was the first PC-based 3D first-person shooter (Courtesy of Software & Apogee Software 1992 id)*

</div>
### Shaders (1988)

Shading software, also known as shaders, calculates rendering effects such as lighting, colors, reflections and shadows, position, and other image-enhancement functions. Pixar introduced the term *shader* in May 1988 in its RenderMan Interface Specification. Early shaders ran on CPUs. Subsequent graphics processors provided specialized hardware with just enough capability to run shaders directly in the graphics pipeline. The first graphics hardware device with built-in shader capabilities was the Nvidia GeForce 3 (NV20), released on February 27, 2001. It could process only pixel shaders. Soon afterward, GPUs supported vertex shaders. A vertex shader manages the raw geometry of a 3D model and converts it into the coordinate space of the display. The pixel shader manages the pixel’s visibility and coloring.

## 1.3 The Graphics Processor Unit (1999)

Today’s GPU is quite different from the first graphics controllers of the 1970s and 1980s. Modern GPUs combine multiple stages and are beneficiaries of VLSI. By 1985, graphics controllers, the GPU’s predecessors, had become heterogeneous in their functions, adding audio and video (AV) capabilities. Then, in the early 1990s, integrated graphics processors (IGPs) appeared in CPU chipsets.

### SGI Introduced the First GPU for Consoles in 1996

Arcade-game system boards had hardware T&L as early as 1993—the Sega Model 2 by Real3D—and video-game consoles had it since the Nintendo 64’s Reality Coprocessor GPU, created by SGI in 1996. PCs implemented T&L in software until 1999.

### The Term GPU was Introduced in 1997 by 3Dlabs

Jim Clark introduced the first integrated geometry engine in 1981. In 1997, UK-based 3Dlabs developed the first dedicated programmable T&L engine; they called it the Glint Gamma processor. Transform and lighting were part of the Glint workstation graphics chips. 3Dlabs first introduced the term GPU—geometry processor unit—with the Glint chip.

While Glint was developed for the workstation market as a coprocessor, Nvidia introduced the GeForce 256, a single-chip graphics processor with a T&L engine, for the consumer market in 1999. The company popularized the term GPU to mean graphics processor unit. The company has been associated with it ever since and is credited with inventing the GPU.

### Nvidia Built the First Single-Chip PC GPU in 1999

GPUs have a wide range of applications, providing computing power for fields as diverse as industrial design, scientific computing, finance, aerospace, biomedicine, autonomous driving, and data centers. Their computing power has grown dramatically and given them a dominant role in games and movies. Due to the high technical threshold and significant investment needed, companies such as Advanced Micro Devices (AMD), Intel, and Nvidia have long dominated the GPU market.

The specific defining moment of the first GPU is difficult to determine. Multiple dates could constitute “first”: the date the project started, the date the prototype worked, the announcement date, the date the first part shipped, or the date the first end user obtained one. Because the only one of those dates that every company consistently uses is the announcement, this book uses the announcement date.

### 1.3.1 The Evolution of Graphics Controllers to GPUs

The evolutionary path from a primary 2D display controller to today’s GPU had several steps or phases that were not necessarily linear. Except for some phase shifts, it generally looked like the diagram shown in Fig. 1.12.

At the 1994 COMDEX conference, Intel’s founder and chairman Andy Grove said, “We need to achieve built-in multimedia and communications capability ... ahead of this information conduit coming our way. Otherwise, it will turn into a debilitating situation for us.” Yet Intel did not integrate video or graphics until 2010, and serious audio processing did not appear until 2016. GPUs integrated those functions in the late 1990s and early 2000s.

In 2006, Nvidia introduced its proprietary parallel-programming software derived from C++, called CUDA—compute unified device architecture. CUDA is a software layer that gives direct access to the GPU’s virtual instruction set and parallel computational elements for executing compute kernels.

### Tessellation, AI, and Ray Tracing (2000–2020)

Software developers moved specialized computer-graphics operations that had previously run on the CPU to dedicated hardware accelerators within the GPU. Because of that change, those functions ran far faster. It was a blend of Moore’s law and putting processors where performance called for them. AMD introduced hardware tessellation in 2001. In 2018, Nvidia introduced hardware AI and accelerated ray tracing. Then, in 2020, Nvidia introduced Ampere, the largest GPU ever made at that time—38 billion transistors, 8192 processors, and hundreds of other specialized processors.

<div align="center">

![Fig. 1.12 The evolutionary path of the GPU](../images/chapter-01-fig-13.jpeg)

*Fig. 1.12 The evolutionary path of the GPU*

</div>
### Mesh Shading (2016–2020)

GPU development never slowed. In 2016 AMD introduced primitive shaders in its Graphics Core Next (GCN) Vega GPU. In 2018 Nvidia introduced mesh-shader capability in its Turing GPU. In response, Microsoft introduced DirectX 12 Ultimate in May 2020, allowing software developers to exploit the hardware developments.

Shortly afterward, Epic released a mesh-shading demo on the new PlayStation 5. It showed images containing billions of subpixels in real time [26]. The visuals were stunning and used what Epic called Nanite virtualized micropolygon geometry. This new level-of-detail geometry would free artists to create polygon detail beyond what the eye could see.

<div align="center">

![Fig. 1.13 The entire image above was calculated; it is not a photograph or texture map (Courtesy of Epic Games, Nanite demo)](../images/chapter-01-fig-14.jpeg)

*Fig. 1.13 The entire image above was calculated; it is not a photograph or texture map (Courtesy of Epic Games, Nanite demo)*

</div>
## 1.4 Performance (2000–2026)

Over most of the history of GPUs, vendors have battled over performance figures. Graphics quality is often subjective, so how do you convince customers that a closely matched product is better than the competition? Performance.

Computer and computer-graphics performance are measured in several ways. No single method is best or most correct; the choice depends on what matters to the user and the user’s level of understanding. GigaFLOPS—billions of floating-point operations per second—is a useful option because it is an empirical measurement used with different platforms for comparison.

For this book, giga floating-point operations per second (GFLOPS) also helps tell the story. Performance improvements over time are shown in Fig. 1.14, and there is an apparent leveling-off in gains. Several observers have commented that Moore’s law is slowing down. Remember that Moore’s law is an economic observation: the slowdown is true because it becomes more expensive to obtain performance improvements as processor counts rise. Photolithography and other manufacturing equipment have their own kind of inverse Moore’s law—as process size shrinks, equipment costs double. That delays new process nodes and parts.

Practical limitations also inspire innovative ways to extract more performance from nanometer- and angstrom-sized transistors: architectural techniques involving caches, multichip designs, 3D memory stacking, new materials, and, most of all, software.

<div align="center">

![Fig. 1.14 Performance of popular platforms over time](../images/chapter-01-fig-15.jpeg)

*Fig. 1.14 Performance of popular platforms over time*

</div>
## 1.5 The GPU’s Changing Role

With the introduction of VLSI graphics controllers, costs came down, demand increased, and production went up. Twenty years later, VLSI chips with millions of transistors and parallel processors entered the market labeled as graphics processor units—GPUs.

GPUs replaced all the logic on the Tektronix circuit board apart from memory and a few input/output chips. More importantly, they added new and more robust functionality at a fraction of the cost of system boards.

Since its introduction, the GPU has evolved, becoming more programmable and more of a compute platform than a specialized graphics engine. As a result, it is now central to the progress of digital technology. Although it may always be used as a graphics engine, it has taken on other roles and added specialized compute engines for AI and ray tracing.

Hardware-design tools have also evolved. Designers have introduced tools that are easy to install and use, including tools that run in a web browser and are free. Prototyping boards have become more available, with off-the-shelf boards from Raspberry Pi, micro:bit, and others. Online storefronts, accessible design tools, consultancies, collaborators, crowdfunding, incubators, and next-day delivery networks have reduced time and cost, and reduced risk for new projects in established and start-up companies [27].

Those tools and services do not guarantee success; many new hardware products, especially consumer products, have failed. A working prototype is only the start. The other challenge is capital: in-house projects and start-ups need materials and manufacturing equipment. Crowdfunding has offset some financial obstacles. Open-source intellectual property (IP) has also helped organizations develop products by reusing sections or functions that are not the value-added portion of a new design but are needed for a functional unit.

Most or all of these infrastructure and tool improvements are because of the GPU. The GPU is even used to create more advanced GPUs.

Designers created powerful GPUs in the late 1990s for two applications: CAD and 3D gaming on a PC. By then, the CAD market was smaller than the gaming market, but it still accounted for millions of users whose processing demands were growing. The larger gaming market provided economies of scale for consumer GPU suppliers, allowing them to offer devices at economical prices. At the beginning of the twenty-first century, computer scientists recognized the cost-effectiveness of GPUs as parallel processors. Consumer GPUs became accessible with their own software-development environments and showed the potential to solve challenging computing problems.

<div align="center">

![Fig. 1.15 Nvidia’s GeForce 256, the first single-chip GPU (Courtesy of Konstantin Lanzet, Wikipedia)](../images/chapter-01-fig-16.jpeg)

*Fig. 1.15 Nvidia’s GeForce 256, the first single-chip GPU (Courtesy of Konstantin Lanzet, Wikipedia)*

</div>
<div align="center">

![Fig. 1.16 GPUs have become ubiquitous and accelerated science, resulting in new products, enhanced vehicle safety, and many other applications](../images/chapter-01-fig-17.jpeg)

*Fig. 1.16 GPUs have become ubiquitous and accelerated science, resulting in new products, enhanced vehicle safety, and many other applications*

</div>
## 1.6 The GPU’s Application

Because of the redundancy of processors in a GPU, also called shaders, computer architects and engineers saw that the GPU would be highly scalable, making it suitable for applications and price points beyond gaming. As the application base broadened, new programming languages emerged to make GPUs easier to use. Today’s GPUs are more efficient than ever, accelerate a broader range of applications, and have become as ubiquitous as the CPU and the display. GPUs are not just for gaming anymore.

### 1.6.1 AI and Machine Learning

AI and ML offer some of the most exciting applications for a GPU. AI applies machine learning, deep learning, and other techniques to solve real problems. Computer scientist and ML pioneer Tom M. Mitchell defined machine learning as “the study of computer algorithms that allow computer programs to automatically improve through experience” [28].

Because of a GPU’s single-instruction, multiple-data (SIMD) construction, it offers exceptional capability for processing massive amounts of data. That makes it useful for image recognition, recommendation systems, and database indexing. Massive-data processing is possible as long as the CPU–GPU data path is sufficiently fast and the algorithms can be implemented in parallel.

AI and ML use deep-learning techniques and deconvolutional neural networks (DNNs) to create extensive data sets that could take years for conventional CPUs to process. A GPU can work through that data in minutes, giving researchers answers sooner and enabling them to ask the next question, thereby speeding scientific and medical research.

### 1.6.2 Accelerated Computing and Supercomputers

Some challenges involve enormous quantities of data that share attributes. Credit-card transactions are one example: hundreds of millions of people use credit cards every day, and computers must complete transactions, check for fraud, and verify funds in seconds.

Scientists and engineers create simulations of viruses and vehicles with millions to trillions of data points. Those points are stressed and tested, and the effect on adjacent points is equally important. Such analyses must happen as quickly as possible. A typical comment among engineers and scientists is, “I need an answer before I retire or die.”

GPUs are used as accelerator coprocessors in supercomputers. They accelerate specific and specialized parts of a problem; they are not used for general-purpose work, system operations, or overhead functions.

### 1.6.3 Content Creation

The first graphics processors drew lines for engineering drawings using CAD. CAD was the first digital-content-creation (DCC) application and remains essential. Drawing lines is relatively simple; shading the areas within those lines so that they look and behave realistically and accurately is complicated. Today GPUs are prominent in video editing, rendering, and extraordinary special effects.

Later applications involved animations and simulations of actors, imagined space, ancient sailing ships, tigers, and ants coming to life. Film, television, and today’s games tax the GPU in every possible way.

### 1.6.4 Gaming

Because so many people play video games, gaming has always been a significant computer application. Gaming appeared on computers as early as 1949 [29]. Video games, especially adventure and first-person-world games, are massive simulations. Simulating and rendering such environments evolved beyond the capabilities of a single CPU. Developed as coprocessors, graphics processors offloaded the main CPU and took on the arduous task of rendering elaborate scenes and actions. Such games require thirty to sixty frames per second, and now often 120.

Gaming propelled GPU development to new heights as demand for realism and speed increased. Games became computationally intensive, with realistic images and massive worlds. GPUs developed alongside increasingly complex games and high-resolution displays reaching 5K and 8K, with the promise of 16K. The burden such displays place on the GPU rises exponentially.

### 1.6.5 Molecular Modeling

Molecular modeling is the use of a computer to study molecules and their properties. In the 1960s, scientists and chemists made wireframe visualizations of molecules on large CRT screens and pen plotters.

MIT developed the first interactive display of molecular structures in the mid-1960s. It ran on Project MAC (Multi-Access Computer), an early time-sharing mainframe. Cyrus Levinthal [30] and colleagues designed a model-building program for protein structures.

Molecular structures were appealing for developing computer-graphics tools because the data were relatively easy to create and the results were visually pleasing. Molecular graphics are useful for representing global and local properties such as electrostatic potential. Models can also be animated to represent molecular processes and chemical reactions.

### 1.6.6 Video and Photo Editing

Imaging, including photo editing, was an early GPU application. Digitized photos and computer-generated images have always pushed processing limits as artists and photographers manipulate every pixel to create effects, correct blemishes, and remove elements.

In video, the first genuinely nonlinear editor was the analog CMX 600, introduced in 1971 by CMX Systems, a joint venture between CBS and Memorex. The concept moved to computers and enabled the digital nonlinear video-editing (DNLE) era in the early 1990s. The first DNLE was Quantel’s *Harry*, released in 1985, the first all-digital video-editing and effects-compositing system.

Modern GPUs have dedicated video compression and decompression (codec) engines, providing video-creation and playback capabilities more efficiently. GPUs have also been used in transcoding, converting one video format into another. AMD and Intel have built dedicated transcoding engines into their CPUs that can be even more efficient.

### 1.6.7 Vehicle Navigation and Robots

Because GPUs can consume and compute results for large quantities of data, they are ideal for processing the inputs needed by autonomous vehicles. Autonomous robots are similar. GPUs are useful in every phase, from concept through simulation and testing to deployment as device controllers.

### 1.6.8 Crypto Mining

In late 2015, monitoring transactions based on cryptocurrencies such as Ethereum used graphics add-in boards (AIBs) to brute-force search for transactions. This practice is called mining or crypto mining. As cryptocurrency values rose relative to the U.S. dollar, demand for AIBs increased, driving up prices, distorting the market, and causing shortages. In 2021, Nvidia introduced a class of GPUs called the Cryptocurrency Mining Processor (CMP), leading to the term “mining GPU” (mGPU). The goal was to ensure that GeForce AIBs went to gamers and smooth supply and demand.

### 1.6.9 Summary

The preceding sections briefly recapped applications in which GPUs are used. The list will continue to expand as adjacent markets see the advantage of massive parallel processing. There may be fifty or more applications in AI alone; the examples above summarize some of the most prominent.

## 1.7 The Many Roles of the GPU Require Additional Names

GPU use has spread to multiple platforms, and several naming schemes have become standardized:

- Category name—GPU, CPU, and APU.
- Architecture, also called microarchitecture—for example, AMD’s Radeon DNA (RDNA), Intel’s Xe, or Nvidia’s Ampere.
- Code name—for example, AMD’s Navi, Intel’s Arc, or Nvidia’s A40.
- Model name or number—for example, AMD’s Navi21 and Nvidia’s GA100.
- AIB brand and model—for example, AMD’s Radeon RX 6000, Intel’s Alchemist, or Nvidia’s RTX 3080 Ti.
- Generation—for example, AMD’s Radeon 6000 or Nvidia’s 3000. Generation names are not reliable because manufacturers change their naming schemes.

| Model name | Product name | Architecture name |
|---|---|---|
| NV04 | Riva TNT, TNT2 | Fahrenheit |
| NV10 | GeForce 256, GeForce 2, GeForce 4 MX | Celsius |
| NV20 | GeForce 3, GeForce 4 Ti | Kelvin |
| NV30 | GeForce 5 / GeForce FX | Rankine |
| NV40 | GeForce 6, GeForce 7 | Curie |
| NV50 | GeForce 8, 9, 100, 200, 300 | Tesla |
| NVC0 | GeForce 400, 500 | Fermi |
| NVE0 | GeForce 600, 700, GTX Titan | Kepler |
| NV110 | GeForce 750, 900 | Maxwell |
| NV130 | GeForce 1060, 1070 | Pascal |
| NV140 | Nvidia Titan V | Volta |
| NV160 | GeForce RTX 2060, GTX 1660 | Turing |
| NV170 | GeForce RTX 3060, RTX 3070 | Ampere |

AIB marketing names have been Radeon for AMD, Arc for Intel, and GeForce for Nvidia. It has become common, although incorrect, to refer to an AIB as a GPU. The terms have become interchangeable for many consumers and reporters. This is like referring to a car as the motor. The term *card* is also frequently used for an AIB. AIB is more specific and descriptive and is the convention used in this book.

The original purpose of the GPU was to accelerate the graphics pipeline for games and CAD visualization. Displaying 3D models requires geometry processing and matrix mathematics, followed by rendering to determine each pixel’s color. Rendering shows effects such as transparency, reflection, and smoothness. Both tasks are served by high-speed parallel processing. The algorithms that determine rendering colors using GPU processors became known as shaders.

### Shaders and Processors

The term *shaders* has become synonymous with *processor*. People refer to the number of shaders in a GPU, or to a fixed-function processor as a tessellation shader. Strictly speaking, a shader is a program running on a processor, and sometimes the term is applied to a fixed-function processor. The distinction is not always respected, so parallel processors in a GPU are commonly called shaders.

SIMD is the type of architecture used in a GPU. CISC (complex instruction set computer) is the type of architecture used in an x86 CPU. RISC (reduced instruction set computer) is used in mobile-device CPUs. GPU and CPU architectures are given names, such as AMD RDNA, Intel Golden Cove, and Nvidia Hopper.

Architectural designs may be used in several versions or generations and given code names, such as AMD Navi, Intel Alder Lake, or Nvidia Ampere. Models or versions can form a family, such as AMD Radeon, Intel Core, and Nvidia RTX. GPUs are mounted on graphics AIBs or on a PC system board, also called a motherboard or mobo. Each AIB is given a brand and model name, such as AMD Radeon RX 6000, Intel Core nth-Gen, or Nvidia RTX 3080.

<div align="center">

![Fig. 1.17 Taxonomy of names](../images/chapter-01-fig-18.jpeg)

*Fig. 1.17 Taxonomy of names*

</div>

The mass-produced GPU quickly reached an economy of scale comparable to that of the x86 processor. It became recognized as a cost-effective processor with massive computing density. Soon it was used as a compute accelerator. Over time, GPU-based systems moved into the top ten of the 500 fastest supercomputers. Once there, they never left.

GPUs were then integrated into x86 CPUs and ARM-based systems-on-chip (SoCs) as shared-memory GPUs.

### The First eGPU was by ATI in 2008

As laptops became thinner and lighter, the power and space needed for a powerful GPU became problematic. Designers developed systems with high-speed connections for GPUs, such as PCI Express (PCIe). The complexity of cabling, connectors, and line drivers proved expensive and cumbersome. Fujitsu offered a PCIe product called the Amilo GraphicsBooster [32].

The introduction of Thunderbolt and then USB-C made external GPUs practical. USB-C could carry PCIe signals over a low-cost, high-bandwidth cable and connector, making an external AIB/GPU a practical docking option. The additional enclosure and power supply nevertheless increased the price.

## 1.8 Types of GPUs

The GPU has evolved across several platforms and applications while sharing instruction-set architectures (ISAs) and application-programming interfaces (APIs). Lower-case prefixes distinguish GPU types and have been generally accepted by industry:

- **dGPU**—a discrete, stand-alone processor with its own private high-speed memory; dGPUs are on AIBs and notebook system boards.
- **iGPU**—a scaled-down version with fewer processors than a discrete GPU, using shared local RAM with the CPU.
- **vGPU**—a virtual GPU on an AIB with a powerful dGPU located remotely in the cloud or on a campus server.
- **mGPU**—a GPU used by crypto miners, later called CMP, a cryptocurrency-mining GPU.
- **eGPU**—an external AIB with a dGPU in a stand-alone enclosure, used as a graphics booster and notebook docking station. The term can also refer to embedded GPUs and ExpressCard GPUs [33].

ATI was the first company to demonstrate the eGPU concept, showing its External Graphics Port (XGP) in 2008 as an external GPU enclosure attached to a laptop.

GPUs are found in PCs as dGPUs and iGPUs, often both at once; in smartphone and tablet SoCs; in game consoles; in vehicles; and as computer accelerators in supercomputers and servers. They are also found in aircraft and ship cockpits, AR and VR systems, cameras, digital-cinema projectors, robots, scientific instruments, toys, home-security devices, TVs, and visualization and simulation systems.

The GPU grew out of a need for faster and more realistic games, but the GPU market is far from a game. It is mission-critical, with high demands, high stakes, extraordinary development, and advances exceeding Moore’s law by orders of magnitude.

<div align="center">

![Fig. 1.18 GPUs are found in many types of systems and have different prefixes](../images/chapter-01-fig-19.jpeg)

*Fig. 1.18 GPUs are found in many types of systems and have different prefixes*

</div>
<div align="center">

![Fig. 1.19 The problems with segmentations and names](../images/chapter-01-fig-20.jpeg)

*Fig. 1.19 The problems with segmentations and names*

</div>
Getting terminology right is a challenge. The same name can apply to multiple things, and the same thing can have multiple names. It is the tyranny of terminology [34].

## 1.9 Conclusion

This chapter introduced the history of the GPU and some of the many terms used to describe a GPU and its environment. GPUs have been with us since the turn of the century, but they did not suddenly appear like dandelions. The need for a GPU began in the 1960s. At that time there was no term for it, only a desire.

Computer graphics has always been limited by memory. In the 1960s, memory was more precious than the CPU. Today, memory is less expensive per unit than the processors it serves. Even so, 32 GB of RAM can represent almost a third of the price of an AIB, so memory is still not cheap—only more available and reliable.

GPUs are remarkable devices, but VLSI and Moore’s law made them possible.

## References

1. Redmond, K. C. and Smith, T. M. *Project Whirlwind: The History of a Pioneer Computer*. Bedford, MA, Digital Press. ISBN 0-932376-09-6. (1980)
2. Canning, C. “Predicting the Past.” *The Lark*, April 5, 2017. https://www.larktheatre.org/blog/predicting-past/
3. “Moore’s law.” *Moore’s law – Wikipedia*. https://en.wikipedia.org/wiki/Moore%27s_law
4. Smith, A. R. *A Biography of the Pixel*. MIT Press. https://mitpress.mit.edu/books/biography-pixel (August 3, 2021)
5. Yares, E. “50 years of CAD.” *Design*, February 13, 2013. https://www.designworldonline.com/50-years-of-cad/
6. “The Manchester Small Scale Experimental Machine – ‘The Baby’.” http://curation.cs.manchester.ac.uk/computer50/www.computer50.org/mark1/new.baby.html
7. Committee on Innovations in Computing and Communications: Lessons from History, National Research Council. *Funding a Revolution: Government Support for Computing Research*. The National Academies Press. ISBN-10: 0-309-06278-0 (1999).
8. Fedorkow, G. “Gambling On Whirlwind: How The US Navy Spent $3 Million+ And Got A Computer Game.” Computer History Museum, October 22, 2019. https://computerhistory.org/blog/gambling-on-whirlwind-how-the-us-navy-spent-3-million-and-got-a-computer-game/
9. Peddie, J. “Developing the Computer.” In *The History of Visual Magic in Computers*, Springer Nature Switzerland AG, pp. 148–158 (2013).
10. Jacobs, J. F. *The SAGE Air Defense System: A Personal History*. MITRE Corporation (1986).
11. Carlson, W. E. *Computer Graphics and Computer Animation: A Retrospective Overview*. Ohio State University (2017). https://ohiostate.pressbooks.pub/graphicshistory/
12. Oppenheimer, R. “William Fetter, E.A.T., and 1960s Computer Graphics Collaborations in Seattle” (2005). https://www.academia.edu/7801224/William_Fetter_E_A_T_and_1960s_Computer_Graphics_Collaborations_in_Seattle
13. Fetter, W. A. *Computer Graphics in Communication*. McGraw-Hill, first edition (January 1, 1965). https://openlibrary.org/works/OL7390788W/Computer_graphics_in_communication
14. Bresenham, J. E. “Algorithm for computer control of a digital plotter.” *IBM Systems Journal*, vol. 4, issue 1 (1965). https://ieeexplore.ieee.org/document/5388473
15. Kasik, D. and Senesac, C. J. “Visualization: Past, Present, and Future at The Boeing Company” (2014). http://gpdisonline.com/wp-content/uploads/past-presentations/DX28_Boeing-Kasik-Senesac-Visualization-DX-Open.pdf
16. Bissell, Don. “Was the IDIIOM the First Stand-Alone CAD Platform?” *IEEE Annals of the History of Computing*, vol. 20, issue 2, April–June 1998. https://ieeexplore.ieee.org/cart/download.jsp?partnum=667292&searchProductType=IEEE%20Journals%20Magazines
17. Don Bissell’s March 14, 1997 interview with Carl Machover.
18. Billingsley, C. B. https://en.wikipedia.org/wiki/Frederic_C._Billingsley
19. Billingsley, C. B. “Digital Video Processing At JPL.” SPIE, volume 0003 (September 26, 1965).
20. Richard, L. “Pixels and Me.” Lecture. https://www.youtube.com/watch?v=D6n2Esh4jDY
21. “Dynabook.” https://history-computer.com/products/dynabook-complete-history-of-the-dynabook-computer/
22. Martin, D. “Ralph H. Baer, Inventor of First System for Home Video Games, Is Dead at 92.” *New York Times*, December 7, 2014. https://www.nytimes.com/2014/12/08/business/ralph-h-baer-dies-inventor-of-odyssey-first-system-for-home-video-games.html
23. Wood, L. *Datapoint: The Lost Story of the Texans Who Invented the Personal Computer Revolution*. Hugo House Publishing, Ltd., Englewood, CO (2010).
24. “I, Robot – Videogame by Atari.” *Killer List of Videogames* (1983). Retrieved August 19, 2009.
25. “I, Robot (arcade game).” http://en.wikipedia.org/wiki/I,_Robot_(arcade_game)
26. “A first look at Unreal Engine 5.” June 15, 2020. https://www.unrealengine.com/en-US/blog/a-first-look-at-unreal-engine-5
27. Hodges, S. and Chen, N. “Long Tail Hardware: Turning Device Concepts Into Viable Low Volume Products.” *IEEE Pervasive Computing*, vol. 18, issue 4, October–December 2019. https://doi.org/10.1109/MPRV.2019.2947966
28. Iriondo, Roberto. “Machine Learning (ML) vs. Artificial Intelligence (AI)—Crucial Differences.” https://medium.com/towards-artificial-intelligence/differences-between-ai-and-machine-learning-and-why-it-matters-1255b182fc6
29. Peddie, J. “Developing the Applications.” In *History of Visual Magic in Computers: How Beautiful Images are Made in CAD, 3D, VR, and AR*, p. 81. Springer, London (2013).
30. Francoeur, E. “Cyrus Levinthal, the Kluge and the Origins of Interactive Molecular Graphics.” *Endeavour*, vol. 26, no. 4 (2002). https://tinyurl.com/995uczze
