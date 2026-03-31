import numpy as np
import random
import pandas as pd 

# student_marks = [1,2,3]

# n = np.array([1, 2, 3])
# n = np.array([1, 2, 3],dtype = float)
# n = np.array([1, 2, 3],dtype = str)

# print(type(n))
# print(n)
# print(n[0])
# print(n[2])
# print(n.dtype)

# x = np.zeros([3,4],dtype = int)
# y = np.ones([3,4],dtype = int)
# print(x)
# print(y)

# print(np.random.random([2,2]))
# first = np.array([1,2,3])
# second = np.array([4,5,6])
# print(np.add(first,second))


dataset1 = pd.DataFrame({
    "index": [0, 1, 2, 3],
    "a" : [4, 5, 6, 7],
    "b" : [8, 9, 10, 11],
    "c" : [12, 13, 14, 15],
})
print(dataset1)