"""
a = int(input("Enter the A : "))
b = int(input("Enter the B. : "))

print("B greater than A") if a < b else print("A greater than B")
"""

"""
# Functions

def func():
    print("Hello i am function")


func()
"""


def func(a, b, c):
    """This is a function which calculate average of three numbers !"""
    avg = (a + b + c) / 2
    return avg


v = func(13, 44, 51)
print(v)
print(func.__doc__)