import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,10,15,20,25])

plt.grid(axis="y",color="Maroon",linestyle="dashed") #Linewidth, #

plt.plot(x,y)

plt.show()