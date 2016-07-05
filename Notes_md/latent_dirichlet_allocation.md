
#Latent Dirichlet Allocation
2016-06-01

Latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar. In the case of NLP, if observations are words collected into documents, it posits that each document is a mixture of a small number of topics and that each word's creation is attributable to one of the document's topics. 

In LDA, each document may be viewed as a mixture of various topics. This is similar to probabilistic latent semantic analysis (pLSA), except that in LDA the topic distribution is assumed to have a Dirichlet prior. In practice, this results in more reasonable mixtures of topics in a document. It has been noted, however, that the pLSA model is equivalent to the LDA model under a uniform Dirichlet prior distribution.

### Formalization
The model is formed by the elements:
* {\displaystyle \alpha} is the parameter of the Dirichlet prior on the per-document topic distributions,
* {\displaystyle \beta} is the parameter of the Dirichlet prior on the per-topic word distribution,
* {\displaystyle \theta _{i}} is the topic distribution for document i,
* {\displaystyle \varphi _{k}} is the word distribution for topic k,
* {\displaystyle z_{ij}} is the topic for the jth word in document i, and
* {\displaystyle w_{ij}} is the specific word.

The generative model is expressed by:

$${\displaystyle P({\boldsymbol {W}},{\boldsymbol {Z}},{\boldsymbol {\theta }},{\boldsymbol {\varphi }};\alpha ,\beta )=\prod _{i=1}^{K}P(\varphi _{i};\beta )\prod _{j=1}^{M}P(\theta _{j};\alpha )\prod _{t=1}^{N}P(Z_{j,t}|\theta _{j})P(W_{j,t}|\varphi _{Z_{j,t}})}$$

using the assumptions of the distributions.

LDA is an example of a topic model and was first presented as a graphical model for topic discovery by David Blei, Andrew Ng, and Michael I. Jordan in 2003. Essentially the same model was also proposed independently by J. K. Pritchard, M. Stephens, and P. Donnelly in the study of population genetics in 2000.

***Tags***: Computer Science, Information Retrieval, Natural Language Processing

### See also
[Latent Semantic Analysis](/latent_semantic_analysis)
## Material
* http://radimrehurek.com/gensim/
* [LDA and Topic Modelling Video Lecture by David Blei](http://videolectures.net/mlss09uk_blei_tm/) or [same lecture on YouTube](https://www.youtube.com/watch?v=DDq3OVp9dNA/)
* [LDA in Mahout implementation of LDA using MapReduce on the Hadoop platform](https://mahout.apache.org/users/clustering/latent-dirichlet-allocation.html)
* [LDA in Spark: Since version 1.3.0](https://spark.apache.org/docs/latest/mllib-clustering.html#latent-dirichlet-allocation-lda)

## Papers
* Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). [Latent dirichlet allocation](http://www.jmlr.org/papers/v3/blei03a.html). Journal of machine Learning research, 3(Jan), 993-1022.
* Griffiths, Thomas L.; Steyvers, Mark (April 6, 2004). [Finding scientific topics](http://www.pnas.org/content/101/suppl_1/5228.short). Proceedings of the National Academy of Sciences 101 (Suppl. 1): 5228-5235.
* Hoffman, M., Bach, F. R., & Blei, D. M. (2010). [Online learning for latent dirichlet allocation](http://papers.nips.cc/paper/3902-online-learning-for-latentdirichlet-allocation!). In advances in neural information processing systems (pp. 856-864).
* Blei, David M.; Lafferty, John D. (2006). [Correlated topic models](http://galton.uchicago.edu/~lafferty/pdf/ctm.pdf). Advances in Neural Information Processing Systems 18.
* Teh, Y. W., Newman, D., & Welling, M. (2006). [A collapsed variational Bayesian inference algorithm for latent Dirichlet allocation](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2006_511.pdf). In Advances in neural information processing systems (pp. 1353-1360).
* Krestel, R., Fankhauser, P., & Nejdl, W. (2009, October). [Latent dirichlet allocation for tag recommendation](https://www.researchgate.net/profile/Ralf_Krestel/publication/221141032_Latent_dirichlet_allocation_for_tag_recommendation/links/02e7e51e42a994f415000000.pdf). In Proceedings of the third ACM conference on Recommender systems (pp. 61-68). ACM.
* Wang, Xiaogang; Grimson, Eric (2007). [Spatial Latent Dirichlet Allocation](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2007_102.pdf). Proceedings of Neural Information Processing Systems Conference (NIPS).
* Lancichinetti, A., Sirer, M. I., Wang, J. X., Acuna, D., Körding, K., & Amaral, L. A. N. (2015). [High-reproducibility and high-accuracy method for automated topic classification](http://link.aps.org/pdf/10.1103/PhysRevX.5.011007). Physical Review X, 5(1), 011007.


