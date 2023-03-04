# 2nd challenge
"""
Dict = {
    "one": 1, "Two": 2, "Three": 3, "Four": 4, "Five":5
        }

Input_of_user = input("Enter Name of the word: ")
print(Dict[Input_of_user])
"""
"""
# 3rd challenge
# input enter user age to eligible you are drive or not and you are 18 to you visit in RTO
User_age = input("Enter your age: ")
if "18" < User_age:
    print("You are Eligible to driving !")
elif "18" == User_age:
    print("You Visit in Driving school to verify, You are Eligible to Drive !")
else:
    print("You are not Eligible to driving !")
"""

"""
# Similar
user_age = int(input("What is your age : "))

if user_age < 7:
    print("You are not eligible to Participate! ")

elif 18 < user_age < 7:
    print("You are not eligible to Drive! ")

elif user_age == 18:
    print("You Visit in Driving school to verify, You are Eligible to Drive !")

elif user_age == 19 < 101:
    print("You are eligible to driving !")
else:
    print("You enter invalid age! ")
"""
# Faulty Calculator

"""# Faulty value: 27- 9 = 16, 16*4 = 54, 2+4 = 10 and 500/5 = 30

Input_1st_number = int(input("Enter your 1st Number: "))
Input_operator = input("Enter your operator ")
Input_2nd_number = int(input("Enter your 2nd Number: "))

if Input_operator == "+":
    Sum = Input_1st_number + Input_2nd_number
    if Input_1st_number == 2 and Input_2nd_number == 4:
        print("Addition of these Number: 10")
    else:
        print("Addition of these Number: " + str(Sum))

elif Input_operator == "-":
    Sub = Input_1st_number + Input_2nd_number
    if Input_1st_number == 27 and Input_2nd_number == 9:
        print("Subtract of these Number: 16")
    else:
        print("Subtract of these Number: " + str(Sub))

elif Input_operator == "*":
    Multi = Input_1st_number * Input_2nd_number
    if Input_1st_number == 16 and Input_2nd_number == 4:
        print("Multiply of these Number: 54")
    else:
        print("Multiply of these Number: " + str(Multi))

elif Input_operator == "/":
    Div = Input_1st_number / Input_2nd_number
    if Input_1st_number == 500 and Input_2nd_number == 5:
        print("Division of these Number: 30")
    else:
        print("Division of these Number: " + str(Div))
else:
    print("Invalid operator")"""
"""
# Make a list in a list number 6 se badi ho

list1 = [["Tom", 4], ["Star", 5], ["Kevin", 18], ["Copper", 10], ["Mini", 20]]

for name, age in list1:
    if age > 6:
        print(name, age)

"""
"""
# give user input execute only 100

i = 0
while True:
    i = i + 1
    User_input = int(input("Enter the Number: "))
    if User_input <= 100:
        continue
    if User_input > 100:
        print("Successfully end the task! ")
        break
    i = i + 1

"""
# Guess the Hidden number and also know as number smaller and greater
"""
Hidden_number = 23
no_of_guesses = 0

print("Guess the Hidden Number: ")
i = 0
while 1:
    i = i + 1
    no_of_guesses = i + 1
    user_input = int(input())
    if no_of_guesses <= 5:
        print("Guess left: ", 5 - no_of_guesses)
        if user_input < Hidden_number:
            print("Enter the Greater no. of ", user_input)
            continue
        if user_input > Hidden_number:
            print("Enter the Smaller no. of ", user_input)
            continue
        if user_input == Hidden_number:
            print("Congratulation you Win the Game !")
            print("You Win only", no_of_guesses - 1, end=" Guesses")
            break
    print("Guess Over! ")
    break

"""

# Pattern Printing
"""
Input = Integer n boolean variable ture ya false
if ture
*
**
***
****
if false 
****
***
**
*
"""
"""

def pattern_boolean_is_ture(n):
    l = []
    for i in range(1, n + 1):
        l.append("*" * i)
    print("\n".join(l))


n = 4
pattern_boolean_is_ture(n)


def pattern_boolean_is_false(n):
    l = []
    for i in range(1, n + 1):
        l.("*" * i)

    reversed = "".join(l)
    print("\n".join(l))


n = 4
pattern_boolean_is_false(n)
"""

"""
No_of_rows = int(input("Enter the number of rows: "))
User_input = int(input("Enter the Boolean variable 0/1 : "))

if User_input == 0:
    boolean = False
    for i in range(No_of_rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("* ", end="")
        print()


elif User_input == 1:
    boolean = True
    for i in range(0, No_of_rows):
        for j in range(0, i + 1):
            print("* ", end="")
        print()
else:
    print("Invalid input")
"""

row = int(input("Enter the number of rows : "))
Boolean_expression = int(input("Enter 0 / 1 "))
pettern = bool(Boolean_expression)
if pettern is True:
    for i in range(1, row+1):
        for j in range(1, i+1):
            print("*", end="")
        print()
elif pettern is False:
    for i in range(row, 0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()
