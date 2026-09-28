# Foreword

> Source: *The History of the GPU – Steps to Invention*  
> Printed pages: v–vii  
> PDF pages in the complete source: 5–7  
> Raw chapter PDF: [`../raw/00-foreword.pdf`](../raw/00-foreword.pdf)

## Printed page v

History often elicits strong responses whether it is studied in school, the subject of documentary films and books, or passed orally from generation to generation. No matter the source, no history can cover every event for any one person. My own memory demonstrates that daily.

I believe that history is an essential subject. Understanding what happened in the past gives insight into what worked and (perhaps more importantly) what didn't work and why. In addition, history provides context for current events. We learn from history in important ways.

Computing itself is a relatively new field. Many science and engineering fields are significantly older and their history has been documented extensively. There are substantive debates about what counts as the first digital computer. Suffice it to say that digital computers are not much more than 100 years old.

Computer graphics is an even newer field. It integrates disparate display technologies, digital and analog computers, and a human's innate capability to see pictures on a flat screen. Verne Hudson from Boeing-Wichita coined the term circa 1960. His collaborator, Bill Fetter, popularized it.

Jon's book complements a spate of recent publications devoted to the history of different aspects of computer graphics. Books by Peddie, Masson, and Carlson describe the field in general. Smith traces the evolution of the pixel. Llach looks at graphics in building and architecture, Weisberg the history of CAD, and Gaboury the influence of the University of Utah. This is just a sampling.

What I find interesting about the authors is that many are intimately involved with the field rather than historians per se. A number of them are pioneers or students of pioneers who have first-hand knowledge of the history they are documenting. These authors write with both authority and immediacy.

This book provides a broad view of the graphics processing unit. Jon has been involved with special purpose graphics processing technology since day one. He does an excellent job documenting processors dedicated to generating better images faster. Like any history, it's not complete. The book does provide a coherent, well-organized view of the evolution of a valuable technology. Jon emphasizes how GPUs evolved from custom processors devoted to picture generation to general-purpose parallel

## Printed page vi

processors. It provides context that helps the reader better understand how GPUs fit into the computer graphics world.

I was totally unaware of Hudson and Fetter and the existence of computers and computer graphics until the late 1960s. I didn't enter high school until 1962. My curriculum included Latin, Greek, and little science. Therefore, I could barely spell "computer." Ironically, I retired from Boeing as a Senior Technical Fellow in visualization and interactive techniques after a 35-year career.

The computer graphics bug bit me as a Johns Hopkins undergrad in 1969. Bill Huggins, who had spent his sabbatical learning computer animation with Bell Labs pioneers, recruited me to make computer-animated educational films. The process was arduous. It involved punched cards, line printer keyframes, a microfilm recorder (located in Brooklyn NY), an assembly language animation "language," and an IBM 7094 mainframe. There were no interactive devices for animators/programmers, no color output, no shaded images, and no sound. Just white lines on a black background. And I loved it!

My early career let me create more animated films and learn about interactive graphics at Battelle-Columbus Labs. I became aware that a digital computer can display one frame at a time whether the frame is part of a projected film or displayed on a graphics screen. The human visual system does the rest and gives a person the illusion of continuous motion as long as each image is shown quickly enough.

For the film, a projector shows frames fast enough (24–30 Hz) to make the motion seem continuous. Images on interactive device screens must be redrawn at the same rate or faster. Current interactive devices established a redraw rate at 60+ Hz. The requirement to draw new frames interactively ultimately led to the work with GPUs. A film may take compute-centuries to produce enough frames for a full-length animated film. Projectors are responsible for showing the frames fast enough.

GPUs help reduce compute-centuries for a film to something more reasonable by improving overall throughput. Interactivity pushes compute performance even harder. In today's interactive graphics world, GPUs must compute a completely new frame fast enough to create the illusion of continuous motion. Put another way, the image generation compute task, the task GPUs perform, must determine the color of each pixel on each frame fast enough to convince the human visual system that image transformations (either 2D or 3D) are continuous.

My work at Boeing emphasized acceptable interactive performance. I was able to work at a Boeing scale (interactively working with the complete digital design of a commercial airplane like a 787, ~2 billion polygons) on a GPU-equipped PC to make end-users think the task was easy. I often measure success by making the difficulty of complicated behind-the-scenes tasks seem simple when in actual use.

I think Jon's discussion about GPU evolution to become a generalized parallel processor adds real value. It confirms my belief that the most successful and powerful technologies are those that can be generalized and applied to problems the original developers never foresaw. GPUs fit that profile.

## Printed page vii

Pay careful attention to the lessons learned from GPU evolution and generalization. Those lessons can be applied to the reader's own work. And understand how forthcoming generations of GPUs can be extended to provide even more value in the future.

Sammamish, WA, USA  
D. J. Kasik  
June 2022

## Source notes

- The page break between “parallel” and “processors” is retained so the Markdown can be checked against the printed source pages.
- The source PDF contains an extracted character anomaly in the original `24–30 Hz` range; this cleaned Markdown restores the range using the visible context and the PDF text extraction.
- The cleaned Markdown preserves paragraph and page structure but is not a facsimile of the PDF layout.
