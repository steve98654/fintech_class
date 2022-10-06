import numpy as np 

data = np.random.randn(100) 
mn = np.mean(data)
std = np.std(data)
print(np.cumsum(data)[-1])
print(mn)
print(std)

