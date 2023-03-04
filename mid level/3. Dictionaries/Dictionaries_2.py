Dic = {"Name": "Max","Age": 24, "City":  "New york"}
print(Dic)

# Condition method is two type e.g.

if "Name" in Dic:
    print("Element in Dictionary")
else:
    print("Element in not a Dictionary")

# When Second example

if "lastname" in Dic:
    print("Element in Dictionary")
else:
    print("Element is not in Dictionary")

# When we using try method
try:
    print(Dic["Name"])
except:
    print("Error")

# try fail e.g.
try:
    print(Dic["Lastname"])
except:
    print("Error")

# Using For loop in Dictionary

for key in Dic:
    print(key)

for key_2 in Dic.keys():
    print(key_2)

for value in Dic.values():
    print(value)

# You print both this

for key_3 ,value_2 in Dic.items():
    print(key_3,value_2)

# Copy of Dictionary

Dic_copy = Dic
# If we modified the Dictionary
Dic_copy["Email"] = "max@xyz.com"
print(Dic_copy)
print(Dic)

# Resolve the Problem
Dic_copy_2 = Dic_copy.copy()
Dic_copy_2["Fav Fruit"] = "Fig"
print(Dic_copy_2)

# also you can use

Dic_copy_3 = dict(Dic_copy_2)
Dic_copy_3["Fav Game"] = "Baseball"
print(Dic_copy_3)

