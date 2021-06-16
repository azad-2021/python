import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns				#for ploting boxplot

data = pd.read_csv('train.csv')
print(data.head(),'\n')

'''
A boxplot is a standardized way of displaying the distribution of data based on five number summary
("minimum", first quartile(Q1), median, Third quatile(Q3) and maximum). It can tell you about your outliers and what there values are.

minimum outlier = Q1 - 1.5*IQR
maximum outlier = Q3 + 1.5*IQR

'''

#ploting univariate outliers
plt.rcParams["figure.figsize"]=(16,4)

plt.subplot(1,4,1)
sns.boxplot(data['Item_Weight'])

plt.subplot(1,4,2)
sns.boxplot(data['Item_Visibility'])

plt.subplot(1,4,3)
sns.boxplot(data['Item_MRP'])

plt.subplot(1,4,4)
sns.boxplot(data['Item_Outlet_Sales'])

plt.suptitle('checking the univariate ourliers')
plt.show()

#ploting Bivariate Outliers. It is always found in the target set.
plt.subplot(1,3,1)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_Weight'])

plt.subplot(1,3,2)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_Visibility'])

plt.subplot(1,3,3)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_MRP'])

plt.suptitle('checking the Bivariate ourliers')
plt.show()


'''
Winsorization :
Winsorization is a way to minimize the influence of outliers in our data by either by Deleting the extreme observation of our data.
The concept of winsorization is based on the concept of normal distribution.
Where it tries to find out the most uncommon observations and treat them in most appropiate way.

#steps for winsorization
1.TO analyze the data and try to find out the cause for the outliers in the dataset
2.To decide how much winsorization we want. In general, we prefer the winsorization of top 5% and the bottom 5% of the dataset.
But it can be varied from 2 to 10%.
3.To replace the extreme values by maximum or minimum values.

'''

#Handling outliers
'''
Two ways of handling outliers
1.Deleting
2.capping

We have to handle outliers carefully
Example:
The age variable in our dataset which predict loan approval.
The normal range of age can be 15-60 years but there may be some people with age greater than 60
Here in this case, where people having age greater than 60 applied for the loan are not outliers, we can't simply delete them.

We can delete outliers only in the following cases

1.We are sure that the outliers are due to an entry error or due to measurement error
2.If outliers create a significant relationship between two indipendent variables which is against the assumption
of many of our machine learning algorithms.

#capping outliers
Capping refers to replacing the outliers to a near value so that we can keep the point in our analysis and it also doesn't skew data.

Note: Other than deleting and capping, there are two more ways of handling outliers.
	1.Imputing: If an outlier seems to be due to some mistake and we recognise the mistake, we replace it with the mean.
	2.Binning: It is the process of transforming numerical variables into categorical type.
			 Example: We bcan bin the age variuable into categories such as 20-40,40-60,60-80 and above...
'''

#capping the outliers in the column Item_outlet_sales having values greater than 10000
data['Item_Outlet_Sales'].values[data['Item_Outlet_Sales'].values>10000]=10000

#checking if there is still any value greater that 10000 left in the Item_Outlet_sales column
z = data[data['Item_Outlet_Sales']>10000]
print(z,'\n')

plt.subplot(1,3,1)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_Weight'])

plt.subplot(1,3,2)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_Visibility'])

plt.subplot(1,3,3)
sns.scatterplot(y=data['Item_Outlet_Sales'],x=data['Item_MRP'])

plt.suptitle('checking the Bivariate ourliers')
plt.show()


#ploting univariate outliers
plt.rcParams["figure.figsize"]=(16,4)

plt.subplot(1,4,1)
sns.boxplot(data['Item_Weight'])

plt.subplot(1,4,2)
sns.boxplot(data['Item_Visibility'])

plt.subplot(1,4,3)
sns.boxplot(data['Item_MRP'])

plt.subplot(1,4,4)
sns.boxplot(data['Item_Outlet_Sales'])

plt.suptitle('checking the univariate ourliers')
plt.show()