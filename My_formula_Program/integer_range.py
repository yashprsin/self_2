n1 = input("Enter the value of N: ")

if n1 == "1":
    max_range = pow(2, 7)
    print("Value of byte:  " + "-" + str(max_range) + " to " + str(max_range - 1))
elif n1 == "2":
    max_range = pow(2, 15)
    print("Value of short:  " + "-" + str(max_range) + " to " + str(max_range - 1))
else:
    print("Invalid input")