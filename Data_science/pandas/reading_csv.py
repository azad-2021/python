import pandas as pd

#reading csv file
data = pd.read_csv('data.csv')

x = data.head()						#prints first five data set.
print(x,'\n')

a = data.head(10)					#prints first 10 data set.
print(a,'\n')


#reading excel file

df = pd.read_excel('data.xlsx')
z = df.head()					#returns first five rows
print(z,'\n')

b = df.head(10)					#returns first ten rows
print(b,'\n')