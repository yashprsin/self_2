# ------------- Linear search ----------------------------


# Simple way


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i, print(i)
        return -1


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
x = 3

result = search(arr, n, x)
if result == -1:
    print("Match found !")
else:
    print("Match not found !")
