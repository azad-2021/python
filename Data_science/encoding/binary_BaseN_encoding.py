import pandas as pd
from category_encoders import BinaryEncoder
be = BinaryEncoder()
import category_encoders as ce
#Binary Encoding
#reading dataset
data = pd.read_csv('bigmart.csv')
print(data.head(),'\n')

#value count of different categories of Item types 
x = data['Item_Type'].value_counts()
print(x,'\n')

y = be.fit_transform(data['Item_Type'])
print(y,'\n')

#concatenating the original data and encoded data togather
data = pd.concat([data,y],axis=1)
print(data.columns,'\n')


#BaseN Encoding for column 'Name' using base 4. BaseN Encoding reduces dimensionality of Encoding
df = pd.read_csv('fifa.csv')
print(df.head,'\n')
a = ce.BaseNEncoder(cols=['Name'],base=4)
a = a.fit_transform(df[['Name']])

print(a,'\n')