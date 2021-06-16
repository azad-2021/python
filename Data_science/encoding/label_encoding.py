import pandas as pd
from sklearn.preprocessing import LabelEncoder		#label Encoding
le=LabelEncoder()

#reading dataset
data = pd.read_csv('bigmart.csv')
print(data.head(),'\n')

data = data.drop('Item_Identifier',axis=1)
missing_data = data.select_dtypes('object').isnull().sum()
print(missing_data,'\n')

#check the frequency of all categories in the variable
y = data['Outlet_Size'].value_counts()
print(y,'\n')

#medium size have highest frequency, so we will fill the data with medium. Missing value treatement.
data['Outlet_Size'].fillna('Medium',inplace=True)
missing_data = data.select_dtypes('object').isnull().sum()
print(missing_data,'\n')

#In Label encoding, each category is assigned a value from 1 through N where N is the number of the categories for the category feature.
data['Item_Fat_Content_enc'] = le.fit_transform(data['Item_Fat_Content'])
data['Item_Type_enc'] = le.fit_transform(data['Item_Type'])
data['Outlet_Size_enc'] = le.fit_transform(data['Outlet_Size'])
data['Outlet_Type_enc'] = le.fit_transform(data['Outlet_Type'])
print(data.head(),'\n')