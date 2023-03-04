import pickletools
import re
str = """
Name - yash
class - 7th
contact - 9029009109
email - yashpratap@gmail.com
Name - pawan
class - 11th
contact - 9032909109
email - pawankumar@gmail.com
Name - shellu
class - 12th
contact - 9229009109
email - shellu@gmail.com
Name - Rose
class - 7th
contact - 9219009109
email - rose@gmail.com
Name - Queen
class - 7th
contact - 90290098993
email - imqueen@gmail.com
"""
# pat = re.compile(r'(<)?(\w+@\w+(?:\.\w+)+)')
# email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
# print(email)
i = input()
Email = re.search('(.+)'+i+'(.+)',str)
for i in Email:
    print(Email)

