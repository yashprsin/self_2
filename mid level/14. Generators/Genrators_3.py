"""
def fibonacci(limit):

    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

"""
import sys

mygenerators = (i for i in range(10) if i % 2 == 0)
# print(list(mygenerators))
print(sys.getsizeof(mygenerators))

mylist = [i for i in range(10) if i % 2 == 0]
# print(mylist)
print(sys.getsizeof(mylist))