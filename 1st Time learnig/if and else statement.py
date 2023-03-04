is_male = False
is_tall = True

if is_male and is_tall:
    print("Ya there is a male and also be a tall person !")

elif is_male and not(is_tall):
    print("Person is a male but is not a tall !")

elif is_tall and not(is_male):
    print("Person is not tall but is male person !")
else:
    print("There is not a male and also be not tall !")


# condition statement of is else condition

def max_value_number(n1,n2,n3):

    if n1>=n2 and n1>=n2:
        return n1

    elif n2>=n1 and n2>=n3:
        return n2

    else:
        return n3

print(max_value_number(3,50,6))