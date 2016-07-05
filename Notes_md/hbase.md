
#Hbase
2016-06-01

HBase, or Apache HBase, is an open source, non-relational, distributed database modeled after Google's BigTable and written in Java. It is developed as part of Apache Software Foundation's Apache Hadoop project and runs on top of HDFS (Hadoop Distributed Filesystem), providing BigTable-like capabilities for Hadoop. That is, it provides a fault-tolerant way of storing large quantities of sparse data (small amounts of information caught within a large collection of empty or unimportant data, such as finding the 50 largest items in a group of 2 billion records, or finding the non-zero items representing less than 0.1% of a huge collection).

HBase features compression, in-memory operation, and Bloom filters on a per-column basis as outlined in the original BigTable paper. Tables in HBase can serve as the input and output for MapReduce jobs run in Hadoop, and may be accessed through the Java API but also through REST, Avro or Thrift gateway APIs. Hbase is a column-oriented key-value data store and has idolized widely because of its lineage with Hadoop and HDFS. HBase runs on top of HDFS and is well-suited for faster read and write operations on large datasets with high throughput and low input/output latency.

HBase is not a direct replacement for a classic SQL database, however Apache Phoenix project provides an SQL layer for Hbase as well as JDBC driver that can be integrated with various analytics and business intelligence applications. The Apache Trafodion project provides a SQL query engine with ODBC and JDBC drivers and distributed ACID transaction protection across multiple statements, tables and rows that uses HBase as a storage engine.

Hbase is now serving several data-driven websites, including Facebook's Messaging Platform. Unlike relational and traditional databases, HBase does not support SQL scripting instead written in Java employing similarity with MapReduce application.

***Tags***: Computer science, Data Analysis, Big Data, Hadoop ecosystem

#### See also
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Machine learning](/machine_learning), [Artificial Intelligence](/artificial_intelligence), [Spatial Data Analysis](/spatial_data_analysis), [Data Analysis](/data_analysis)
## Material
* http://hbase.apache.org/

## Papers
* Chang, et al. (2006). [Bigtable: A Distributed Storage System for Structured Data](https://www.usenix.org/legacy/events/osdi06/tech/chang/chang_html/) ACM Transactions on Computer Systems (TOCS) 26.2 (2008): 4.

## Books
* EMC editor (2014) [Data Science and Big Data Analytics: Discovering, Analyzing, Visualizing and Presenting Data](https://www.goodreads.com/book/show/22263956-data-science-and-big-data-analytics). John Wiley & Sons.
* George, Lars. (2011). [HBase: The Definitive Guide](https://www.goodreads.com/book/show/10316770-hbase). O'Reilly Media
* Dimiduk, Nick; Khurana, Amandeep (2012). [HBase in Action](https://www.goodreads.com/book/show/13507799-hbase-in-action). Manning Publications Co.
* Shriparv, Shashwat (2014). [Learning HBase](https://www.goodreads.com/book/show/24529152-learning-hbase). Packt Publishing


