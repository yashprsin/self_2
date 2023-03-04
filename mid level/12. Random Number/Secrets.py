import random
import secrets

'''
Only has 3 Function
and they use thing like - Password, Secuhrity Tokens, Account Authentication
DisAdvantage: It take too much time but they will generated ture random
'''
# randbelow method but they not included 10
'''
a = secrets.randbelow(10)
print(a)
'''
# randbits method
'''
a = secrets.randbits(4)
print(a)
'''
# They count range of binary value

# choice method
'''
mylist = list("ABCDEFGH")

a = secrets.choice(mylist)
print(a)
'''

# Similar with using of numpy

import numpy as np

'''
a = np.random.rand(3)
print(a)
'''
# 3 by 3 array
'''
a = np.random.rand(3,3)
print(a)
'''
# random integer in array
'''
a = np.random.randint(0, 10, 3)
print(a)
'''
# Similar i using tuples
'''
a = np.random.randint(0, 10, (3,4))
print(a)
'''

# shuffle method

'''
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)
'''
# They only change array doesn't change element positions

# seed method in numpy

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
