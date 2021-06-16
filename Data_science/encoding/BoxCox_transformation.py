'''
A box Cox transformation is a way to transform non-normal dependent variable into a normal shape.
'''

import pandas as pd
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.special import boxcox, boxcox1p
from scipy.stats import skew				#for skewness

data = pd.read_csv('Bigmart.csv')
print(data.head(),'\n')

numerical_feats = data.dtypes[data.dtypes != 'object'].index

#checking the skewness in all numerical features
skewed_feats = data[numerical_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending = False)

#converting the feature into dataframe
skewness = pd.DataFrame({'skew': skewed_feats})

print(skewness.head(10),'\n')

'''
If the skewness is less than -1 and greater than 1, the distribution is highly skewed. If the skewness is between -1 and -0.5
or between 0.5 and 1, the distribution is moderately skewed and if the distribution is between -0.5 and 0.5, the 
distribution is approximately symmetric.
'''
#Applying Box Cox Transformation

skewness = skewness[abs(skewness > 0.5)]

#printing how many features are to be box-cox transformed
print("There are {} skewed numerical features to box cox transform\n".format(skewness.shape[0]))
#definig skewed features
skewed_features = skewness.index

lam = 0.15
for feat in skewed_features:
	data[feat] += 1
	data[feat] = boxcox1p(data[feat],lam)

data[skewed_features] = np.log1p(data[skewed_features])

#Again checking skewness
numerical_feats = data.dtypes[data.dtypes != 'object'].index

#checking the skewness in all numerical features
skewed_feats = data[numerical_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending = False)

#converting the feature into dataframe
skewness = pd.DataFrame({'skew': skewed_feats})

print(skewness.head(10),'\n')