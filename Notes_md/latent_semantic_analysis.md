
#Latent Semantic Analysis
2016-06-01

Latent semantic analysis (LSA) is a technique in natural language processing, in particular distributional semantics, of analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. LSA assumes that words that are close in meaning will occur in similar pieces of text. So the process will be:
* Build a matrix containing word counts per paragraph (rows represent unique words and columns represent each paragraph) is constructed from a large piece of text
* Use SVD to reduce the number of rows while preserving the similarity structure among columns. 
* Words are then compared by taking the cosine of the angle between the two vectors (or the dot product between the normalizations of the two vectors) formed by any two rows. Values close to 1 represent very similar words while values close to 0 represent very dissimilar words.

An information retrieval technique using latent semantic structure was patented in 1988 (US Patent 4,839,853, now expired) by Scott Deerwester, Susan Dumais, George Furnas, Richard Harshman, Thomas Landauer, Karen Lochbaum and Lynn Streeter. In the context of its application to information retrieval, it is sometimes called Latent Semantic Indexing (LSI).

***Tags***: Computer Science, Information Retrieval, Natural Language Processing

#### See also
[Latent Dirichlet Allocation](/latent_dirichlet_allocation)
## Material
* http://radimrehurek.com/gensim/
* [Latent Semantic Analysis, a scholarpedia article on LSA written by Tom Landauer](http://www.scholarpedia.org/article/Latent_semantic_analysis), one of the creators of LSA.

## Papers
* Landauer, Thomas; Foltz, Peter W.; Laham, Darrell (1998). [Introduction to Latent Semantic Analysis](http://tottdp.googlecode.com/files/LandauerFoltz-Laham1998.pdf). Discourse Processes 25 (2-3): 259-284.
* Deerwester, Scott; Dumais, Susan T.; Furnas, George W.; Landauer, Thomas K.; Harshman, Richard (1990). [Indexing by Latent Semantic Analysis](http://www.cob.unt.edu/itds/faculty/evangelopoulos/dsci5910/LSA_Deerwester1990.pdf). Journal of the American Society for Information Science 41 (6): 391-407.
* Dumais, S. T. (2004). [Latent semantic analysis](http://onlinelibrary.wiley.com/doi/10.1002/aris.1440380105/abstract). Annual review of information science and technology, 38(1), 188-230.
* Hofmann, T. (1999). [Probabilistic latent semantic analysis](http://arxiv.org/pdf/1301.6705). In Proceedings of the Fifteenth conference on Uncertainty in artificial intelligence (pp. 289-296). Morgan Kaufmann Publishers Inc.
* Shu, Liangcai; Long, Bo; Meng, Weiyi (2009). [A Latent Topic Model for Complete Entity Resolution](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.156.6463&rep=rep1&type=pdf). 25th IEEE International Conference on Data Engineering (ICDE 2009).
* Hofmann, T. (2001). [Unsupervised learning by probabilistic latent semantic analysis](http://www.kmklaw.com/assets/attachments/Unsupervised%20Learning%20by%20Probabilistic%20Latent%20Semantic%20Analysis.pdf). Machine learning, 42(1-2), 177-196.

## Books
* Landauer, T. K., McNamara, D. S., Dennis, S., & Kintsch, W. (2013). [Handbook of latent semantic analysis](https://www.goodreads.com/book/show/517158.Handbook_of_Latent_Semantic_Analysis). Psychology Press.
* Loehlin, J. C. (1998). [Latent variable models: An introduction to factor, path, and structural analysis](https://www.goodreads.com/book/show/5164960-latent-variable-models). Lawrence Erlbaum Associates Publishers.
* Hagenaars, J. A., & McCutcheon, A. L. (Eds.). (2002). [Applied latent class analysis](https://www.goodreads.com/book/show/2859314-applied-latent-class-analysis). Cambridge University Press.


