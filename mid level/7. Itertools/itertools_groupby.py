from itertools import groupby

def smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_object = groupby(a, key=smaller_than_3)
for key, value in group_object:
    print(key, list(value))

# lambda function
person =[{'Name' : 'Tim', 'age' : 24},{'Name' : 'Lisa', 'age' : 24},
         {'Name' : 'kevin', 'age' : 25}, {'Name' : 'Max', 'age' : 26}

         ]

group_object = groupby(person, key=lambda x: x['age'])
for key, value in group_object:
    print(key, list(value))
