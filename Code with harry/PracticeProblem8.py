import random


def Table_Multi(n):
    w = random.randint(4, 8)
    for i in range(10):
        i += 1
        i = n * i
        table.append(i)

    table.pop(w)

    table.insert(w, n * w + 1)
    return table


def is_Correct(n):
    c = 0
    for i in table:
        c += 1
        if i % n != 0:
            print(f"Table is Wrong {i} Correct is {c * n}")
            check1 = int(input("If you want a new list \nPress any  key\n1.Yes\t2.No\n"))
            if check1 == 1:
                c = c - 1
                table.pop(c)
                table.insert(c, (c + 1) * n)
                print(table)


if __name__ == '__main__':
    n = int(input("Enter your number to print table : "))
    table = []
    ps = Table_Multi(n)
    print(ps)
    check = int(input("Check your table is Correct\nPress any  key\n1.Yes\t2.No\n"))
    if check == 1:
        is_Correct(n)
    else:
        print("Thank you")
