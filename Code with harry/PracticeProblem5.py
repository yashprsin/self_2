def Next_Palindrome(n):
        while not is_Palindrome(n):
            n += 1
        return n
def is_Palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    size = int(input("Enter the test cases: "))
    numbers = []
    for i in range(size):
        number = int(input("Enter the number: "))
        numbers.append(number)
    print(f"You Enter number of list {numbers}")
    print(f"Palindrome list is : {[numbers[i] if numbers[i] < 10 else Next_Palindrome(numbers[i]) for i in range(size)]}")
    # new_ls = []
    # for element in numbers:
    #     if element > 10:
    #         n = Next_Palindrome(element)
    #         new_ls.append(n)
    #     else:
    #         new_ls.append(element)
    # print(f"Palindrome list: {new_ls}")