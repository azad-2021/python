'''
There are 4 data manupulation functions:
1.reindex
2.set_index
3.reset_index
4.sort_index

'''

#Reindex function is used to reorder the index in the dataframe
import numpy as np
import pandas as pd

#creating a Dataframe
index = ['Firefox', 'Chrome','Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({'http_status':[200,200,404,404,301],
					'response_time': [0.04,0.02,0.07,0.08,1.0]},
					index=index)

print(df,'\n')

#creating a new order of index
new_index = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']

#apply new order of index
df = df.reindex(new_index)

print(df,'\n')

#Reset index is used to reset the index or convert an index into a column

df = pd.DataFrame([('bird',389.0),
					('bird',24.0),
					('mammal',80.5),
					('mammal',np.nan)],
					index=['Falcon','Parrot','Lion','Monkey'],
					columns=('class','max_speed'))

print(df,'\n')

#convert the index into column
df = df.reset_index()
print(df,'\n')

#Remove the index completely
df = df.reset_index(drop=True)
print(df,'\n')


#sort index
df = pd.DataFrame({'month':[1,4,7,10],
					'year':[2012,2014,2013,2014],
					'sale':[55,40,84,31]})

print(df,'\n')

sort_sale = df['sale'].sort_values()			#sorted by values
print(sort_sale,'\n')

sort_sale = df['sale'].sort_index()				#sorted by index
print(sort_sale,'\n')

#set month column into index
df = df.set_index('month')
print(df,'\n')

#Replace function is used to replace old values with the new one
df['year'] = df['year'].replace((2013),(2021))		#year 2013 replaced by year 2021
print(df,'\n')

#Droplevel function is used to remove levels in multilevel indexing
df = pd.DataFrame([
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
	]).set_index([0,1]).rename_axis(['a','b'])
print(df,'\n')

df = df.droplevel('a')		#droping the column a
print(df,'\n')

#split function splits a string into a list
s = 'x y z'
print(s.split(' '))
print(s.split(' ')[0])		#to fetch x which is at index 0

#stack function
df = pd.DataFrame([[0,1],[2,3]],
					index=['cat','dog'],
					columns=['weight','height'])
print(df,'\n')

df = df.stack()
print(df,'\n')

#unstack function
df = df.unstack()
print(df,'\n')

#melt function
'''
This function is used to massage a dataframe into a format where one or more columns are identifier variables
(Id_vars), while all other columns, consider measured variables (value_vars), are 'unpivoted' to the row axis,
leaving just two non-identifier columns, 'variable' and 'value'.
'''

df = pd.DataFrame({'A':{0: 'a', 1:'b', 2: 'c'},
				   'B':{0: 1, 1: 3, 2: 5},
				   'c':{0: 2, 1: 4, 2: 6}}) 
print(df,'\n')

#melt the data
df = df.melt(id_vars=['A'], value_vars=['B'])
print(df,'\n')

#The explode function transform each element of a list-like to a row representing index values.
#create dataframe
df = pd.DataFrame({'A': [[1,2,3],'foo',[],[3,4]], 'B': 1})
print(df,'\n')

df = df.explode('A')
print(df,'\n')

#squeeze function
'''
Series or dataframe with a single element are squeezed to a scalar. Dataframe with a single column or a single row
are squeezed to a series. Otherwise the object is unchanged.
This method is most useful when you don't know if your object is a Series or Dataframe, but you do know it has just
a single column. In that case you can safely call squeeze to ensure you have a series.
'''

df = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
print(df,'\n')
#slicing a single column will produce a dataframe with the column having only one value:
df_a = df[['a']]
print(df_a,'\n')

squeeze_a = df_a.squeeze()
print(squeeze_a,'\n')