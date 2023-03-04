print("Hey guys my name is alex.")
print("I am a student and i just start a coding by python.")

String_1 = "joker"
String_2 = "JOKER"
String_3 = "Joker"
String_4 = "I love kiwi, kiwi are my favorite fruit."

# Converts the first character to upper case

print(String_1.capitalize())

# Converts string into lower case

print(String_2.casefold())

# Returns a centered string

print(String_2.center(20))

# Returns the number of times a specified value occur in a string

print(String_4.count("kiwi"))

# Formats specified values in a string

String_5 = "Apple are only {price:.2f} Rupees!"

print(String_5.format(price = 20))

# Searches the string for a specified value and returns the position of where it was found

Animal = "Elephant"

print(Animal.index("p"))

# Returns True if all characters in the string are alphanumeric

password = "Alex123"

print(password.isalnum())
# Returns True if all characters in the string are ascii characters

print(Animal.isalpha())

print(password.isprintable())
print(password.istitle())

txt = " I could eat apple all days"

x = txt.rsplit()
xt = txt.rjust()
print(x)
print(xt)
