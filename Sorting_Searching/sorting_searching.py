
# coding: utf-8

# # Sets

# In[16]:


import random

set1 = []
set2 = []

for _i in range(0,10):
    set1.append(random.randint(0,10))
for _i in range(0, 10):
    set2.append(random.randint(0,10))
    
set1 = set(set1)
print(set1)

set2 = set(set2)
print(set2)

both = set1 & set2
print(both)


# In[17]:


a = {1,2,3,5,1,2,5,1,4}
b = {3,5,1,2,5,6,7,2,3,7}

set1 = a & b
print(set1)


# # Storting and Searching
# 

# In[25]:


cat = 14
if cat > 10:
    print("Welcome to middle age cat!")

x = 0
while x < 5:
    print("Hello")
    x = x + 1
    
for i in range(0,10):
    print("Goodbye")
    
def my_function():
    print("Im doing something")
    print("I am a function that is working hard.")
    
for i in range(0,5):
    my_function()


# In[48]:


# Sorting
import random
import timeit

def switch(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return array

def smallest(array):
    i = 0
    index = 0
    smallest = array[0]
    while i < len(array):
        value = array[i]
        if value < smallest:
            smallest = value
            index = i
        i = i + 1
    return (smallest, index)

def sort(array):
    # Loop through the list elements
    i = 0
    while i < len(array) - 1:
        # Check if there is a smaller element later in the list
        small, index = smallest(array[i + 1:])
        # If there is:
        if small < array[i]:
            # Switch the element we are looking at with the smallest value
            array = switch(array, i, index+i+1)
        i = i + 1
def setup():
    b = []
    for i in range(0,10000):
        b.append(random.randint(0,50))
    return b

if __name__ == '__main__':
    a = [9,4,4,5,1,3,0]
    sort(a)
    print(a)
    print(smallest(a))

    num = 10
    t1 = timeit.timeit('sort(b)', setup='b = setup()', globals=globals(),number=num) / num
    t2 = timeit.timeit('a.sort()', setup='a = setup()', globals=globals(), number=num) / num

    print(t1)
    print(t2)


# In[80]:


# Searching

def has_value(array, value):
    i = 0
    while i < len(array):
        if array[i] == value:
            return i
        i = i + 1
    return False

def setup():
    b = []
    for i in range(0,1000000):
        b.append(random.randint(0,50))
    return b
a = setup()

num = 1000000
t1 = timeit.timeit('binary_search(a, 9)', setup='a = setup(); a.sort()', globals=globals(), number = num) / num
print(t1)

t2 = timeit.timeit('a.index(9)', setup='a = setup()', globals=globals(), number = num) / num
print(t2)
      
def binary_search(array, value):
    # This assumes that the array is sorted!!!!!
    low = 0
    high = len(array) - 1
    while low < high:
        mid = int((low + high) / 2)
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False

a = setup()
a.sort()
print(binary_search(a, -1))

