# Sets: unordered, mutable, no duplicates
myset = {1,2,3}
print(myset)

# when i use duplicate value
myset_1 ={1,2,3,1,2}
print(myset_1)

# Declare different type

myset_2 = ([3, 4, 5])
print(myset_2)

myset_3 = set("hello")
print(myset_3)

# type method

myset_4 = {}
myset_5 = set()
print(type(myset_4))
print(type(myset_5))

# add method

myset_5.add(1)
myset_5.add(2)
myset_5.add(3)

print(myset_5)

# remove method
myset_1.remove(3)
print(myset_1)

# discard method

myset_5.discard(1)
print(myset_5)

# clear method

myset_5.clear()
print(myset_5)

# pop method
myset = set([4,5,6,7])

print(myset.pop())
print(myset)
