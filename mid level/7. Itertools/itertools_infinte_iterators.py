from itertools import count, cycle, repeat
'''
for i in count(10):
    print(i)

'''


# 2 e.g.
'''
for x in count(10):
    print(x)
    if x == 15:
        break
'''
# cycle function
''''
a = [1,2,3]
for i1 in cycle(a):
    print(i1)
'''
# repeat function
a = [1,2,3]
for i in repeat(1,4):
    print(i)
