# map(func, seq)
a =[1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# similar thing to do
c = [x*2 for x in a]
print(c)

# map(func, seq)
e = [1,2,3,4,5,6]
f = filter(lambda x: x%2==0, e)
print(list(f))

# similar thing to do
g = [x for x in e if x%2==0]
print(g)

# reduce(func, seq)
from functools import reduce
h = [1,2,3,4,5,6]

product_a = reduce(lambda x,y: x*y, h)
print(product_a)
