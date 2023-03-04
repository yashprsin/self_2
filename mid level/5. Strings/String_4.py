# Using %
var = "Tom"
my_string = "The variable is %s " %var
print(my_string)

# using decimal
var2 = 3
my_string = "The variable is %d " % var2
print(my_string)

# using Float
var3 = 3.7838462
my_string = "The variable is %f " % var3
print(my_string)
my_string = "The variable is %.3f " % var3
print(my_string)

# format method
my_string = "The variable is {} " .format(var3)
print(my_string)
my_string = "The variable is {:.2f} " .format(var3)
print(my_string)
my_string = "The variable is {:.2f} and {} " .format(var3,var2)
print(my_string)
my_string = f"The variable is {var3} and {var2}"
print(my_string)
my_string = f"The variable is {var3*2} and {var2}"
print(my_string)
my_string = f"The variable is {var3*var2}"
print(my_string)
my_string = f"The variable is {var3:.4} and {var2}"
print(my_string)
my_string = f"The variable is {var3*var2:.6}"
print(my_string)




