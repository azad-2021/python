import pandas as pd

data = pd.read_csv('data.csv')			#reading dataset
#print first five rows of dataset
print(data.head,'\n')
print(data.columns,'\n')

#sorting the missing value in rows in decending order
missing_sort = data.isnull().sum(axis=1).sort_values(ascending=False)
print(missing_sort,'\n')

#checking if there is any missing values in rows
missing = data.isnull().any(axis=1)
print(missing,'\n')

#checking if there is any row having all missing values
missing_all = data.isnull().all(axis=1).sum()
print(missing_all,'\n')		#prints 0 bcz there is no row having all values missing

#check missing values is greator than 50
missing_50 = data[data.isnull().sum(axis=1)>50]
print(missing_50,'\n')

print('Before deleting rows ',data.shape[0],'\n')

data = data[data.isnull().sum(axis=1)<=50]
print("after removing more than 50 missing values ",data.shape[0],'\n')


#checking for missing values in columns
missing_columns = data.isnull().sum()

print(missing_columns,'\n')

display_all = pd.set_option('max_rows',89)
missing_columns = data.isnull().sum()
print(missing_columns,'\n')

#check the % of missing values in each column of dataset
x = data.isnull().sum()
y = (data.isnull().sum()/data.shape[0])*100
z = {'Number of missing values':x, 'percentage of missing values':y}
df = pd.DataFrame(z,columns=['Number of missing values','percentage of missing values'])
df.sort_values(by = 'percentage of missing values', ascending=False)
print(x,'\n')
print(y,'\n')
print(df,'\n')

data = data.drop(['Loaned From'], axis = 1)
print("columns after removing Loaned From",data.columns,'\n')