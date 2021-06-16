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

#peforming feature mapping
data['Outlet_Size'] = data['Outlet_Size'].replace(('High','Medium','Small'),(3,2,1))
y = data['Outlet_Size'].value_counts()
print(y,'\n')