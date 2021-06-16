#for operations
import numpy as np
import pandas as pd

#for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Big_mart.csv')
print(data.shape)					#prints (8523, 12), (rows, columns)
print(data.head,'\n')

missing_data = data.isnull().sum()
print(missing_data,'\n')

#imputing the missing values
data['Item_Weight'] = data['Item_Weight'].fillna(data['Item_Weight'].mean())		#imputing data with mean
data['Outlet_Size'] = data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0])		#imputing data with mode
data = data[data['Item_Visibility']<=0.2]

missing_Update_data = data.isnull().sum()
print(missing_Update_data,'\n')

#checking for outliers in the data
plt.rcParams["figure.figsize"]=(12,3)
plt.style.use('fivethirtyeight')

plt.subplot(1,3,1)
sns.boxplot(data['Item_Weight'])

plt.subplot(1,3,2)
sns.boxplot(data['Item_Visibility'])

plt.subplot(1,3,3)
sns.boxplot(data['Item_MRP'])
plt.show()

#cleaning the item identifiers
data['Item_Identifier'] = data['Item_Identifier'].apply(lambda x: x[0:2])
#check the values
x = data['Item_Identifier'].value_counts()
print(x,'\n')

#check Item_Fat content
y = data['Item_Fat_Content'].value_counts()
print(y,'\n')

#Cleaning values
data['Item_Fat_Content'] = data['Item_Fat_Content'].replace(('low fat','Lf','reg'),('Low Fat','Low Fat', 'Low Fat'))
y = data['Item_Fat_Content'].value_counts()
print(y,'\n')
