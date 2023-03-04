'''
def cal():

    def add():
        n1 = input("Enter 1st number : ")
        n2 = input("Enter 2nd number : ")
        r1 = int(n1) + int(n2)
        return r1

    add_result = add()
    print(add_result)

    def sub():
        n1 = input("Enter 1st number : ")
        n2 = input("Enter 2nd number : ")
        r2 = int(n1) - int(n2)
        return r2

    sub_result = sub()
    print(sub_result)

    def mul():
        n1 = input("Enter 1st number : ")
        n2 = input("Enter 2nd number : ")
        r3 = int(n1) * int(n2)
        return r3

    mul_result = mul()
    print(mul_result)

    def div():
        n1 = input("Enter 1st number : ")
        n2 = input("Enter 2nd number : ")
        r4 = int(n1) / int(n2)
        return r4

    div_result = div()
    print(div_result)

'''

n1 = float(input("Enter your first number : "))
n2 = float(input("Enter your second number : "))
operator_name = input("Enter name of operator \n OR \n Operator : ")
# op = input("Enter your operator : ")
'''
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("Invalid operator ! ")
'''

if operator_name == "Addition" or "addition":
    print(n1+n2)
elif operator_name == "Subtraction" or "subtraction":
    print(n1-n2)
elif operator_name == "Multiply" or "multiply":
    print(n1*n2)
elif operator_name == "Divide" or "divide":
    print(n1/n2)
elif operator_name == "+":
    print(n1+n2)
elif operator_name == "-":
    print(n1-n2)
elif operator_name == "*":
    print(n1*n2)
elif operator_name == "/":
    print(n1/n2)
else:
    print("Invalid operator name OR Operator ! ")
