import pandas as pd
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('Bigmart.csv')
print(data.head(),'\n')

#A Q-Q plot is a scatterplot created by plotting two sets of quantities against one another. If both sets of Quantities
#came from same distribution. We should see the points forming a line that's roughly straight

#MAke the Q-Q plot for the item outlet sales to check for the distribution and skewness

sns.distplot(data['Item_Outlet_Sales'], fit = norm)

#Get the fitted parameters used by function
(mu,sigma) = norm.fit(data['Item_Outlet_Sales'])
print('mean = {:.2f} and standard deviation = {:.2f}'.format(mu,sigma))

#Plot the distribution
plt.legend(['Normal dist. ($\mu=${:.2f} and $\sigma=$ {:.2f} )'.format(mu,sigma)],
			loc='best')
plt.ylabel('Frequency')
plt.title('Item Outlet Sales Distribution')

#Get also the QQ-plot
fig = plt.figure()
res = stats.probplot(data['Item_Outlet_Sales'], plot = plt)
plt.show()

#performing square root transformation

data['Item_Outlet_Sales'] = np.sqrt(data['Item_Outlet_Sales'])
sns.distplot(data['Item_Outlet_Sales'], fit = norm)

#Get the fitted parameters used by function
(mu,sigma) = norm.fit(data['Item_Outlet_Sales'])
print('mean = {:.2f} and standard deviation = {:.2f}'.format(mu,sigma))

#Plot the distribution
plt.legend(['Normal dist. ($\mu=${:.2f} and $\sigma=$ {:.2f} )'.format(mu,sigma)],
			loc='best')
plt.ylabel('Frequency')
plt.title('Item Outlet Sales Distribution')

#Get also the QQ-plot
fig = plt.figure()
res = stats.probplot(data['Item_Outlet_Sales'], plot = plt)
plt.show()

#performing qube root transformation
data['Item_Outlet_Sales']=np.cbrt(data['Item_Outlet_Sales'])

sns.distplot(data['Item_Outlet_Sales'], fit = norm)

#Get the fitted parameters used by function
(mu,sigma) = norm.fit(data['Item_Outlet_Sales'])
print('mean = {:.2f} and standard deviation = {:.2f}'.format(mu,sigma))

#Plot the distribution
plt.legend(['Normal dist. ($\mu=${:.2f} and $\sigma=$ {:.2f} )'.format(mu,sigma)],
			loc='best')
plt.ylabel('Frequency')
plt.title('Item Outlet Sales Distribution')

#Get also the QQ-plot
fig = plt.figure()
res = stats.probplot(data['Item_Outlet_Sales'], plot = plt)
plt.show()
