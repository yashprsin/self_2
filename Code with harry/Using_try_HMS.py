"""
User_list = {1: "Harry", 2: "Cherry", 3: "Akhil"}
log_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select User Name: ")
    for key, value in User_list.items():
        print("Enter", key, "For", value, "\n", end="")
    User_name = int(input("\n"))

    print("Select User: ", User_list[User_name], "\n", end="")

    print("Enter 1 for Log")
    print("Enter 2 for Retrieve")
    op = int(input())

    if op == 1:
        for key, value in log_list.items():
            print("Press", key, "to Log", value, "\n", end="")
        log_name = int(input())
        print("Select Job : ", log_list[log_name])
        f = open(User_list[log_name] + "_" + log_list[log_name] + ".txt", "a")
        k = "y"
        while k != "n":
            print("Enter", log_list[log_name], "\n", end="")
            My_text = input()
            f.write("[ + str(getdate()]:" + My_text + "\n")
            k = input("Add More ? y/n :")
            continue
        f.close()
    elif op == 2:
        for key, value in log_list.items():
            print("Enter", key, "To Retrieve", value, "\n", end="")
        log_name = int(input())
        print(User_list[User_name] +"." + log_list[log_name], "Report:", "\n", end="")
        f = open(User_list[User_name] + "_" + log_list[log_name] + ".txt", "rt")
        Content = f.readline()
        for line in Content:
            print(line, end="")
        f.close()
    else:
        print("Invalid input !!")
except Exception as e:
    print(e)


"""
from File import joke

joke("Pawan")
