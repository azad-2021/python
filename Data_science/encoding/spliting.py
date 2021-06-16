import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv('Iris.csv')
print(data.head(),'\n')

#droping the ID column
data = data.drop('Id',axis=1)

#spliting the dependent and Independent variables
x = data.iloc[:,:-1]
y = data['Species']

print('Shape of x is -', x.shape)
print('Shape of Y is -', y.shape)


print(x,'\n')

#soliting the train and test dataset
x_tarin, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
print('Shape of x_tarin is ',x_tarin.shape)
print('Shape of x_test is',x_test.shape)
print('Shape of y_tarin is ',y_train.shape)
print('Shape of y_test is',y_test.shape)