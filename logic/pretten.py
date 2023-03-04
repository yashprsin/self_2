"""
Sum = 0
ls = []
while True:
    number = input("Enter the price - ")
    if number != 'q':
        ls.append(number)
        Sum = Sum + int(number)
    else:
        break
for i in range(len(ls)):
    print(f"{i+1}.{ls[i]}")
print(f"Total is - {Sum}")
"""
def fac(num):
    if num == 0 or num == 1:
        return 1
    else:
        return  num * fac(num-1)
def tr_zero(num):
    count = 0
    i = 5
    while (num//i != 0):
        count += int(num/i)
        i = i *5
        return count

    # f = fac(num)
    # while f%10==0:
    #     count = count+1
    #     f = f/10
    # return count
if __name__ == '__main__':
    num = int(input("Enter a number - "))
    # print(fac(num))
    print(tr_zero(num))