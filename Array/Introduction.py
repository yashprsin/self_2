import array

arr = array.array("i", [1, 2, 3])
print("First Array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

arr.append(4)
print("After append array is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")
arr.insert(2, 5)
print("After insert array : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")
