
#Cross-validation
2016-06-01

Cross-validation is a statistical method for validating a predictive model. Subsets of the data are held out for use as validating sets; a model is fit to the remaining data (a training set) and used to predict for the validation set. Averaging the quality of the predictions across the validation sets yields an overall measure of prediction accuracy. Cross-Validation is employed repeatedly in building decision trees or in the validation process in Machine learning in order to avoid overfitting.

The main types of cross-validation are:
* Leave-one-out cross-validation (similar to jackknife)
* Leave-p-out cross-validation
* K-fold cross-validation (splits the data into K subsets, each is held out in turn as the validation set)

Cross-validation main goal is to avoid "self-influence".

This is often used for deciding how many predictor variables to use in regression. Without cross-validation, adding predictors always reduces the residual sum of squares (or possibly leaves it unchanged). In contrast, the cross-validated mean-square error will tend to decrease if valuable predictors are added, but increase if worthless predictors are added.

***Tags***: Statistics, Machine Learning

### See also
[Resampling methods](/resampling_methods)
## Papers
* Kohavi, R. (1995, August). [A study of cross-validation and bootstrap for accuracy estimation and model selection](https://pdfs.semanticscholar.org/0be0/d781305750b37acb35fa187febd8db67bfcc.pdf). In Ijcai (Vol. 14, No. 2, pp. 1137-1145).
* Golub, G. H., Heath, M., & Wahba, G. (1979). [Generalized cross-validation as a method for choosing a good ridge parameter](http://www.atomki.hu/~efo/hornyak/Tikhonov_references/Technometrics_Golub_Heath_Wahba.pdf). Technometrics, 21(2), 215-223.
* Krogh, A., & Vedelsby, J. (1995). [Neural network ensembles, cross validation, and active learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.9672&rep=rep1&type=pdf). Advances in neural information processing systems, 7, 231-238.
* Efron, B. (1983). [Estimating the error rate of a prediction rule: improvement on cross-validation](http://www.cs.berkeley.edu/~jordan/sail/readings/archive/efron-improve_cv.pdf). Journal of the American Statistical Association, 78(382), 316-331.


