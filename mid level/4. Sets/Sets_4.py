# copy method

SetA = {1,2,3,4,5,6}

SetB = SetA

SetB.add(7)
print(SetA)
print(SetB)
# then modified value

# actual copy method

Set_B = SetA.copy()
Set_B.add(8)
print(Set_B)

# 2nd copy method
Set_C = set(Set_B)
Set_C.add(9)
print(Set_C)

# Frozen Set

a = frozenset([21,33,44])
print(a)

# that sets you can not change value
