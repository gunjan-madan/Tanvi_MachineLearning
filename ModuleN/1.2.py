# operations


"""---------Arithmetic operations------------"""
print(" ")
print("*** Addition:***")


import numpy as np
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)


#Joining two arrays
print(" ")
print("*** Join:***")
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


#Joining 2-D arrays
print()
#To joing 2-D arrays, axis is set to 0 if needs to add more rows. To add more columns, set it to 1

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


#Splitting the arrays
print()

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

#If the array has less elements than required, it will adjust from the end accordingly.