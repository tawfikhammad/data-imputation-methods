## Overview

`PredictiveIterativeImputer` is a Python class that extends the capabilities of the basic `SimpleImputer` to provide a more sophisticated data imputation method using predictive iterative imputation. This class is inspired by scikit-learn's `IterativeImputer` but offers a simplified and understandable solution for imputing missing values in tabular data, including both numeric and categorical columns.

## Usage

Here's an example of how to use the `PredictiveIterativeImputer` class:

```python
import numpy as np
import pandas as pd
from predictive_iterative_imputer import PredictiveIterativeImputer
from sklearn.linear_model import LinearRegression

# Sample data with missing values
data = {'Age': [25, 30, 35, np.nan, 45],
        'Income': [50000, 55000, np.nan, 65000, 70000],
        'Education': [16, np.nan, 18, 20, 16],
        'Color': ['red', np.nan, 'blue', 'green', 'red']}

df = pd.DataFrame(data)

# Instantiate the PredictiveIterativeImputer with a predictive model (e.g., Linear Regression)
predictive_model = LinearRegression()
imputer = PredictiveIterativeImputer(predictive_model, imputation_order='random', max_iter=10)

# Fit the imputer on the data
imputer.fit(df)

# Transform the data to impute missing values iteratively
imputed_data = imputer.transform(df)

print(imputed_data)
```

## Supported Strategies

- The `PredictiveIterativeImputer` uses a custom predictive model (e.g., Linear Regression) for iterative imputation. It predicts missing values based on available non-missing values in other rows, iteratively refining the imputed values.

## Limitations

- The current implementation handles only numerical and categorical columns.
- Advanced features present in scikit-learn's `IterativeImputer`, such as multiple predictive models and optimization strategies, are not included in this simplified version.

## Contributing

Contributions to the `PredictiveIterativeImputer` project are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

The `PredictiveIterativeImputer` class is provided under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code according to the terms of the license.


---
Note: The `PredictiveIterativeImputer` class provided in this README is a simplified version for illustrative purposes. For a more comprehensive and production-ready implementation, consider using advanced libraries like [scikit-learn's `IterativeImputer`.](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html)
