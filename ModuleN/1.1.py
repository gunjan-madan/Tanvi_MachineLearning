#Numpy - Numerical Python
#NumPy is a Python library used for working with arrays.
#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

"""---------Intro to Numpy------------"""
print(" ")
print("*** Intro:***")

#install Numpy
#pip install numpy

import numpy
arr1 = numpy.array([1, 2, 3, 4, 5])
print(arr1)

#Create an alias with the as keyword while importing:
#import numpy as np


#The array object in NumPy is called ndarray.
print(type(arr1))

"""---------Dimensions in Array------------"""
print(" ")
print("*** Dimensions:***")
print(" ")
print("***2-D Arrays***")
#2-d arrays
import numpy as np
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

print(" ")
print("***3-D Arrays***")
#3-D arrays
import numpy as np
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

print(" ")
print("***check the Dimensions***")
print("Dimensions in arr1 : ",arr1.ndim)
print("Dimensions in arr2 : ", arr2.ndim)
print("Dimensions in arr3 : ", arr3.ndim)

print(" ")
print("***Type of elements stored***")
print(arr2.dtype)

print(" ")
print("***Specify the type***")
arr2 = np.array([[1, 2, 3], [4, 5, 6]], dtype="float")
print(arr2)

print(" ")
print("***check the Size and shape***")
print(arr2.size)
print(arr2.shape)

print(" ")
print("***reshape***")
arr2=arr2.reshape(3,2)
print(arr2)

print(" ")
print("***Create an array with random values***")
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

#Create a 2-D array of size (3,4) of type float. 
#reshape to (2,6) and print size, type