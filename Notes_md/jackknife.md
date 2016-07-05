
#Jackknife
2016-06-01

The jackknife is a resampling technique especially useful for variance and bias estimation. It uses random sample of observations to compute it. The jackknife predates other common resampling methods such as the bootstrap. The jackknife estimator of a parameter is found by systematically leaving out each observation from a sample and calculating the estimate and then finding the average of these calculations. Given a sample of size ${\displaystyle N}$, the jackknife estimate is found by aggregating the estimates of each ${\displaystyle N-1} estimate in the sample.
Instead of using the jackknife to estimate the variance, it may instead be applied to the log of the variance. This transformation may result in better estimates particularly when the distribution of the variance itself may be non normal.

For many statistical parameters the jackknife estimate of variance tends asymptotically to the true value *almost surely*. In technical terms one says that the jackknife estimate is consistent. The jackknife is consistent for the sample means, sample variances, central and non-central t-statistics (with possibly non-normal populations), sample coefficient of variation, maximum likelihood estimators, least squares estimators, correlation coefficients and regression coefficients.

It is not consistent for the sample median. In the case of a unimodal variate the ratio of the jackknife variance to the sample variance tends to be distributed as one half the square of a chi square distribution with two degrees of freedom.

The jackknife, like the original bootstrap, is dependent on the independence of the data. Extensions of the jackknife to allow for dependence in the data have been proposed.

Another extension is the delete-a-group method used in association with Poisson sampling.

The jackknife technique was developed by Maurice Quenouille (1949, 1956). John Tukey (1958) expanded on the technique and proposed the name "jackknife" since, like a physical jack-knife (a compact folding knife), it is a rough-and-ready tool that can improvise a solution for a variety of problems even though specific problems may be more efficiently solved with a purpose-designed tool.

The jackknife is a linear approximation of the bootstrap.

***Tags***: Statistics

#### See also
[Statistical testing](/statistical_testing), [Resampling methods](/resampling_methods), [Bootstrapping](/bootstrapping)
## Papers
* Jones, H.L. (1974). [Jackknife estimation of functions of stratum means](http://biomet.oxfordjournals.org/content/61/2/343.short). Biometrika 61 (2): 343-348.
* Efron, B. (1992). [Bootstrap methods: another look at the jackknife](http://projecteuclid.org/download/pdf_1/euclid.aos/1176344552). In Breakthroughs in Statistics (pp. 569-593). Springer New York.
* Efron, B., & Stein, C. (1981). [The jackknife estimate of variance](http://projecteuclid.org/download/pdf_1/euclid.aos/1176345462). The Annals of Statistics, 586-596.

## Books
* Efron, B., & Efron, B. (1982). [The jackknife, the bootstrap and other resampling plans](https://www.goodreads.com/book/show/2668500-the-jackknife-and-bootstrap) (Vol. 38). Philadelphia: Society for industrial and applied mathematics.


