
#Statistical testing
2016-06-01

A statistical hypothesis is a hypothesis that is testable framework process to study and compare data assumption of observing a process that are modeled via a set of random variables. A statistical hypothesis test is a method of statistical inference (frequentist and bayesian).

Commonly, two statistical data sets are compared, or a data set obtained by sampling is compared against a synthetic data set from an idealized model. A hypothesis is proposed for the statistical relationship between the two data sets, and this is compared as an alternative to an idealized null hypothesis that proposes no relationship between two data sets. The comparison is deemed statistically significant if the relationship between the data sets would be an unlikely realization of the null hypothesis according to a threshold probability -the significance level. Hypothesis tests are used in determining what outcomes of a study would lead to a rejection of the null hypothesis for a pre-specified level of significance. The process of distinguishing between the null hypothesis and the alternative hypothesis is aided by identifying two conceptual types of errors (type 1 & type 2), and by specifying parametric limits.

### Procedure
So, put it simply:
* Proposing an alternative hypothesis over the relationship between 2 data sets.
* Proposing null hypothesis by selecting and applying a random model over the data.
* Select the test statistic T and the appropiate test to use.
* Using comparison tests to get a measure of confidence.
* Accept or reject the alternative hypothesis.

An alternative framework for statistical hypothesis testing is to specify a set of statistical models, one for each candidate hypothesis, and then use model selection techniques to choose the most appropriate model. The most common selection techniques are based on either Akaike information criterion or Bayes factor.

### Main concepts
The summary of main concepts of hypothesis testing:
* Statistical hypothesis: assumption over parameters describing the population (not the sample which are the observed parameters).
* Statistic: value computed from a sample, often to summarize the sample for comparison purposes.
* Simple hypothesis: any hypothesis which specifies the population distribution completely.
* Null hypothesis (H0): a simple hypothesis based on a random model applied over the sample. It will use to contradict the theory proposed.
* Alternative hypothesis (H1): a hypothesis (often composite) associated with a theory one would like to prove.
* Statistical test: a procedure whose inputs are samples and whose result is a hypothesis.
* Critical value: the threshold value delimiting the regions of acceptance and rejection for the test statistic.
* Power of a test (1 − $\beta$): the test's probability of correctly rejecting the null hypothesis. The complement of the false negative rate, $\beta$. Power is termed sensitivity in biostatistics. ("This is a sensitive test. Because the result is negative, we can confidently say that the patient does not have the condition.") 
* Significance level of a test ($\alpha$): it is the upper bound imposed on the size of a test. Its value is chosen by the statistician prior to looking at the data or choosing any particular test to be used. It is the maximum exposure to erroneously rejecting H0 he/she is ready to accept. Testing H0 at significance level α means testing H0 with a test whose size does not exceed α. In most cases, one uses tests whose size is equal to the significance level.
p-value: the probability, assuming the null hypothesis is true, of observing a result at least as extreme as the test statistic.


### Main statistical tests
Some categories:
* One-sample tests are appropriate when a sample is being compared to the population from a hypothesis. The population characteristics are known from theory or are calculated from the population.
* Two-sample tests are appropriate for comparing two samples, typically experimental and control samples from a scientifically controlled experiment.
* Paired tests are appropriate for comparing two samples where it is impossible to control important variables. Rather than comparing two sets, members are paired between samples so the difference between the members becomes the sample. Typically the mean of the differences is then compared to zero. The common example scenario for when a paired difference test is appropriate is when a single set of test subjects has something applied to them and the test is intended to check for an effect.

Possible statistical tests to use:
* Z-tests (assumption of gaussian): comparing means with known variance.
* Welch's t test (assumption of Gaussian distribution).
* Fisher's exact test (assumption of Binomial distribution).
* E-test (assumption Poisson distribution).
* Chi-squared test (assumption of Multinomial distribution).
* Mann-Whitney U test (no assumption of distribution).
* Student's t-tests are appropriate for comparing means under relaxed conditions when less is assumed.

***Tags***: Statistics

## See also
## See also:
[Resampling methods](/resampling_methods)
## Papers
* Loftus, G R (1991). [On the Tyranny of Hypothesis Testing in the Social Sciences](https://www.ics.uci.edu/~sternh/courses/210/loftus91_tyranny.pdf). Contemporary Psychology 36 (2): 102-105.

## Books
* Huff, Darrell (1993). [How to lie with statistics](https://www.goodreads.com/book/show/51291.How_to_Lie_with_Statistics). New York: Norton.


