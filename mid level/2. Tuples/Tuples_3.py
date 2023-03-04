# Compare list and tuples

import sys

Mylist = [0, 1, 2, "Hello", True]
Mytuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(Mylist),"bytes")
print(sys.getsizeof(Mytuple),"bytes")
