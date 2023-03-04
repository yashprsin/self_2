import json

# data = '{"var1" : "herry" , "var2" : 56}'
# parsed = json.loads(data)
#
# print(parsed['var1'])
#
# data2 = {
#     "channel_name": "8deadlyjoker",
#     "cars": ['bmw', 'audi', 'honda'],
#     "Hosue_item": ('Oil', 'vegetable oil', 'kiwi', 560),
#     "isbad": False
# }
# jscomp = json.dumps(data2)
# print(jscomp)
#  x = {
#     "name": "john",
#     "age": 44,
#     "children": ("anny", "willy"),
#     "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x, indent=4, separators=(",", " " "=" " ")))

# print(json.dumps(x, indent=4, sort_keys=True))
my_details = {

    "Name" : "Lalit Salunkhe",

    "Age" : 28,

    "Job" : True,

    "Married" : False,

    "Bikes" : [

        {"Model1": "Jupiter 120", "price": 62000},

        {"Model2": "Yamaha YZF-R15", "price": 150000}

        ]

    }

#Using file I/O operation to create a new json file into working directory

with open("Data_File.json", "w") as file:

#Using json.dump() to write the data into a JSON file.

    json.dump(my_details, file)

x = open("Data_File.json")
print(x)

# Using python I/O open function to read the json file named Data_File.

with open("C:\\Users\\jo\\PycharmProjects\\test1\\Code with harry\\Data_File.json") as file:
    # Using json.load() to deserialize a python object into python object

    Py_object = json.load(file)

    print(Py_object)

    print(type(Py_object))