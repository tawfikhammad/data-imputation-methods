## Overview

`SimpleImputer` is a Python class that provides a simple implementation of data imputation for handling missing values in tabular data. The class is inspired by scikit-learn's `SimpleImputer`, offering a straightforward and easy-to-understand solution for imputing missing values in both numeric and categorical columns.

## Features

- Supports mean and median imputation strategies for numerical columns.
- Handles most frequent category imputation for categorical columns.
- Works with both numerical and categorical data.
- Easy-to-use API with `fit` and `transform` methods similar to scikit-learn's estimators.

## Installation

The `SimpleImputer` class is a stand-alone Python file. To use it, simply download the `simple_imputer.py` file and place it in your project directory or any location accessible in your Python environment.

## Usage

Here's a basic example of how to use the `SimpleImputer` class:

```python

import numpy as np
import pandas as pd
from simple_imputer import SimpleImputer

# Sample data with missing values
data = {'Age': [25, 30, 35, np.nan, 45],
        'Income': [50000, 55000, np.nan, 65000, 70000],
        'Education': [16, np.nan, 18, 20, 16],
        'Color': ['red', np.nan, 'blue', 'green', 'red']}

df = pd.DataFrame(data)

# Instantiate the SimpleImputer with the desired strategy (mean, median, or most_frequent)
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the data
imputer.fit(df)

# Transform the data to impute missing values
imputed_data = imputer.transform(df)

print(imputed_data)
```

## Supported Strategies

- **Mean:** Impute missing numerical values with the mean of the column.
- **Median:** Impute missing numerical values with the median of the column.
- **Most Frequent:** Impute missing categorical values with the most frequent category.

## Limitations

- The current implementation handles only numerical and categorical columns.
- Advanced features present in scikit-learn's `SimpleImputer` like constant imputation, custom fill values, and handling non-numeric missing values are not supported.

## Contributing

Contributions to the `SimpleImputer` project are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

The `SimpleImputer` class is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code according to the terms of the license.

## Contact

For any questions or inquiries, you can reach out to [contact@example.com](mailto:contact@example.com).

---
Note: The `SimpleImputer` class provided in this README is a simplified version for illustrative purposes. For a more comprehensive and production-ready implementation, it is recommended to use [scikit-learn's `SimpleImputer`.](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
