import matplotlib.pyplot as plt
import numpy as np
#print(matplotlib.__version__)
#%matplotlib inline
x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)

plt.xlabel("time")
plt.ylabel("volatage")
plt.title("sine wave voltage graph")
plt.legend(['Data 1'])
plt.plot(x,y)
plt.savefig('sine_wave.png', dpi=350, bbox_inches='tight')
plt.show()

