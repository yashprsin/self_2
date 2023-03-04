
try:
    value = 10/0
    Number = print(int(input("Enter the Number : ")))
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invaild Input")