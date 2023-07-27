# Understanding k-NN Imputation 
**k-Nearest Neighbors (k-NN) imputation** is a method used to estimate and replace missing values in datasets.
As its name suggests, **k-NN imputation** involves the use of 'k' closest neighbors to predict and fill in missing data.

# k-NN Imputation in Action⚙️
**The k-NN imputation** operates under the assumption that similar data points should have similar values.
The **k-NN algorithm** identifies the 'k' closest neighbors to the sample using a distance function, and estimates the missing value based on these neighboring values.

# Comparison with Other Imputation Methods 📊
**k-NN imputation** isn't the only imputation technique available. Let's compare it with two other popular methods: 
**`Multiple Imputation`**
Multiple imputation, typically implemented as Multiple Imputation by Chained Equations (MICE), replaces each missing value with a set of plausible values to generate multiple complete datasets.
These datasets are then analyzed, and the results are pooled to account for imputation uncertainty.

**`Predictive Mean Matching (PMM)`**
[Predictive Mean Matching (PMM)](../Predictive-Mean-Matching-(PMM)) fits a predictive model (like a regression) using other variables and then imputes the missing value by picking an observed value from a donor who has a similar predicted value.


# Reference 📚
1- Buisson, F. (2021). Behavioral Data Analysis with R and Python. O'Reilly Media, Inc.

2- Bruce, P., Bruce, A., & Gedeck, P. (2020). Practical Statistics for Data Scientists. O'Reilly Media.

3- van Buuren, S. (2012). Flexible Imputation of Missing Data (Chapman & Hall/CRC Interdisciplinary Statistics) (1st ed.)
