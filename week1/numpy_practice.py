import numpy as np


# ------------------------------- BASICS ------------------------------------ #

# Creates a 2D array with 3 rows each having 5 elements and the value being in the range(15)
a = np.arange(15).reshape(3,5)
b = np.array([1,3,5])

# total number of elements of the array (3,5)
print(a.shape)

# total number of elements
print(a.size)

# type of data
print(a.dtype)

# size in byte for each element
print(a.itemsize)

# type method to give type of data -> <class 'numpy.ndarray'>
print(type(a))
print(type(b))

# Converts a seq of seq into a 2D, 3D, etc array
c = np.array([(1.5,2),(3,4)])
print(c)
# [[1.5 2. ]
#  [3.  4. ]]

#Type of array can be explicitly mentioned
d = np.array([[1,2],[3,4]], dtype = complex)
print(d)

# [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]]

#To create an array with 0s. by default data type would be float64
zero = np.zeros((3,4))

#o create an array with 1s
one = np.ones((2,3,4), dtype = np.int16)

# To create an empty array. This creates an array with initial content as random and depends on the state of memory
emp = np.empty((2,3))

# To create a seq of numbers similar to range

rng1 = np.arange(10, 30, 5) #all values in int
rng2 = np.arange(0, 2, 0.3) # all values in float

# when received as an argument the number of elements that we want, instead of the step

lin = np.linspace(0, 2, 9) #9 number from 0 to 2

# to evaluate a function at lots of points
x = np.linspace(0, 2 * np.pi, 100)
f = np.sin(x)
print(f)

# ------------------------------- OPERATIONS  ------------------------------------ #

# Arithmetic operators apply elemntwise. A new array is created and filled with the result

a = np.array([20, 30, 40, 50])
b = np.arange(4)

c = a - b
print(c)

print(b**2)

print(10*np.sin(a))

print(a < 35)

print(a*b) #elementwise

print(a @ b) #matrix product
print(a.dot(b)) #matrix product

# To modify an existing array
a *= 3
a +=1
a+= b #will work if a had float and b has int but not vice-versa

d = np.exp(a * 1j) #multiply each elemnt in a with i which is passed as theta to e^i*theta
print(d)

#Unary operations

a.sum()
a.min()
a.max()

# to perform these opn for a specific axis

b = np.arange(12).reshape(3, 4)
print(b)
#sum of each column
print(b.sum(axis = 0))

#min of each row
print(b.min(axis = 1))

# cumulative sum along each row
print(b.cumsum(axis = 0))

# Universal func: NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc).
B = np.arange(3)

print(np.sin(B))
print(np.exp(B))
print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(np.add(B, C))

# Multi-dimensional indexing
def f(x, y):
    return 10*x + y

b = np.fromfunction(f, (5,4), dtype = int)
# This will create an array of shape (5,4) with each value of typ int calculated using the func f

b[0:5, 1] # each row's second col element
b[: , 1] # same

b[1:3, ] #each col in 2nd and 3rd row

b[-1] # returns last row: b[-1, :] also b[-1, ...]

#The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then
#x[1, 2, ...] is equivalent to x[1, 2, :, :, :]

# Iterating over multidimensional arrays is done with respect to the first axis
# However, if one wants to perform an operation on each element in the array, one can use the flat attribute which is an iterator over all the elements of the array

for i in b.flat:
    print(i)

# Mean of a matrix
mat = np.array([1,2,3],[4,5,6])

#overall mean
print(np.mean(mat))

#column wise mean
print(np.mean(mat, axis = 0))

#row wise mean
print(np.mean(mat, axis = 1))

#Median of a matrix

#overall median
print(np.median(mat))

#column wise median
print(np.median(mat, axis = 0))

#row wise median
print(np.median(mat, axis = 1))