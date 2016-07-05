
#Hive
2016-06-01

Hive, formally known as Apache Hive, is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.

While developed by Facebook, Apache Hive is now used and developed by other companies such as Netflix and the Financial Industry Regulatory Authority (FINRA). Amazon maintains a software fork of Apache Hive that is included in Amazon Elastic MapReduce on Amazon Web Services.

Apache Hive supports analysis of large datasets stored in Hadoop's HDFS and compatible file systems such as Amazon S3 filesystem. 

It provides an SQL-like language called HiveQL with schema on read and transparently converts queries to MapReduce, Apache Tez and Spark jobs. All three execution engines can run in Hadoop YARN. To accelerate queries, it provides indexes, including bitmap indexes. Other features of Hive include:
* Indexing to provide acceleration, index type including compaction and Bitmap index as of 0.10, more index types are planned.
* Different storage types such as plain text, RCFile, HBase, ORC, and others.
* Metadata storage in an RDBMS, significantly reducing the time to perform semantic checks during query execution.
* Operating on compressed data stored into the Hadoop ecosystem using algorithms including DEFLATE, BWT, snappy, etc.
* Built-in user defined functions (UDFs) to manipulate dates, strings, and other data-mining tools. Hive supports extending the UDF set to handle use-cases not supported by built-in functions.
* SQL-like queries (HiveQL), which are implicitly converted into MapReduce or Tez, or Spark jobs.

Four file formats are supported in Hive, which are TEXTFILE, SEQUENCEFILE, ORC and RCFILE. Apache Parquet can be read via plugin in versions later than 0.10 and natively starting at 0.13. Additional Hive plugins support querying of the Bitcoin Blockchain.

***Tags***: Computer science, Data Analysis, Big Data, Hadoop ecosystem

### See also
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Machine learning](/machine_learning), [Artificial Intelligence](/artificial_intelligence), [Spatial Data Analysis](/spatial_data_analysis), [Data Analysis](/data_analysis)
## Material
* https://hive.apache.org/

## Books
* EMC editor (2014) [Data Science and Big Data Analytics: Discovering, Analyzing, Visualizing and Presenting Data](https://www.goodreads.com/book/show/22263956-data-science-and-big-data-analytics). John Wiley & Sons.


