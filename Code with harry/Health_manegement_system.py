def getdate():
    import datetime
    return datetime.datetime.now()


def take(Select_Category):
    if Select_Category == 1:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            value = input("Type Here !\n")
            with open("Rohan-ex.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")
        elif c == 2:
            value = input("Type Here !\n")
            with open("Rohan-Diet.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")
    elif Select_Category == 2:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            value = input("Type Here !\n")
            with open("Hammad-ex.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")
        elif c == 2:
            value = input("Type Here !\n")
            with open("Hammad-Diet.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")

    elif Select_Category == 3:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            value = input("Type Here !\n")
            with open("Harry-ex.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")
        elif c == 2:
            value = input("Type Here !\n")
            with open("Harry-Diet.txt", "a") as file:
                file.write(str([str(getdate())]) + ": " + value + "\n")
            print("Done.")


def retrieve(Select_Category):
    if Select_Category == 1:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            with open("Rohan-ex.txt") as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open("Rohan-Diet.txt") as file:
                for i in file:
                    print(i, end="")
    elif Select_Category == 1:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            with open("Hammad-ex.txt") as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open("Hammad-Diet.txt") as file:
                for i in file:
                    print(i, end="")
    if Select_Category == 3:
        c = int(input("Enter key:\n 1. Exercises\n2. Diet"))
        if c == 1:
            with open("Harry-ex.txt") as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open("Harry-Diet.txt") as file:
                for i in file:
                    print(i, end="")


print("Welcome to Health managements System")
User_access = int(input("Enter Key:\n1. Log\n2. Retrieve\n"))
if User_access == 1:
    Select_user_for_log = int(input("Enter Key:\n1.Rohan\n 2.Hammad\n 3.Harry\n"))
    take(Select_user_for_log)
else:
    Select_user_for_retrieve = int(input("Enter Key:\n1.Rohan\n 2.Hammad\n 3.Harry\n"))
    retrieve(Select_user_for_retrieve)
