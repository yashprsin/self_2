# ------------------------- Binary search -----------------------

# Recursive Binary search

def BinarySearch(arr, r, l, x):

    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr, l, mid - 1, x)
        else:
            return BinarySearch(arr, mid + 1, r, x)

    else:

        return -1


arr = [2, 3, 6, 10, 19]
x = 10

result = BinarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
