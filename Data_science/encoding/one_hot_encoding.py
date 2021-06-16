import pandas as pd

#reading dataset
data = pd.read_csv('employee.csv')
print(data.head(),'\n')

#one hot encoding in depatment column
x = pd.get_dummies(data['Department'])
print(x,'\n')

#Concactenating original dataset and x togather
data = pd.concat([data,x],axis=1)
print(data.columns,'\n')

#droping the department column
data = data.drop('Department',axis=1)
print(data.columns,'\n')