import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Creating a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])



arr = np.array([1, 2, 3, 4, 5])

# Element-wise addition
result = arr + 10

# Element-wise multiplication
result = result * 2



data = np.array([12, 18, 21, 25, 30, 35])

# Calculate the mean
mean = np.mean(data)

# Calculate the median
median = np.median(data)

# Calculate the standard deviation
std_dev = np.std(data)


arr = np.array([1, 2, 3, 4, 5])

# Slicing to get a subset
subset = arr[1:4]  # Retrieves elements 2, 3, 4

# Conditional indexing
filtered_data = arr[arr > 2]  # Retrieves elements greater than 2

# print(std_dev)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(A, B)

# Calculate the determinant
det_A = np.linalg.det(A)


random_numbers = np.random.uniform(0, 1, 5)

arr = np.array([[1, 2], [3, 4]])

# Reshape the array
reshaped = arr.reshape(4, 1)

# Transpose the array
transposed = arr.T

print(transposed)