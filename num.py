import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Basic operations
sum_arr = arr1 + arr2  # Element-wise addition
diff_arr = arr2 - arr1  # Element-wise subtraction
prod_arr = arr1 * arr2  # Element-wise multiplication
div_arr = arr2 / arr1  # Element-wise division

# Printing results
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Sum of arrays:", sum_arr)
print("Difference of arrays:", diff_arr)
print("Product of arrays:", prod_arr)
print("Division of arrays:", div_arr)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)

# Printing matrix multiplication result
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Product:")
print(matrix_product)
