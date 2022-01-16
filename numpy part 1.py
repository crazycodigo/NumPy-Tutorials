'''
This contains all the functions demonstrated in NumPy (part 1).
Link to video: https://youtu.be/u-yn7np77XM
'''

# importing module
import numpy as np

# creating array
arr = np.array([])

# creating array with one row
arr = np.array([1,2,3])

# shape of array
print(arr.shape)

# creating n-dimensional array
arr = np.array([[1,2,3], [4,5,6]])

# finding dimension of array
print(arr.ndim)

# referencing a certain index of n-dimensional array
print(arr[1][2])

# pointing memory address where array is stored
print(arr.data)

'''
Link to DEV blog: https://dev.to/crazycodigo/numpy-part-1-5d2b
Part 2 out soon.
'''