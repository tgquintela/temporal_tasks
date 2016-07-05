
#Unbalance data problem
2016-06-01

Unbalance data problem is the problem that the machine learning algorithms have to face in order to model data that have unbalance labels. That's there are a minority of classes that have little instances in comparison to the total of the dataset and the cost to miss in them is much lower to the majority class.

Most learning systems are not prepared to cope with unbalanced data and several techniques have been proposed to rebalance the classes. This package implements
some of most well-known techniques and propose a racing algorithm to select adaptively the most appropriate strategy for a given unbalanced task.

The most general basic methods are thought:
* Sampling: oversampling or undersampling in order to correct the biases.
	* Random undersampling: it is quicker, but you could lose important information.
	* Neighborhood cleaning rule (NCR): finds each data example whose class label differs from the class of at least two of its three nearest neighbors. If this example belongs to the majority class, remove it. Otherwise, remove its nearest neighbors which belong to the majority class.
	* Condensed Nearest Neighbor (CNN): selects the subset of instances that are able to correctly classifying the original datasets using a one-nearest neighbor rule. The goal is to eliminate examples from the majority class that are much further away from the border. Easy to model with balance and information important instances.
	* TOMEK links: the objective is removing the noise and borderline instances. That helps discriminatory algorithms easy to learn.
	* On-side selection: an undersampling method resulting from the application of Tomek links followed by the application of Condensed Nearest Neighbor. 
	* Random oversampling: replicate the minority class elements in order to rebalance the classes. Hurts the generalization property.
	* SMOTE: Nearest Neighbors jitterized-driven replication of the minority class.
	* Borderline-SMOTE: application of SMOTE and TOMEK links undersampling.

* Adapting learning algorithms (by changing decision thresholds or objective functions):
	* Boosting: meta-algortithm which uses weak learners to adaptively use a flexible learning of each point.
		* Standard Boosting:
		* AdaBoost: 
		* SMOTEBoost:
		* RUSBoost:   
* Ensemble methods: a proper weighted collection of learning algorithms.
* All combined: all the methods combined properly.


It is important to consider how noisy is the data and how many instances you have (or better, the information value per instance), or if there is heterogeneity value for instance (in order to data model) in the data. Regarding the previous information we have to select our methods. Direct properties that can conditioned this values are the overlap between classes and the density.

***Tags***: Data Science

## Material
* [imblanced-learn python package](http://glemaitre.github.io/UnbalancedDataset/index.html)

## Papers
* Dal Pozzolo, A., Caelen, O., Waterschoot, S., & Bontempi, G. (2013, October). [Racing for unbalanced methods selection](http://www.oliviercaelen.be/doc/Racing_unbalanced_IDEAL.pdf). In International Conference on Intelligent Data Engineering and Automated Learning (pp. 24-31). Springer Berlin Heidelberg.
* Birattari, M., Stützle, T., Paquete, L., & Varrentrapp, K. (2002, July). [A Racing Algorithm for Configuring Metaheuristics](https://www.researchgate.net/profile/Thomas_Stuetzle/publication/220740639_A_Racing_Algorithm_for_Configuring_Metaheuristics/links/0deec525c3e2125471000000.pdf). In GECCO (Vol. 2, pp. 11-18).
* Maron, O., & Moore, A. W. (1997). [The racing algorithm: Model selection for lazy learners](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.48.954&rep=rep1&type=pdf). In Lazy learning (pp. 193-225). Springer Netherlands.
* Searle, S. R. (1987). [Linear models for unbalanced data](http://www.sidalc.net/cgi-bin/wxis.exe/?IsisScript=ORTON.xis&method=post&formato=2&cantidad=1&expresion=mfn=051159) (No. 519.5352 S439). Wiley.
* Cieslak, D. A., & Chawla, N. V. (2008, September). [Learning decision trees for unbalanced data](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.151.3829&rep=rep1&type=pdf). In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (pp. 241-256). Springer Berlin Heidelberg.
* Tao, Q., Wu, G. W., Wang, F. Y., & Wang, J. (2005). [Posterior probability support vector machines for unbalanced data](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.452.1728&rep=rep1&type=pdf). IEEE Transactions on Neural Networks, 16(6), 1561-1573.
* Mani, I., & Zhang, I. (2003, August). [kNN approach to unbalanced data distributions: a case study involving information extraction](https://www.site.uottawa.ca/~nat/Workshop2003/jzhang.pdf). In Proceedings of workshop on learning from imbalanced datasets.
* Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). [SMOTE: synthetic minority over-sampling technique](http://www.jair.org/media/953/live-953-2037-jair.pdf). Journal of artificial intelligence research, 16, 321-357.
* Han, H., Wang, W. Y., & Mao, B. H. (2005, August). [Borderline-SMOTE: a new over-sampling method in imbalanced data sets learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.308.9315&rep=rep1&type=pdf). In International Conference on Intelligent Computing (pp. 878-887). Springer Berlin Heidelberg.
* Luengo, J., Fernández, A., García, S., & Herrera, F. (2011). [Addressing data complexity for imbalanced data sets: analysis of SMOTE-based oversampling and evolutionary undersampling](http://sci2s.ugr.es/sites/default/files/ficherosPublicaciones/1276_2011-luengo-fernandez-garcia-herrera-imbalanced-datacomplexity-SOCO.pdf). Soft Computing, 15(10), 1909-1936.
* Maciejewski, T., & Stefanowski, J. (2011, April). [Local neighbourhood extension of SMOTE for mining imbalanced data](http://www.cs.put.poznan.pl/jstefanowski/pub/LNSmote-CIDM2011.pdf). In Computational Intelligence and Data Mining (CIDM), 2011 IEEE Symposium on (pp. 104-111). IEEE.
* He, H., & Garcia, E. A. (2009). [Learning from imbalanced data](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=5128907&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D5128907). IEEE Transactions on knowledge and data engineering, 21(9), 1263-1284.
* Sun, Y., Kamel, M. S., Wong, A. K., & Wang, Y. (2007). [Cost-sensitive boosting for classification of imbalanced data](https://uwspace.uwaterloo.ca/bitstream/handle/10012/3000/thesis.pdf?sequence=1&isAllowed=y). Pattern Recognition, 40(12), 3358-3378.
* Provost, F. (2000, July). [Machine learning from imbalanced data sets 101](http://www.aaai.org/Papers/Workshops/2000/WS-00-05/WS00-05-001.pdf). In Proceedings of the AAAI’2000 workshop on imbalanced data sets (pp. 1-3).
* Beckmann, M., Ebecken, N. F., & de Lima, B. S. P. (2015). [A KNN Undersampling Approach for Data Balancing](http://www.scirp.org/journal/PaperDownload.aspx?paperID=60996). Journal of Intelligent Learning Systems and Applications, 7(04), 104.


