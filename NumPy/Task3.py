import numpy as np

arr = np.array([5, 12, 17, 23, 45, 50, 66])
print(arr)

even_numbers = arr[arr % 2 == 0]
print(even_numbers)

greater_than_20_count = np.sum(arr > 20)
print(greater_than_20_count)

arr[arr < 20] = 0
print(arr)