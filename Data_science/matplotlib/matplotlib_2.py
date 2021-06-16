import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)
ax.set_title("Functions")
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle')
ax.yaxis.set_label_text('Sin & cos')
plt.show()