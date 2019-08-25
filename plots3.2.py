#myplot.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.savefig('plot1_3.2.png')
plt.savefig('E:/analytics/plots/plot1.png')
plt.show()
 # import when running from script 
import matplotlib.image as mpimg
img = mpimg.imread('plot1.png')
print(img)
imgplot = plt.imshow(img)
