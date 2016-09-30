
##HW3, Assignment 1:
Visually demonstrate the Central Limit Theorem with 5 different distributions (Chi-squared, Gaussian, Poisson, Binomial, and Logistic).

For each distribution, use 100 samples, with sample sizes ranging from 20 to 2000.

For each distribution, plot sample mean against sample size for the 100 samples, showing that as sample size increases, the sample mean of the distribution is more likely to equal to that of the parent of distribution, which is the universal mean of 100 that is specified.
For each distribution, also plot the distribution of the sample means, showing that the sample means do follow a Gaussian distribution themselves, in other words, the majority of the sample means, with enough samples drawn, will be the same, equaling to the mean of the parent distribution.

The 5 distributions are generated with the module of numpy.random. To ensure that the results generated each time remain the same, a seed of 0 is also given.

(The extra credit of fitting a Gaussian to the distribution of the sample means is not done here yet...)

##Assignment 3:
Complete a Z-test for new and old bus commute time comparison.
Tasks performed:
1. Formulate measurable null and alternate hypotheses with a given question, both in words and in equations.
2. Select a statistic test, with a significance level specified in advance.
3. Gather variables needed to perform the chosen statistic test, in this case the mean of the new travel times measured (read data from a text file into an array using the np.loadtxt module, then use the np.mean module to calculate the mean).
4. Calculate the z-score with the relevant formula. Then compare the result to chosen threshold.
5. If result is lower than the threshold, then Null hypothesis is rejected, and the alternate hypothesis stands true.
