"""
File operations ----

"r" - Open file for reading - default
"w" - Write file for writing
"x" - Creates file if not exist
"a" - Add more content to file
"t" - text mode - default
"b" - Binary mode
"+" - Read and write mode
"""
# open file
"""
f = open("yash.txt", "rt")
content = f.read()
print(content)
f.close()

f = open("yash.txt", "rt")
for line in f:
    print(line, end="")
"""
"""
print(f.readline())
print(f.readline())
"""
"""
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
"""

"""
print(f.readline())
f.seek(0)
print(f.readline())
"""
"""
# open file block case:
with open("yash.txt") as f:
    a = f.read(4)
    f.seek(0)
    b = f.readline()
    print(b)
"""
a = 7
b = 10


def joke(str):
    print(f"{str} are big fool like dunk asshole.")