# Define the variable with help of tuple

My_tuple = "Max",28,"Boston"

Name,Age,City = My_tuple

print(Name)
print(Age)
print(City)

# Once i don't specify the variable and some variable specify

mytuple = (0,1,2,3,4)

a,*b,c = mytuple

print(a)
print(b)
print(c)
