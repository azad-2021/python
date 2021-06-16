import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("insurance.xlsx")
print(data.head(),'\n')
print(data.shape,'\n')		#prints 1338 records and each records have 7 columns
print(data.info(),'\n')

fig, ax = plt.subplots(figsize=(10,10))

corr = data.corr()						#To find all linear corelations of all columns in the dataframe
#These corelations can only be drawn on numerical feeds

sns.heatmap(corr, annot = True, ax=ax)
plt.show()

#The values of corelation is between 0 and 1. If the values have close to zero, then those two columns have very less corelations.
#If the values have close to 1, then those two columns have very high corelations.
#If the corelations between two diffrenet columns are very high then you can feel free to drop one of the columns in the dataset.
#Because it would not have any sence having two columns explaining the same thing.

#searching for string type dataset
d_type = dict(data.dtypes)
for name, type_ in d_type.items():
	if str(type_) == 'object':
		print(f"<-------- {name} ----------->")
		print(data[name].value_counts())
		print()

 	
 	
 	