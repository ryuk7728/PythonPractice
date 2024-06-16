import matplotlib.pyplot as plt
import numpy as np

x=np.array([])
y=np.array([])

for i in range(0,50):
    x=np.append(x,i)
    y=np.append(y,2**(x[i]))


plt.scatter(x,y,color='red')

plt.plot(x,y,color='blue')
plt.show()
