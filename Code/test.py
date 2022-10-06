import numpy as np 
import matplotlib.pyplot as plt

data = np.random.randn(100) 
mn = np.mean(data)
std = np.std(data)
print(np.cumsum(data)[-1])
print(mn)
print(std)
plt.plot(data)
plt.show()