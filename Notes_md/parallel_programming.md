
#Parallel programming
2016-06-01

Parallel computing is a type of computation in which many calculations are carried out simultaneously, operating on the principle that large problems can often be divided into smaller ones, which are then solved at the same time. There are several different forms of parallel computing: bit-level, instruction-level, data, and task parallelism. Parallelism has been employed for many years, mainly in high-performance computing, but interest in it has grown lately due to the physical constraints preventing frequency scaling. As power consumption (and consequently heat generation) by computers has become a concern in recent years, parallel computing has become the dominant paradigm in computer architecture, mainly in the form of multi-core processors.

Parallel computing is closely related to concurrent computing, but they are NOT the same: it is possible to have parallelism without concurrency (such as bit-level parallelism), and concurrency without parallelism (such as multitasking by time-sharing on a single-core CPU). In parallel computing, a computational task is typically broken down in several, often many, very similar subtasks that can be processed independently and whose results are combined afterwards, upon completion. In contrast, in concurrent computing, the various processes often do not address related tasks; when they do, as is typical in distributed computing, the separate tasks may have a varied nature and often require some inter-process communication during execution.

Parallel computers can be roughly classified according to the level at which the hardware supports parallelism, with multi-core and multi-processor computers having multiple processing elements within a single machine, while clusters, MPPs, and grids use multiple computers to work on the same task. Specialized parallel computer architectures are sometimes used alongside traditional processors, for accelerating specific tasks.

In some cases parallelism is transparent to the programmer, such as in bit-level or instruction-level parallelism, but explicitly parallel algorithms, particularly those that use concurrency, are more difficult to write than sequential ones, because concurrency introduces several new classes of potential software bugs, of which race conditions are the most common. Communication and synchronization between the different subtasks are typically some of the greatest obstacles to getting good parallel program performance.
A theoretical upper bound on the speed-up of a single program as a result of parallelization is given by Amdahl's law.

### TODO:
* Amdahl's law
* embarrassing parallelism
* Consistency model
* Open MP
* MPI
* OpenHMPP

***Tags***: Computer engineering, Programming

### See also
[Programming paradigm](/programming_paradigm), [Concurrent programming](/concurrent_programming), [Amdahl's law](/amdahl's_law)
## Books
* Hwang, Kai (1992). [Advanced Computer Architecture: Parallelism, Scalability, Programmability](https://www.goodreads.com/book/show/688409.Advanced_Computer_Architecture). McGraw-Hill Science/Engineering/Math
* Hwang, Kai; Dongarra, Jack; Fox, Geoffrey C. (2011). [Distributed and Cloud Computing: Clusters, Grids, Clouds, and the Future Internet](https://www.goodreads.com/book/show/11230369-distributed-and-cloud-computing). Morgan Kaufmann


