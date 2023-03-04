SetA = {1,2,3,4,5,6,7,8,9}
SetB = {1,2,3,10,11,12}

SetA_1 = set(SetA).copy()
SetB_1 = set(SetB).copy()


# update difference method

SetA.difference_update(SetB)
print(SetA)

# update symmetric difference

SetA_1.symmetric_difference_update(SetB_1)
print(SetA_1)

# subset method

SetC = {1,2,3,4,5,6}
SetD = {1,2,3}

print(SetC.issubset(SetD))
print(SetD.issubset(SetC))

# note : because that are all the element SetC and SetD
# Super subset method

print(SetC.issuperset(SetD))
print(SetD.issuperset(SetC))

# note : because that are all the element SetC all the element SetD

# Disjoint method

print(SetC.isdisjoint(SetD))

# note : because SetC and SetD some same element

SetE = {7,8}
print(SetE.isdisjoint(SetC))