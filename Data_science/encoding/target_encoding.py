import pandas as pd
import numpy as np

#reading dataset
data = pd.read_csv('bigmart.csv')
print(data.head(),'\n')

#Finding the avg sales based on the Item Type
x = data['Item_Outlet_Sales'].groupby(data['Item_Type']).agg('mean')
print(x,'\n')

#sort the unique categories of the item type column
y = np.sort(data['Item_Type'].unique())

#replacing the categories by mean of the target variable
data['Item_Type'] = data['Item_Type'].replace((y),(x.values))
print(data,'\n')