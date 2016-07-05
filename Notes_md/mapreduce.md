
#MapReduce
2016-06-01

MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster. Conceptually similar approaches have been very well known since 1995 with the Message Passing Interface standard having reduce and scatter operations.
The "MapReduce System" (also called "infrastructure" or "framework") orchestrates the processing by marshalling the distributed servers, running the various tasks in parallel, managing all communications and data transfers between the various parts of the system, and providing for redundancy and fault tolerance.
The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the MapReduce framework is not the same as in their original forms. The key contributions of the MapReduce framework are not the actual map and reduce functions, but the scalability and fault-tolerance achieved for a variety of applications by optimizing the execution engine once.

A MapReduce program is composed of:
* _Map step_: Each worker node applies the "Map()" function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of redundant input data is processed. Map() is a procedure (method) that performs filtering and sorting (such as sorting students by first name into queues, one queue for each name).
* _Shuffle step_: Worker nodes redistribute data based on the output keys (produced by the "map()" function), such that all data belonging to one key is located on the same worker node.
* _Reduce step_: Worker nodes now process each group of output data, per key, in parallel. Reduce() is a method that performs a summary operation (such as counting the number of students in each queue, yielding name frequencies).

As such, a single-threaded implementation of MapReduce will usually not be faster than a traditional implementation; any gains are usually only seen with multi-threaded implementations. The use of this model is beneficial only when the optimized distributed shuffle operation (which reduces network communication cost) and fault tolerance features of the MapReduce framework come into play. Optimizing the communication cost is essential to a good MapReduce algorithm.

MapReduce libraries have been written in many programming languages, with different levels of optimization. A popular open-source implementation that has support for distributed shuffles is part of Apache Hadoop. The name MapReduce originally referred to the proprietary Google technology, but has since been generalized. By 2014, Google was no longer using MapReduce as their primary Big Data processing model, and development on Apache Mahout had moved on to more capable and less disk-oriented mechanisms that incorporated full map and reduce capabilities.

MapReduce could be not usable in some parallel solvable problems but for most of the problems could be used and save coding time between the developers.

***Tags***: Computer science, Data Analysis

#### See also
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Machine learning](/machine_learning), [Artificial Intelligence](/artificial_intelligence), [Spatial Data Analysis](/spatial_data_analysis), [Data Analysis](/data_analysis)
## Books
* Miner, Donald; Shook, Adam (2016). [MapReduce Design Patterns: Building Effective Algorithms and Analytics for Hadoop and Other Systems](https://www.goodreads.com/book/show/14514285-mapreduce-design-patterns). O'Reilly Media
* Miner, Donald (2016). [Hadoop : What you Need to Know](https://www.goodreads.com/book/show/30326744-hadoop). O'Reilly
* Jurney, Russell. (2013). [Agile Data Science: Building Data Analytics Applications with Hadoop](https://www.goodreads.com/book/show/15815177-agile-data-science). O'Reilly Media.
* Tannir, Khaled (2014). [Optimizing Hadoop for MapReduce](https://www.goodreads.com/book/show/20920720-optimizing-hadoop-for-mapreduce). Packt Publishing
* Holt, Bradley (2011). [Writing and Querying MapReduce Views in CouchDB](https://www.goodreads.com/book/show/10378832-writing-and-querying-mapreduce-views-in-couchdb). O'Reilly Media.
* Amazon Web Services. [Amazon Elastic MapReduce Developer Guide](https://www.amazon.com/Amazon-Elastic-MapReduce-Developer-Guide-ebook/dp/B007US6CIO?ie=UTF8&tag=duckduckgo-d-20). Kindle Edition
* Chalkiopoulos, Antonios (2014). [Programming Mapreduce with Scalding](https://www.goodreads.com/book/show/22632842-programming-mapreduce-with-scalding). Packt Publishing
* Lin, Jimmy; Dyer, Chris; Hirst, Graeme (2010). [Data-Intensive Text Processing with Mapreduce](https://www.goodreads.com/book/show/8346166-data-intensive-text-processing-with-mapreduce). Morgan & Claypool


