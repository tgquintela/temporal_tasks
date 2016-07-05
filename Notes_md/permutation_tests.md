
#Permutation tests
2016-06-01

A permutation test (also called a randomization test, re-randomization test, or an exact test) is a type of statistical significance test in which the distribution of the test statistic under the null hypothesis is obtained by calculating all possible values of the test statistic under rearrangements of the labels on the observed data points. In other words, the method by which treatments are allocated to subjects in an experimental design is mirrored in the analysis of that design. If the labels are exchangeable under the null hypothesis, then the resulting tests yield exact significance levels; see also exchangeability. Confidence intervals can then be derived from the tests. The theory has evolved from the works of Ronald Fisher and E. J. G. Pitman in the 1930s.

The process goes as follows:
* Computing the observed value of the test statistic using the whole samples.
* The points are permuted and reasigned computing the value of the test statistic using the transformed samples. The set of these calculated test statistic is the exact distribution of possible differences under the null hypothesis that group label does not matter.

Permutation tests are a subset of non-parametric statistics.

The permutation tests assume you compute the null hypothesis by computing all the possible permutations. For big datasets that's become impossible. In that cases we use Montecarlo for computing an asymptotically equivalent permutation test.

***Tags***: Statistics

#### See also
[Resampling methods](/resampling_methods)
## Papers
* Anderson, M. J. (2001). [Permutation tests for univariate or multivariate analysis of variance and regression](http://ubio.bioinfo.cnio.es/Cursos/CEU_MDA07_practicals/Further%2520reading/Papers%2520on%2520ecological%2520statistics/Permutation%2520tests%2520in%2520ecological%2520statistics%2520Anderson2001.pdf). Canadian journal of fisheries and aquatic sciences, 58(3), 626-639.
* Anderson, M., & Braak, C. T. (2003). [Permutation tests for multi-factorial analysis of variance](http://avesbiodiv.mncn.csic.es/estadistica/permut1.pdf). Journal of statistical computation and simulation, 73(2), 85-113.

## Books
* Good, P. (2013). [Permutation tests: a practical guide to resampling methods for testing hypotheses](https://www.goodreads.com/book/show/7824330-permutation-tests). Springer Science & Business Media.


