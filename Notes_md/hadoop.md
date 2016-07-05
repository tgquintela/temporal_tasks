
#Hadoop
2016-06-01

Hadoop, formaly known as Apache Hadoop, is an open-source software framework for distributed storage and distributed processing of very large datasets on computer clusters from commodity hardware. Apache ease the management of the related tasks of distribute computations in an optimal way and solving the problems related with random fails that it can occur. Hadoop is the main software solutions in the ecosystem of Big Data.

The core of Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part called MapReduce. Hadoop splits files into large blocks and distributes them across nodes in a cluster. To process data, Hadoop transfers packaged code for nodes to process in parallel based on the data that needs to be processed. This approach takes advantage of data locality- nodes manipulating the data they have access to- to allow the dataset to be processed faster and more efficiently than it would be in a more conventional supercomputer architecture that relies on a parallel file system where computation and data are distributed via high-speed networking.

The base Apache Hadoop framework is composed of the following modules:
* Hadoop Common: contains libraries and utilities needed by other Hadoop modules.
* Hadoop Distributed File System (HDFS): a distributed file-system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster.
* Hadoop YARN: a resource-management platform responsible for managing computing resources in clusters and using them for scheduling of users' applications.
* Hadoop MapReduce: an implementation of the MapReduce programming model for large scale data processing.

The term Hadoop has come to refer not just to the base modules above, but also to the ecosystem, or collection of additional software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Cloudera Impala, Apache Flume, Apache Sqoop, Apache Oozie, Apache Storm.

Apache Hadoop's MapReduce and HDFS components were inspired by Google papers on their MapReduce and Google File System.

The Hadoop framework itself is mostly written in the Java programming language, with some native code in C and command line utilities written as shell scripts. Though MapReduce Java code is common, any programming language can be used with "Hadoop Streaming" to implement the "map" and "reduce" parts of the user's program. Other projects in the Hadoop ecosystem expose richer user interfaces.

***Tags***: Computer science, Data Analysis, Big Data, Hadoop ecosystem

## See also
## See also:
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Machine learning](/machine_learning), [Artificial Intelligence](/artificial_intelligence), [Spatial Data Analysis](/spatial_data_analysis), [Data Analysis](/data_analysis)
## Material
* http://hadoop.apache.org/
* http://www.ibm.com/analytics/us/en/technology/hadoop/
* http://hortonworks.com/apache/hadoop/
* http://www.datascienceassn.org/content/data-locality-hpc-vs-hadoop-vs-spark

## Books
* EMC editor (2014) [Data Science and Big Data Analytics: Discovering, Analyzing, Visualizing and Presenting Data](https://www.goodreads.com/book/show/22263956-data-science-and-big-data-analytics). John Wiley & Sons.
* Lam, Chuck (2010). [Hadoop in Action](https://www.goodreads.com/book/show/7284874-hadoop-in-action). 1st Edition, Manning Publications.
* Venner, Jason (2009). [Pro Hadoop](https://www.goodreads.com/book/show/6863676-pro-hadoop). 1st Edition, Apress.
* White, Tom (2009). [Hadoop: The Definitive Guide](https://www.goodreads.com/book/show/6308439-hadoop). 1st Edition, O'Reilly Media.
* Sammer, Eric. (2012) [Hadoop Operations](https://www.goodreads.com/book/show/15744029-hadoop-operations). O'Reilly Media.
* Jurney, Russell. (2013) [Agile Data Science: Building Data Analytics Applications with Hadoop](https://www.goodreads.com/book/show/15815177-agile-data-science). O'Reilly Media.
* Owen, Sean; Anil, Robin; Dunning, Ted; Friedman, Ellen (2011). [Mahout in Action](https://www.goodreads.com/book/show/9546513-mahout-in-action). Manning Publications
* Hamstra, Mark; Zaharia, Matei (2014). [Learning Spark](https://www.goodreads.com/book/show/17318146-learning-spark). 2nd Edition, O'Reilly Media


