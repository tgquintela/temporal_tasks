
#Bagging
2016-06-01

Bagging (bootstrap aggregating), also called bagging, is a machine learning ensemble meta-algorithm designed to improve the stability and accuracy of machine learning algorithms used in statistical classification and regression. It also reduces variance and helps to avoid overfitting. Although it is usually applied to decision tree methods, it can be used with any type of method. Bagging is a special case of the **model averaging approach**.

Given a standard training set $D$ of size $n'$, bagging process:
1. generation $m$ new training sets ${\displaystyle D_{i}}$, each of size $n$, by sampling from $D$ uniformly and with replacement. By sampling with replacement, some observations may be repeated in each ${\displaystyle D_{i}}$. If $n'=n$, then for large $n$ the set ${\displaystyle D_{i}}$ is expected to have the fraction (1 - 1/e) (≈63.2%) of the unique examples of D, the rest being duplicates. This kind of sample is known as a bootstrap sample. 
2. The $m$ models are fitted using the above m bootstrap samples and combined by averaging the output (for regression) or voting (for classification).

Bagging is specially good for "unstable procedures" (Breiman, 1996), artificial neural networks, classification and regression trees, and subset selection in linear regression (Breiman, 1994).

Bagging leads to "improvements for unstable procedures" (Breiman, 1996), which include, for example, artificial neural networks, classification and regression trees, and subset selection in linear regression (Breiman, 1994). An interesting application of bagging showing improvement in preimage learning is provided here. On the other hand, it can mildly degrade the performance of stable methods such as K-nearest neighbors (Breiman, 1996).

One of the uses of bagging is random subspace method (or attribute bagging) which is an ensemble classifier that consists of several classifiers each operating in a subspace of the original feature space, and outputs the class based on the outputs of these individual classifiers. Random subspace method has been used for decision trees (random decision forests), linear classifiers, support vector machines, nearest neighbours and other types of classifiers. This method is also applicable to one-class classifiers. The algorithm is an attractive choice for simultaniously:
	* classification problems
	* where the number of features is much larger than the number of training objects, such as fMRI data or gene expression data.

***Tags***: Artificial Intelligence, Machine Learning, Statistics

### See also
[Machine Learning](/machine_learning), [Artificial Neural Networks](/artificial_neural_networks), [Random Forest](/random_forest)
## Papers
* Breiman, L. (1996). [Bagging predictors](http://www.machine-learning.martinsewell.com/ensembles/bagging/Breiman1996.pdf). Machine learning, 24(2), 123-140.
* Quinlan, J. R. (1996, August). [Bagging, boosting, and C4. 5](http://www.cs.ecu.edu/~dingq/CSCI6905/readings/BaggingBoosting.pdf). In AAAI/IAAI, Vol. 1 (pp. 725-730).


