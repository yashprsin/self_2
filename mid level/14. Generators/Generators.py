"""def mygen():
    yield 1
    yield 2
    yield 3


g = mygen()
print(g)
"""
"""

def mygen():
    yield 1
    yield 2
    yield 3


g = mygen()

for i in g:
    print(i)
"""

"""
def mygen():
    yield 1
    yield 2
    yield 3


g = mygen()

value = next(g)
print(value)

value = next(g)
print(value)
"""


def mygen():
    yield 4
    yield 2
    yield 3


g = mygen()

# print(sum(g))
print(sorted(g))

