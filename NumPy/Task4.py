import numpy as np

matrix = np.random.randint(1, 101, (5, 5))

print(matrix)


max_value = np.max(matrix)
min_value = np.min(matrix)

print(max_value)
print(min_value)


row_sums = np.sum(matrix, axis=1)

print(row_sums)


matrix[matrix > 50] = -1

print(matrix)



