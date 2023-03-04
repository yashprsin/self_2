def factorial_iterative(n):
    """

    :param n: Integer
    :return: n * n-1 * n-2....1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def factorial_recursive(n):
    """

    :param n: Integer
    :return: n * n-1 * n-2....1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = int(input("Enter the number: "))
print("Factorial Using Iterative Method : ", factorial_iterative(number))
print("Factorial Using Iterative Method : ", factorial_recursive(number))

