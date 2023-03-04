import time
from functools import lru_cache

"""
@lru_cache(maxsize=3)
def work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':

    work(3)
    print("Working...")
    work(1)
    work(4)
    work(3)

    print("Complete...")
    work(3)
    print("Thank You")
"""
# --------- quiz --------------
# Time give as input of max size
a = int(input("Enter time delay : "))


@lru_cache(maxsize=a)
def work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    name = input("Enter your name : ")
    work(2)
    age = input("Enter your age : ")
    work(5)

    work(2)
    print("Processing......................")
    work(2)
    print(f"Name is - {name}  | \t age - {age} !")


