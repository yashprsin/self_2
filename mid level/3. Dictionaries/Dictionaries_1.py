# Type of define Dictionary

Dic = {"Name": "Max","Age": 24, "City":  "New york"}
print(Dic)

Dic_2 = dict(Name= "Mary",Age= 18, City = "Boston")
print(Dic_2)

value = Dic["Name"]
print(value)

# Add the element to add in Dictionary

Dic["Email"] = "max@xyz.com"
print(Dic)

# Then you overwritten

Dic["Email"] = "coolmax@xyz.com"
print(Dic)

# if you can delete item we have several option for Example:

del Dic["Email"]
print(Dic)

Dic.pop("Age")
print(Dic)

Dic_2.popitem()
print(Dic_2)

