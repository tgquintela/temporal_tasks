
#Semantic Hashing
2016-06-01

Semantic hashing uses a word-count vectors obtained from a large set of documents and traines a deep graphical model using semantic information and maps up to the 4th layer where are represented addresses space.
Documents are mapped to memory addresses in such a way that semantically similar documents are located at nearby addresses. Documents similar to a query document can then be found by simply accessing all the addresses that differ by only a few bits from the address of the query document. Unlike sparse distributed memory which operates on 1000-bit addresses, semantic hashing works on 32 or 64-bit addresses found in a conventional computer architecture.

***Tags***: Computer Science, Information Retrieval

### See also
[Locality Sensitive Hashing](/locality_sensitive_hashing)
## Papers
* Salakhutdinov, R., & Hinton, G. (2007). [Semantic hashing](). RBM, 500(3), 500.


