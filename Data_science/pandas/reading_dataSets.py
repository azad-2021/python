import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

#vakue_counts() is used to return the values for different classes present in the column of a dataset
'''
plot a pie chart when we have 4-5 distinct values in the column, a bar chart when we have more than 5 distinct values
in the column and a line chart if we have many didtinct values.

'''
#show pie chart
b['Country'].value_counts().plot(kind = 'pie')
#plt.show()

#show line chart
b['Country'].value_counts().plot(kind = 'line')
#plt.show()

#indexing data
#creating a time series using the date range method from pandas
time_series = pd.date_range('1/1/2020',periods = 20)		#gives next 20 days starting from 1/1/2020
#print(time_series)
df = pd.DataFrame(np.random.randn(20,5),	#creates random numbers. 20 refers to number of rows, 5 refers to number off columns
				  
				index=time_series,
				columns=['column1', 'column2', 'column3', 'column4', 'column5'])
#print(index)
#print(columns)
print(df,'\n')
print(df['column1'],'\n')

print(df[['column1', 'column3', 'column4']],'\n')

#time_series specific indexing
col1 = df['column1']
x = col1[time_series[3]]
print(x,'\n')

#dataframe.loc attribute access a group of rows or columns by labels in the given dataframe
x = pd.DataFrame({'x': [1,2,3], 'y':[3,4,5]})		#creating dataframe using dictonary structure
print(x,'\n')
#selecting by position
#specifying new values to the row no. 1
x.loc[1] = {'x':9, 'y':99}
print(x,'\n')

#slicing is the feature that enables accessing sequences
#iloc attribute access a group of rows or columns by index location
z = df.iloc[:5, 0:2]
print(z,'\n')

a = df[::3]				#prints evry 3rd row of all columns
print(a,'\n')

#filtering filters the given sequence and return it
s = df[(df['column3']<0)]			#prints those values where column 3 is less than 0 after column 3, it wiil prints all results

print(s,'\n')

#Merging is the process of bringing two datasets togather and aligning the rows from each based on common attributes or columns
'''
Types of join
1. inner join - It combines two dataframes based on a common key and returns a new datframe that contins only rows
that have matching values in both of the original dataframes

2. Outer joint returns all those records which either have match in the left or right dataframe
when rows in both dataframes do not match, the resulting dataframe will have NaN for every column of the dataframe that lacks a matching row.

3. Left joint returns a dataframe containing all rows of left dataframe.
All the non-matching rows of left dataframe contain NaN for the columns in right datframe.

4. Right joint returns a dataframe containing all rows of Right dataframe.
All the non-matching rows of left dataframe contain NaN for the columns in left datframe.
'''
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data.csv')
print(data1,'\n')

#merging two datasets
start_date =  pd.merge(data,data1, on = 'Name', how = 'inner')
start_date.head()
print(start_date)