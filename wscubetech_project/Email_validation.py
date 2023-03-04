"""
Condition :

1. a-z
2. 0-9
3. ".", "_" time 1
4. @ time 1
3. ending "." 2,3
"""
"""
----------------- Regex -----------------------
1. ^        =   starting
2. [ ]      =   range  
3. +        =   joint
4. ?        =   only one can be true
5. \w       =   search for special character
6. {}       =   condition searching
7. $        =   reverse searching
"""
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email : ")

if re.search(email_condition, user_email):
    print("Right email !")
else:
    print("Wrong email !")

# Using of if else
"""
Email = input("Enter your email : ")
k, j, d = 0, 0, 0

if len(Email) >= 6:
    if Email[0].isalpha():
        if "@" in Email and Email.count("@") == 1:
            if (Email[-4] == ".") ^ (Email[-3] == "."):
                for i in Email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():  # Y == y
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                if k == 1 or j == 1 or d == 1:
                    print("Wrong email 5")
                else:
                    print("Right email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
"""
