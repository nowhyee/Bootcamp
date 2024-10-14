import numpy as np
#Q1
# Define two custom numpy arrays, say A and B.
# Generate two new numpy arrays by stacking A and B vertically and horizontally.

A = np.array([1, 2, 3, 4, 5])
B = np.array([6, 7, 8, 9, 10])

vertical = np.vstack((A, B))
print("Vertical Stack:\n", vertical)

horizontal = np.hstack((A, B))
print("Horizontal Stack:\n", horizontal)

#Q2
# Find common elements between A and B.
# [Hint : Intersection of two sets]
common_elements = np.intersect1d(A, B)
print("Common Elements:", common_elements)

#Q3
# Extract all numbers from A which are within a specific range.
# eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]

# Using boolean masking
proper = A[(A >= 5) & (A <= 10)]
print("Numbers within range (5 to 10):", proper)

#Q4
# Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

# Filter the rows with petallength > 1.5 and sepallength < 5.0
filtered = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
print("Filtered Rows:\n", filtered)

indices = np.where((A >= 5) & (A <= 10))
proper_nums = A[indices]
print("Numbers within range (5 to 10) using np.where():", proper_nums)
