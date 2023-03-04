def add(a, b):
    return a + b


print(add(5, 6))

clone_add = lambda x, y: x - y

print(clone_add(9, 4))


def a_first(a):
    return a[1]


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=a_first)
print(a)

b = [[1, 14], [5, 6], [8, 23]]
b.sort(key=lambda x: x[1])
print(b)
