f = open("yash.txt")
try:
    f1 = open("yash.txt")
except Exception as r:
    print(r)
else:
    print("Exception is not running")
finally:
    print("Finish your work")
    f.close()
