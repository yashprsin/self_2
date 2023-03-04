list1 = ["Tom", 'Sam', "Jerry", "Perry", 5, 9.33]
"""list2 = [13, 4, 5, 6, 7, 3, 344, 64363]
print(list1)
# list2.sort()
list2.reverse()
print(list2)
"""
"""l1 = [1,2,3,4,5,6,7]
# index = seq = l1[Start:Stop:Step]
seq = l1[0:4:]
print(seq)
l1.append(8)
l1.append(9)
l1.insert(0, 11)
# l1.remove(3)
print(l1)
list1.remove("Tom")
print(type(list1))
print(list1)
"""
"""my_list = [1,2,3,4]
my_list.pop(4)
print(my_list)
"""
"""
# tuple in python
a = (1, 2, 3, 4)

print(type(a))"""
"""
a = 5
b = 6
print(a, b)
a, b = b, a
print(a, b)

l1 = []

l1.append(input("Enter your 1st item: "))
l1.append(input("Enter your 2nd item: "))
l1.append(input("Enter your 3rd item: "))
l1.append(input("Enter your 4th item: "))
l1.append(input("Enter your 5th item: "))
l1.insert(5, 502)
print(l1)
"""
"""
print("Enter first number : ")
n1 = input()
print("Enter second number : ")
n2 = input()
print("Sum of these number : ", int(n1) + int(n2))
"""
from collections import OrderedDict


# Function to remove all duplicates from string
# and order does not matter
def removeDupWithoutOrder(str):
    # set() --> A Set is an unordered collection
    #		 data type that is iterable, mutable,
    #		 and has no duplicate elements.
    # "".join() --> It joins two adjacent elements in
    #			 iterable with any symbol defined in
    #			 "" ( double quotes ) and returns a
    #			 single string
    return "".join(set(str))


# Function to remove all duplicates from string
# and keep the order of characters same
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))


# Driver program
if __name__ == "__main__":
    str = "geeksforgeeks"
    print("Without Order = ", removeDupWithoutOrder(str))
    print("With Order = ", removeDupWithOrder(str))

