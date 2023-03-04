"""def countdown(num):
    print("Strating")
    while num > 0:
        yield num
        num -= 1


cd = countdown(2)

value = next(cd)
print(value)

print(next(cd))
"""
import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generotors(n):
    num = 0
    while num < n:
        yield num
        num += 1




# print(sum(firstn(10)))

print(firstn(10))
print(sum(firstn_generotors(10)))
print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generotors(100000)))
# Now if a use a generators
