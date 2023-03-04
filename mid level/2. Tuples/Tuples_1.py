# type of tuple define
tuple_1 = ("Raju",28,"Shweta")
tuple_2 = "Name","Age","Collage"
tuple_3 = tuple(["Jio","Airtel","Vodafone"])
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Check the tuple
tuple_4 = ("RAJA")
print(type(tuple_4))
print(type(tuple_1))

# indexing of the tuple
item = tuple_1[-1]
print(item)

# Tuple can not be change of the value
'''
tuple_2[1] = "pawan"
print(tuple_2)
if you print showing error because tuple is immutable
'''
# tuple if you print with help of for loop

for i in tuple_2:
    print(i)

# if condition in tuple check the element

if "Raju" in tuple_1:
    print("Yes in Tuple!")
else:
    print("No, there is no in this Element! ")

# Check how many element in tuple
print(len(tuple_1))

# check the element and how many time the same element

mytuple = ('a','b','c','c','d')
print(mytuple.count('c'))

#print(mytuple.count(input('Enter the element to check: ')))

# indexing of element
print(mytuple.index('d'))

# Converting Tuple in list and list into Tuples

my_list = list(mytuple)
print(my_list)

my_tuple_2 = tuple(my_list)
print(my_tuple_2)

# Specific range in print tuple

a = (1,2,3,4,5,6,7,8)
b = a[1:3]
print(b)
