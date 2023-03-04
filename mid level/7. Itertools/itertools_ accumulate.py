from itertools import accumulate
import operator

a = [1,2,3,4]
print(a)

# default is called adding function
acc = accumulate(a)
print(list(acc))

# using multiply function
acc_2 = accumulate(a, func=operator.mul)
print(list(acc_2))

# using max function
b = [1,2,3,4,5,9,8,7,6,]

acc_3 = accumulate(b, func=max)
print(list(acc_3))