# import necessary libraries
import numpy as np
import pandas as pd
 
# import the KNNimputer class
from sklearn.impute import KNNImputer
 
 
# create dataset for marks of a student
dict = {'Maths':[80, 90, np.nan, 95],
        'Chemistry': [60, 65, 56, np.nan],
        'Physics':[np.nan, 57, 80, 78],
       'Biology' : [78,83,67,np.nan]}
 

# creating a data frame from the list
Before_imputation = pd.DataFrame(dict)


#print number of missing data before imputation
print("number of missing data Before performing imputation\n",Before_imputation.isna().sum())
 

# create an object for KNNImputer
imputer = KNNImputer(n_neighbors=2)
After_imputation = imputer.fit_transform(Before_imputation)
df = pd.DataFrame(After_imputation, columns=['Maths', 'Chemistry', 'Physics','Biology'])

# print number of missing data after performing the operation
print("\n\nAfter performing imputation\n",df.isna().sum())

