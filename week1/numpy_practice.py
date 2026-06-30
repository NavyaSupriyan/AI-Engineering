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

d = np.exp(a * 1j) #multiply each element in a with i which is passed as theta to e^i*theta
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
mat = np.array([[1,2,3],[4,5,6]])

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

## SHAPE MANIPULATION
rg = np.random.default_rng() #[0.0, 1.0) 
a = np.floor(10*rg.random((3,4))) #floor so 0.0, 1.0, 2.0.... 9.0
print(a)
# [[4. 1. 0. 7.]
#  [4. 8. 3. 5.]
#  [6. 4. 8. 5.]]

print(a.shape)
#(3, 4)

#ravel: returns the array flattened
print(a.ravel())
#[4. 1. 0. 7. 4. 8. 3. 5. 6. 4. 8. 5.]

#reshape: return the array with modified shape
print(a.reshape(6,2))
# [[4. 1.]
#  [0. 7.]
#  [4. 8.]
#  [3. 5.]
#  [6. 4.]
#  [8. 5.]]

#return the transpose
print(a.T)
# [[4. 4. 6.]
#  [1. 8. 4.]
#  [0. 3. 8.]
#  [7. 5. 5.]]

print(a.T.shape)
# (4, 3)

#resize: similar to reshape but modifies the array itself
a.resize((6,2))
print(a)

#If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated
print(a.reshape(3, -1)) #-1 automatically made 4 as 12 elements are there


##Stacking together diff arrays
a = np.floor(10*rg.random((2,2)))
b = np.floor(10*rg.random((2,2)))

# vertical stack
print(np.vstack((a,b)))
# [[3. 8.]
#  [4. 6.]
#  [3. 8.]
#  [4. 6.]]

# horizontal stack
print(np.hstack((a,b)))
# [[3. 8. 3. 8.]
#  [4. 6. 4. 6.]]

#column stack: stacks 1D array as columns in 2D array
print(np.column_stack((a,b)))
# [[3. 8. 3. 8.]
#  [4. 6. 4. 6.]]

a = np.array([4., 2.])
b = np.array([3., 8.])

print(np.column_stack((a,b)))
# [[4. 3.]
#  [2. 8.]]

print(np.hstack((a,b)))
# [4. 2. 3. 8.]

print(a[:, np.newaxis]) #adds a new axis so inp was (2,) output (1,2)
# [[4.]
#  [2.]]

print(np.column_stack((a[:, np.newaxis], b[:, np.newaxis])))
# [[4. 3.]
#  [2. 8.]]

print(np.hstack((a[:, np.newaxis], b[:,np.newaxis])))
# [[4. 3.]
#  [2. 8.]]

#hstack vs column_Stack: in case of 1D array hstack -> [4. 2. 3. 8.]; column_Stack -> [[4. 3.], [2. 8.]]

#np.concatenate() -> requires arrays to have the exact same number of dimensions. It cannot automatically upgrade 1D arrays into 2D arrays.
print(np.concatenate((a, b), axis=0))  #axis = 1 then out of bound
# [4. 2. 3. 8.]

a_2d = a[np.newaxis, :] # Shape (1, 2)
b_2d = b[np.newaxis, :] # Shape (1, 2)

# axis=0: Stack vertically (row on top of row)
print(np.concatenate((a_2d, b_2d), axis=0))
#[[4. 2.]
# [3. 8.]]

# axis=1: Stack horizontally (end-to-end)
print(np.concatenate((a_2d, b_2d), axis=1))
# Output: [[4. 2. 3. 8.]] 

#np.r_ : row wise stacking
print(np.r_[a, b])
# Output: [4. 2. 3. 8.]

print(np.r_['r', a, b]) ## "r" forces them to turn into row vectors (1, 2) and stack along axis 0
# Output: [[4. 2.]
#          [3. 8.]]

# Takes a and b, turns them into column vectors, and stacks them side-by-side: same as column_stack
#np.c_ : column wise stacking
print(np.c_[a, b])
# Output: [[4. 3.]
#          [2. 8.]]

#The string arguments (like 'r') are only used in the np.r_ command when you want to override its default behavior 
# and force it to stack arrays differently. np.c_ does not accept those configuration strings because its behavior is fixed.

#Splitting

#Using hsplit, you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to 
# return, or by specifying the columns after which the division should occur:

a = np.floor(10*rg.random((2,12)))
print(a)
# [[4. 2. 2. 5. 3. 1. 6. 7. 1. 1. 5. 2.]
#  [7. 7. 4. 5. 4. 6. 1. 7. 8. 3. 2. 8.]]

print(np.hsplit(a,3))
# [array([[4., 2., 2., 5.],
#        [7., 7., 4., 5.]]), array([[3., 1., 6., 7.],
#        [4., 6., 1., 7.]]), array([[1., 1., 5., 2.],
#        [8., 3., 2., 8.]])]

print(np.hsplit(a, (3,4)))
# [array([[4., 2., 2.],
#        [7., 7., 4.]]), array([[5.],
#        [5.]]), array([[3., 1., 6., 7., 1., 1., 5., 2.],
#        [4., 6., 1., 7., 8., 3., 2., 8.]])]

x = np.arange(16.0).reshape(4, 4)
print(np.vsplit(x, 2))
# [array([[0., 1., 2., 3.],
#         [4., 5., 6., 7.]]),
#  array([[ 8.,  9., 10., 11.],
#         [12., 13., 14., 15.]])]

#array_split: splits an array into multiple sub-arrays.

# A 1D array with 7 elements
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Split into 3 sections
result = np.array_split(arr, 3)
print(result)
#[array([10, 20, 30]), array([40, 50]), array([60, 70])]

## Copies
import numpy as np
a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b = a            # no new object is created
print(b is a)           # a and b are two names for the same ndarray object
#True

##View or shallow copy
c = a.view()
print(c is a)
#False
print(c.base is a)            # c is a view of the data owned by a, c.base points to the actual array that owns the data buffer
#True
print(c.flags.owndata) #is a true/false indicator showing whether the array allocates its own memory.
#False

c = c.reshape((2, 6))  # a's shape doesn't change, reassigned c is still a view of a
print(a.shape)
#(3, 4)
c[0, 4] = 1234         # a's data changes
print(a)
# array([[   0,    1,    2,    3],
#        [1234,    5,    6,    7],
#        [   8,    9,   10,   11]])

s = a[:, 1:3]
s[:] = 10  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print(a)
# array([[   0,   10,   10,    3],
#        [1234,   10,   10,    7],
#        [   8,   10,   10,   11]])

#Deep copy: The copy method makes a complete copy of the array and its data.
d = a.copy()  # a new array object with new data is created
print(d is a)
#False
print(d.base is a)  # d doesn't share anything with a
#False
d[0, 0] = 9999
print(a)
# array([[   0,   10,   10,    3],
#        [1234,   10,   10,    7],
#        [   8,   10,   10,   11]])

a = np.arange(int(1e8))
b = a[:100].copy()
del a  # the memory of ``a`` can be released.
