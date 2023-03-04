def fun(n, *a, **k):
    print(n)
    for i in a:
        print(i)
    for key, value in k.items():
        print(f"{key} is a {value}.")


My_list = ["Yash", "Rohan", "Pawan"]
n = "Some name :"
My_dict = {"Yash":"Programmer", "Pawan":"Teacher", "Rohan":"Cricketer" }

fun(n, *My_list, **My_dict)