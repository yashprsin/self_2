n = int(input("Enter the number of apple: "))
min_n = int(input("Minimum user: "))
max_n = int(input("Maximum user: "))

if min_n == max_n:
    print("Range is not valid !")
    exit()
for i in range(min_n, max_n+1):
    if (n % i == 0):
        print(f"{i} is a divisor of {n}")
    elif (n % i != 0):
        print(f"{i} is not divisor of {n}")
