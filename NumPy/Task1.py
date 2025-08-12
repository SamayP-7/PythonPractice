import numpy as np


arr1 = np.arange(10, 51) 
arr2 = arr1[arr1 > 30] 
arr3 = arr1 * 2 
mean_value = np.mean(arr1)
std_dev_value = np.std(arr1)


print(arr1)
print(arr2)
print(arr3)
print(mean_value)
print(std_dev_value)


