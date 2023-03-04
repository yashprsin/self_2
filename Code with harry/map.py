# --------------Map---------------
"""
# type 1
l = ["1", "2", "3", "4"]
n = list(map(int, l))
n1 = n[2] + n[3] + 1
print(n1)


# type 2
def sq(a):
    return a * a


def cube(a):
    return a * a * a


func = [sq, cube]

ls = [1, 2, 3, 4, 5, 6, ]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)
"""

# ----------Filter Function------------

ls = [1, 2, 3, 4, 5, 6, 7]


def greaterthan_5(num):
    return num > 5


ls2 = list(filter(greaterthan_5, ls))
print(ls2)

# ----------------Reduce-------------

from functools import reduce

ls = [1, 2, 3, 4]
p = reduce(lambda x, y: x + y, ls)
print(p)
