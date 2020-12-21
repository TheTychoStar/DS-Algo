import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
print("first random data: ", data)

# data * 10
data = data * 10
print("Data times 10: ", data)

# try np shape
print("Data shape: ", data.shape)

# Print data value's type
print("Data types:", data.dtype)

# Create a new ndarray
data_forarray = [6, 7.5, 8, 0, 1]
np_array = np.array(data_forarray)
print("Np array is: ", np_array )
# create a second ndarry
data_forarray2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
np_array2 = np.array(data_forarray2)
# create a 1D array
data_forarray3 = [10]
np_array3 = np.array(data_forarray3)

# Demo broadcasting, array 1 + array3
print("Broadcasting, array1 + array3:  ", np_array+np_array3)

# numpy array indexing and slicing
np_array4 = np.arange(10)
print("Initialize an array in range 10: ", np_array4)

# print out the range 5:8. The 5th, 6th and 7th values will be printed out. The 8th value won't
print("The range 5:8 is: ", np_array4[5:8])

# assign a slicing
array_slice = np_array4[5:8]
array_slice[1] = 12345
print("After slicing: ", np_array4)
array_slice[:] = 64
print("Second slicing: ", np_array4)

# Create  a 2 dimensional array
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("The second element of array: ", array2d[1])
print("The 3rd value of 2nd sub array: ", array2d[1][2])

# Create a 3 Dimensional array
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("The 3D array is: ", array3d)

