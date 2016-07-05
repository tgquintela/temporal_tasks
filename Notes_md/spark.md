
#Spark
2016-06-01

Apache Spark is an open source cluster computing framework. Originally developed at the University of California, Berkeley's AMPLab, the Spark codebase was later donated to the Apache Software Foundation that has maintained it since. Spark provides an interface for programming entire clusters with implicit data parallelism and fault-tolerance.

Apache Spark provides programmers with an application programming interface centered on a data structure called the resilient distributed dataset (RDD), a read-only multiset of data items distributed over a cluster of machines, that is maintained in a fault-tolerant way. It was developed in response to limitations in the MapReduce cluster computing paradigm, which forces a particular linear dataflow structure on distributed programs: MapReduce programs read input data from disk, map a function across the data, reduce the results of the map, and store reduction results on disk. Spark's RDDs function as a working set for distributed programs that offers a (deliberately) restricted form of distributed shared memory.

The Spark project has 5 main parts:
* _Spark Core_: which is the foundation of the overall project. It provides distributed task dispatching, scheduling, and basic I/O functionalities, exposed through an application programming interface (for Java, Python, Scala, and R) centered on the RDD abstraction.
* _Spark SQL_: which is a component on top of Spark Core that introduces a new data abstraction called DataFrames,[a] which provides support for structured and semi-structured data. Spark SQL provides a domain-specific language to manipulate DataFrames in Scala, Java, or Python. It also provides SQL language support, with command-line interfaces and ODBC/JDBC server.
* _Spark Streaming_: which leverages Spark Core's fast scheduling capability to perform streaming analytics. It ingests data in mini-batches and performs RDD transformations on those mini-batches of data. This design enables the same set of application code written for batch analytics to be used in streaming analytics, on a single engine.
* _Spark MLlib_: which is a distributed machine learning framework on top of Spark Core that, due in large part of the distributed memory-based Spark architecture, is as much as nine times as fast as the disk-based implementation used by Apache Mahout (according to benchmarks done by the MLlib developers against the Alternating Least Squares (ALS) implementations, and before Mahout itself gained a Spark interface), and scales better than Vowpal Wabbit. Many common machine learning and statistical algorithms have been implemented and are shipped with MLlib which simplifies large scale machine learning pipelines.
* _GraphX_: which  is a distributed graph processing framework on top of Apache Spark. It provides an API for expressing graph computation that can model the Pregel abstraction. It also provides an optimized runtime for this abstraction.

***Tags***: Computer science, Data Analysis, Big Data, Hadoop ecosystem

### See also
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Machine learning](/machine_learning), [Artificial Intelligence](/artificial_intelligence), [Spatial Data Analysis](/spatial_data_analysis), [Data Analysis](/data_analysis)
## Material
* https://spark.apache.org/
* https://spark.apache.org/sql/
* https://spark.apache.org/streaming/
* https://spark.apache.org/mllib/
* https://spark.apache.org/graphx/
* http://www.datascienceassn.org/content/data-locality-hpc-vs-hadoop-vs-spark
* Harris, Derrick (28 June 2014). [4 reasons why Spark could jolt Hadoop into hyperdrive](https://gigaom.com/2014/06/28/4-reasons-why-spark-could-jolt-hadoop-into-hyperdrive/)
* http://www.slideshare.net/chaochen5496/mlllib-sparkmeetup8613finalreduced/
* https://intellipaat.com/tutorial/spark-tutorial/

## Papers
* Zaharia, Matei, et al. [Spark: Cluster Computing with Working Sets](https://amplab.cs.berkeley.edu/wp-content/uploads/2011/06/Spark-Cluster-Computing-with-Working-Sets.pdf). HotCloud 10 (2010): 10-10.

## Books
* EMC editor (2014) [Data Science and Big Data Analytics: Discovering, Analyzing, Visualizing and Presenting Data](https://www.goodreads.com/book/show/22263956-data-science-and-big-data-analytics). John Wiley & Sons.
* Karau, Holden; Konwinski, Andy; Wendell, Patrick; Zaharia, Matei (2015) [Learning Spark: Lightning-Fast Big Data Analysis](https://www.goodreads.com/book/show/24808098-learning-spark). 2nd Edition, O'Reilly Media
* Hamstra, Mark; Zaharia, Matei (2014). [Learning Spark](https://www.goodreads.com/book/show/17318146-learning-spark). 2nd Edition, O'Reilly Media
* Karau, Holden (2013). [Fast Data Processing with Spark](https://www.goodreads.com/book/show/19666515-fast-data-processing-with-spark). Packt Publishing
* Karau, Holden; Warren, Rachel. (2016) [High Performance Spark: Best Practices for Scaling and Optimizing Apache Spark](https://www.goodreads.com/book/show/28321014-high-performance-spark). O'Reilly Media


