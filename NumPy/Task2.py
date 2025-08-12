import numpy as np

arr1 = np.arange(1,10).reshape(3,3)
print(arr1)
arr2 = arr1.flatten()
print(arr2)

print(arr1[1])
arr2[-1]=100
print(arr2)