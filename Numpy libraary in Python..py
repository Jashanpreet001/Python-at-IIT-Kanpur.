#Introduction to numpy librabray in python.
#One of the most powerful nummerical processing library.
##Numpy provides
#1.Extension package for multi-dimensional array.
#2.Efficient and convenient scientific computing

# Example.Creating a simple array in numpy.
import numpy as np
a = np.array([1, 2, 3, 4])

print(a)

print(np.arange(10))

# L = range(1000)
# %timeit [i**2 for i in L]
#
# a = np.arange(1000)
# %timeit a**2

#Creating arrays.

b = np.array([1, 3, 4]) # 1-D array (VECTOR)
len(a)

c = np.array([[1, 2, 3], [3, 5, 6]]) # 2-D Array (MATRIX)

print(c)
c.shape

d = np.array ([[[0, 1], [1, 2]], [[2, 3], [5, 6]]]) # 3-D array (n-dimensional array: TENSOR)

# Funtions for creating arrays

# using arange function

e = np.arange(1, 10, 3) # start - end - step
e

# Using linspace function

f = np.linspace(0, 1, 5) #start - end - number of points
f

# common arrays functions
g = np.zeroes((3, 3)) # all zeros
print('c\n', c)

h = np.ones((2, 2)) #all ones
print('d\n', p)

#Using diag() function
i = np.diag([1, 2, 3, 5, 0])
print(i)

# Creating a random array
j = np.random.rand(3, 2)
print(j)

## II. Data Types.
k = np.arange(5)
print('k is', k)
print(b.dtype)

#Compplex data types
l = np.array([1+2t, 3+2t])
print(d.type)

# Boolean data types
m = np.array([True, False, True])
print(m.dtype)

### III. Slicing and Indexing
##
##    #Indexing
##    n = np.diag([1, 2, 3, 4])
##    print(a)
##    print(a[2, 2])
##    a[2, 2] = 5
##    print(a)
##
##    #Slicing
##    a = np.arange(10)
##    print(a)
##    a[1:5:2] #[startindex: endindex(not included: step]

