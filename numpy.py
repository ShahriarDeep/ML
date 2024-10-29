import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Print arrays
print(arr1)
print(arr2)

# Print indexing
print(arr1[0])
print(arr2[2])

# Sum of specific index
print(arr1[0] + arr2[2])

# Sum of two arrays
sum1 = arr1 + arr2
print("Sum of 2 arrays:", sum1)
#in some its work like (0,0+1,0/0,1+1,1)

# Print an element from a 2D array
arr3 = np.array([[1, 2, 3], [6, 7, 8]])
print('2nd element on 2nd row:', arr3[1, 1])

# Sum of specific index in 2D array
print(arr3[0, 2] + arr3[1, 1])

# Print a range of indices
arr4 = np.array([1, 2, 3, 4, 5, 9, 11, 10])
print(arr4[2:5]) 
print(arr4[:5])   
print(arr4[2:])  
print(arr4[-5:-2]) 

# String array
arr5 = np.array(["ami", "tumi", "se"])
print(arr5)

# 3D array
arr6 = np.array([[[1, 2, 3], [6, 7, 8], [4, 5, 9]]])
print(arr6)

# Print type of each array
print(type(arr1))
print(type(arr2))
print(type(arr3))
print(type(arr4))
print(type(arr5))
print(type(arr6))


#some topics may missing here. I am watching the given video. extended deadline is nearby so this version is submitted