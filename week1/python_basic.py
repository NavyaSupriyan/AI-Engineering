from collections import deque


# ------------------------------- LISTS ------------------------------------ #

x = [1, 2, 3, 4, 5, 6, 5, 2]
y = [1, 2, 3]

#Append an element to the last of a list
x.append(7)

#Extend: adds the value of an iterable to the end of the list
x.extend(y)

#Insert a value at a given index list.insert(index, value)
x.insert(0, 3)

#del statement allows to removes slices of a list or clear. Provide index or index range
del x[0]
del x[2:4] #(start to end-1 so value at 2, 3 deleted)
del x #removes the reference to the object itself


#remove: Removes the first occurence of an element given its value
x.remove(5)

# pop: It pops an element from a list given its index. If no index given it removes and returns last element
z = x.pop(2)


#clear: removes all the elements in a list -> same as del x[:]
x.clear()

#index: returns the first occursing index of a given value. Optionally we can also provide starting and end ndex
x.index(2)
x.index(2, 1) #return index of first occurence of 2 starting at index 1

#sort
x.sort()

#reverse
x.reverse()

#count: returns the count of a given value
x.count(5)

#Copy: returns a shallow copy of the list x[:]
x = [1, 2, 3, 4, 5, 6, 5, 2]
x.copy()

# Functions that modify the list liek, insert, remove or sort return None

#Using List as Stack

stack = [3,4,5]
stack.append(6)
stack.pop()

#Using List as Queue
#Doing insert and pops at start is not efficient -> use deque

queue = deque(["ava", "jack", "john"])
queue.append("sam")
queue.popleft()

#To create a list of squares from 0 to 5

# map() acts as transformer -> takes and applies a function to each element of an iterable
# lambda is a throwaway function; one line function; lambda input: expression
square = list(map(lambda x: x**2, range(6))) 
square = [x**2 for x in range(6)]

#Transpose a matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]

# ------------------------------- Tuple ------------------------------------ #
#These are immutable heterogenous squenece of elements

#Create an empty tuple
empty = ()

#Create a tuple with only 1 value. With parenthesis it consider as the data type the of the value inside it
singleton = "hello",
singleton1 = ("hello",)

# ------------------------------- SETS ------------------------------------ #
#Data type: Unordered collection with no duplicate entries

#Create an empty set
empty = set()

#Since unordered -> iterating can print elements in diff order
fruits = {'banana', 'orange', 'banana', 'apple'}

# ------------------------------- DICTIONARY ------------------------------------ #
#Unlike sequences which are indexed by range of numbers, dictionary is indexed by keys

dict = {'a': 1, 'b' : 2}
list(dict) #list keys
sorted(dict) #list sorted keys

square = {x: x**2 for x in range(5)}

sample = dict([('age', 23), ('name', 'ravi')])

#To get key and corresponding value together. Set like operations and non indexable
for k, v in dict.items():
    print(k, v)

# ------------------------------- LOOPING TECHNIQUES ------------------------------------ #

#enumerate() used to retreive the value and corresponding index at the same time
for i, v in enumerate(['ava', 'sam', 'lobo']):
    print(i, v)

#reversed() to loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)
# 9, 7, 5, 3, 1

#sorted() -> loop over a sequence in sorted order. returns a new sorted list without altering original

for i in sorted(x):
    print(i)

# set() eliminates duplicates
for i in sorted(set(x)):
    print(i)