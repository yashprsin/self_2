myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

# using for loops statement

for i in myset:
    print(i)
# if Condition

if 2 in myset:
    print("yes")
else:
    print("No")

# Union and intersection

odds = {1,3,5,7,9}
even = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(even)
i1 = odds.intersection(even)
i2 = odds.intersection(primes)

print(u)
print(i1)
print(i2)

# Difference method (There use of SetA and SetB not consider similar element and also not consider SetB element)

SetA = {1,2,3,4,5,6,7,8,9}
SetB = {1,2,3,10,11,12}

SetA_1 = set(SetA).copy()
SetB_1 = set(SetB).copy()

diff = SetA.difference(SetB)
print(diff)

# 2nd Difference method (There use of SetA and SetB not consider similar element and also consider SetB element)

diff1 = SetA.symmetric_difference(SetB)
print(diff1)

# Update method

SetA.update(SetB)
print(SetA)

# intersection update method

SetA_1.intersection_update(SetB_1)
print(SetA_1)

# update difference method
SetA_1.difference_update(SetB_1)
print(SetA)
