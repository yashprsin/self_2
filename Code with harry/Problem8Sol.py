import random

def Mul(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def is_correct(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1
    return None

if __name__ == '__main__':
    number = int(input("Enter number: "))
    myTable = Mul(number)
    print(myTable)
    wrongIndex = is_correct(myTable, number)
    print(f"The Table is wrong at index {wrongIndex + 1 }")
    # print(Mul(8))