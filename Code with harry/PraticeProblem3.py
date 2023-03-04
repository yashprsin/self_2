print("Enter list element one by one")
size = int(input("Enter the list size: "))
ls = []

for i in range(size):
    ls.append(int(input("Enter the element : ")))
print(f"There is original list: {ls}")

# type 1
r1 = ls[:]
r1 = r1[::-1]
print(f"\nType 1 is : {r1}")

# Type 2
r2 = ls[:]
for i in range((len(r2))//2):
    r2[i], r2[len(r2)-i -1] = r2[len(r2)-i -1], r2[i]

print(f"Type 2 is : {r2}")

# Type 3
r3 = ls[:]
r3.reverse()
print(f"Type 3 is : {r3}")

if r1 == r2 and r2 == r3:
    print("All reversed list is same !")

