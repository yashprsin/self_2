# String : order, immutable, text representation

my_sting_1 = "Hello World"
print(my_sting_1)

my_sting_2 = 'Hey Pycharm'
print(my_sting_2)

my_sting_3 = 'I\'am a programmer.'
print(my_sting_3)

# you use a string as documentation
Documentation = """Hello Everyone My name is Max.
and I am a Programmer."""
print(Documentation)

Documentation_2 = """Hello Everyone My name is Max \
and I am a Programmer."""
print(Documentation_2)

# indexing
my_sting_4 = "Hello world"
char = my_sting_4[1]
print(char)

# Note: String are immutable You can change in after the string declaration

substring = my_sting_4[0:5]
print(substring)

substring_2 = my_sting_4[::2]
print(substring_2)

substring_3 = my_sting_4[::-1]
print(substring_3)

# Concatenated String
greeting = 'Hello'
Name = 'Tom'
Sentance = greeting + ' ' + Name
print(Sentance)

# Using for loop

for x in greeting:
    print(x)

# Using if
if 'H' in my_sting_4:
    print("yes")
else:
    print("No")
if 'Hello' in my_sting_4:
    print("yes")
else:
    print("No")

String = '             hello  World!'
print(String)

# Removing White Space
remove_white_space = String.strip()
print(remove_white_space)

# Convert String in UpperCase and LowerCase
uppercase = remove_white_space.upper()
print(uppercase)
lowercase = remove_white_space.lower()
print(lowercase)

# Check the String End and Started method
Str1 = "Hello World"
print(Str1.startswith("H"))
print(Str1.startswith("Hello"))
print(Str1.startswith("d"))
print(Str1.startswith("World"))

print(Str1.endswith("H"))
print(Str1.endswith("Hello"))
print(Str1.endswith("d"))
print(Str1.endswith("World"))

# using find element
print(Str1.find("H"))
print(Str1.find("lo"))
print(Str1.find("pp"))
# can not find a Sting how the -1

# Using count Statement
print(Str1.count('p'))
print(Str1.count('H'))
print(Str1.count('l'))

# Replace Statement
print(Str1.replace('World','Universe'))
