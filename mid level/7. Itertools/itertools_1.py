# product, permutations, combinations, accumulate, groupby and infinite interators
from itertools import product
from itertools import permutations
a = [1,2]
b = [3,4]
c = [3]

prod = product(a,b)
print(list(prod))

# using repeat
prod = product(a,c, repeat=2)
print(list(prod))

# permutation
d = [1,2,3]
perm = permutations(d)
print(list(perm))
# if i print Second value

e = [1,2,3]
perm_2 = permutations(e, 2)
print(list(perm_2))

