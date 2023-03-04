def exponent_of_the_number(base_number, power_number):
    result = 1
    for index in range(power_number):
       result = result * base_number
    return result

print(exponent_of_the_number(2,4))
print(2**4)
