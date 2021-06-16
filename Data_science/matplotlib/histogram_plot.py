import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')		#it plots look like 'fivethirtyeight.com'

mu = 80
sigma = 7
x = np.random.normal(mu, sigma, size=200)		#used to create an array of random numbers with a normal distrubution

fig, ax = plt.subplots()

ax.hist(x,100)									#build histrogram. first argument is x and second is the number of bars ploted
ax.set_title('New Histogram')
ax.set_xlabel('bin range')
ax.set_ylabel('frequency')

fig.tight_layout()
plt.show()