
#Measures to evaluate and decide in ML
2016-06-01

Here is presented a collection of main measures useful to apply in Data Science and Machine Learning algorithms. That is a collection of association rules and performance measures and tools.

### Classsification
The main classification metrics are:
* ROC (Receiver Operating Characteristic): Measure for a binary classifier, where the true positive rate (TPR) is compared against the false positive rate (FPR).
* AUC (Area Under the Curve (ROC)): The area under the ROC curve.
* Accuracy score: proportion of good classified instances.
* Recall score: the ability of the classifier to find all the positive samples. `tp/(tp +fp)`
* Precision score: proportion of true positive between all the positive cases. `tp/(tp + fn)`
* F1 score: weighted average of the precision and recall. `F1 = 2 * (precision * recall) / (precision + recall)`
* Precision-Recall curve: the curve of precision against recall.
* Jaccard similarity score: size of intersection for the size of the union of two labels.
* Hinge loss: `max(0, 1-t*y)`
* Hamming loss: fraction of labels that are incorrectly predicted.
* Log-loss: logistic regression loss or cross-entropy loss is the negative log-likelihood of the true labels given a probabilistic classifier’s predictions.
* Confusion matrix: not aggregated information of how each class is related by the algorithms. Could be convenient to know what classes the algorithm thing they are too similar in order to improve the results through better selection of features or of a priori parameters of the algorithm.


### Ranking scores
Measures for ranking problems. There are measures that they are also used in classification problems.
* Lift (or Lorenz or power curve): plots the intervals (usually quantiles) performance compared to the average. 
* Label ranking error: average number of label pairs that are incorrectly ordered given y_score weighted by the size of the label set and the number of labels not in the label set.
* LRAP (Label Ranking Average Precision): average over each ground truth label assigned to each sample, of the ratio of true vs. total labels with lower score.
* Coverage error: how far we need to go through the ranked scores to cover all true labels. The best value is equal to the average number of labels in the ground truth per sample.


### Regression
The main measures for regression:
* R2 score: Fraction of unexplained variance.
* MSE (mean squared error): squared error per label and instance.
* Mean absolute error: Absolute error per label and instance.
* Median absolute error: Median absolute error for all labels and instances.
* Explained variance score: the total square difference between data and model.


### Clustering
The main measures for clustering problems:
* Mutual Information: how much information share the predicted labels with the ground truth. MI is symmetric and invariant under label permutation or label magnitudes.
* Normalized Mutual Information: scales the MI between 0 and 1 values.
* Adjusted Mutual Information: adjust of MI taking into account that two bigger clusters have more change to have greater mutual information only by change.
* Adjusted Rand Index: Rand index adjusted for chance. Rand index is the possible pairs that are assigned in the same in ground truth and predicted or in different in both, divided by the total possible pairs.
* Homogeneity score: measures the average of the homogeneity of each cluster in the prediction labels.
* Completeness score: complementary measure of homogeneity.

***Tags***: Data Science, Machine Learning, List


