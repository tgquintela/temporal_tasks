
#Locality Sensitive Hashing
2016-06-01

Locality-sensitive hashing (LSH) reduces the dimensionality of high-dimensional data, as it is the text data. LSH hashes input items so that similar items map to the same “buckets” with high probability (the number of buckets being much smaller than the universe of possible input items). LSH differs from conventional and cryptographic hash functions because it aims to maximize the probability of a “collision” for similar items. Locality-sensitive hashing has much in common with data clustering and nearest neighbor search.

***Tags***: Computer Science, Information Retrieval

#### See also
[Semantic Hashing](/semantic_hashing)
## Material
* [Python Locality Sensitive Hashing library that optionally supports persistence via redis](https://github.com/simonemainardi/LSHash)

## Papers
* Datar, M.; Immorlica, N.; Indyk, P.; Mirrokni, V.S. (2004). [Locality-Sensitive Hashing Scheme Based on p-Stable Distributions](http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p253-datar.pdf). Proceedings of the Symposium on Computational Geometry.
* Pauleve, L.; Jegou, H.; Amsaleg, L. (2010). [Locality sensitive hashing: A comparison of hash function types and querying mechanisms](https://hal.inria.fr/docs/00/56/71/91/PDF/paper.pdf). Pattern recognition Letters.
* Buhler, J. (2001). [Efficient large-scale sequence comparison by locality-sensitive hashing](http://bioinformatics.oxfordjournals.org/content/17/5/419.full.pdf). Bioinformatics, 17(5), 419-428.
* Slaney, M., & Casey, M. (2008). [Locality-sensitive hashing for finding nearest neighbors](http://web.iitd.ac.in/~sumeet/Slaney2008-LSHTutorial.pdf) [lecture notes]. IEEE Signal Processing Magazine, 25(2), 128-131.
* Kulis, B., & Grauman, K. (2012). [Kernelized locality-sensitive hashing](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6072216). IEEE Transactions on Pattern Analysis and Machine Intelligence, 34(6), 1092-1104.
* Satuluri, V., & Parthasarathy, S. (2012). [Bayesian locality sensitive hashing for fast similarity search](http://arxiv.org/pdf/1110.1328). Proceedings of the VLDB Endowment, 5(5), 430-441.
* Koga, H., Ishibashi, T., & Watanabe, T. (2007). [Fast agglomerative hierarchical clustering algorithm using Locality-Sensitive Hashing](http://link.springer.com/article/10.1007/s10115-006-0027-5). Knowledge and Information Systems, 12(1), 25-53.

## Books
* Rajaraman, A.; Ullman, J. (2010). [Mining of Massive Datasets](https://www.goodreads.com/book/show/12818088-mining-of-massive-datasets), Ch. 3. Cambridge University Press


