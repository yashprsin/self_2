Dic_1 = {"Name": "Max","Age": 24, "Email":  "max@cool.com"}
Dic_2 = dict(Name= "Mary",Age= 18, City= "Boston")

# Update dictionary method

Dic_1.update(Dic_2)
print(Dic_1)

# Mutable element

Dic = {3: 9, 4: 16, 6: 36}
print(Dic)

# but using key and value method

value = Dic[4]
print(value)

# But they can not be print indexing wise element

# using tuple in Dictionary

mytuple = (8,9)
Dic = {mytuple: 26}
print(Dic)