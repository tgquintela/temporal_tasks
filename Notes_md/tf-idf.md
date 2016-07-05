
#TF-IDF
2016-06-01

TF-IDF (Term Frequency - Inverse Document Frequency) is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in information retrieval and text mining. The TF-IDF value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus. So it relates the specific more common words related to a document by considering also a correction for the most common words in all the documents.

Variations of the TF-IDF weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query. TF-IDF can be successfully used for stop-words filtering in various subject fields including text summarization and classification.

One of the simplest ranking functions is computed by summing the TF-IDF for each query term; many more sophisticated ranking functions are variants of this simple model.

TF-IDF is a product of two terms:
* Term Frequency: a term that describes the frequency of a word in a document. Depends on the problem this term could be binary, a count or a corrected count in order to save fat-tailed distributions and size dependencies, as the logaritmic scaled count.
* Inverse document frequency: term that describes how much information the word provides, that is, whether the term is common or rare across all documents. It is the logarithmically scaled inverse fraction of the documents that contain the word, obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient, or some similar corrected quotients.

***Tags***: Computer Science, Natural Language Processing, Information Retrieval

## Material
* http://radimrehurek.com/gensim/

## Papers
* Salton, G.; Buckley, C. (1988). [Term-weighting approaches in automatic text retrieval](). Information Processing & Management 24 (5): 513-523.
* Ramos, J. (2003). [Using tf-idf to determine word relevance in document queries](https://www.cs.rutgers.edu/~mlittman/courses/ml03/iCML03/papers/ramos.pdf). In Proceedings of the first instructional conference on machine learning.
* Aizawa, A. (2003). [An information-theoretic perspective of tf–idf measures](https://ccc.inaoep.mx/~villasen/index_archivos/cursoTL/articulos/Aizawa-tf-idfMeasures.pdf). Information Processing & Management, 39(1), 45-65.
* Chum, O., Philbin, J., & Zisserman, A. (2008). [Near Duplicate Image Detection: min-Hash and tf-idf Weighting](http://www.bmva.org/bmvc/2008/papers/119.pdf). In BMVC (Vol. 810, pp. 812-815).
* Tata, S., & Patel, J. M. (2007). [Estimating the selectivity of tf-idf based cosine similarity predicates](http://sigmod.org/publications/sigmodRecord/0706/p07.article-tata.pdf). ACM Sigmod Record, 36(2), 7-12.

## Books
* Baeza-Yates, R., & Ribeiro-Neto, B. (1999). [Modern information retrieval](https://www.goodreads.com/book/show/433444.Modern_Information_Retrieval). New York: ACM press.
* Manning, C. D., & Schütze, H. (1999). [Foundations of statistical natural language processing](https://www.goodreads.com/book/show/776349.Foundations_of_Statistical_Natural_Language_Processing). Cambridge: MIT press.
* Manning, C. D., & Raghavan, P. H. Schütze. (2009). [An introduction to information retrieval](https://www.goodreads.com/book/show/3278309-introduction-to-information-retrieval). Cambridge University Press
* Salton, G; McGill, M. J. (1986). [Introduction to modern information retrieval](https://www.goodreads.com/book/show/633362.Introduction_to_Modern_Information_Retrieval?from_search=true&search_version=service). McGraw-Hill.


