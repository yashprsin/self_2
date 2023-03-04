'''
Author - Yash
Date - 16-11-2021
Purpose - Practice
'''


def next_Even(n):
    n = n + 1
    while not (n//2):
        n = n + 1
    return n


def next_Palindrome(n):
    n = n+1
    while not is_Palindrome(n):
        n += 1
    return n

def is_Palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the Number of test cases: "))
    numbers = []

    for i in range(n):
        number = int(input("Enter the number: "))
        numbers.append(number)

    for i in range(n):
        print(f"Next Palindrome for {numbers[i]} is {next_Palindrome(numbers[i])}")
        print(f"Next Even for {numbers[i]} is {next_Even(numbers[i])}")

