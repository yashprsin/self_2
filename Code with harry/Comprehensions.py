# --------------- print method list -----------------------
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)

print(ls)

# ----------------- printing method for using list compression -------------
ls = [i for i in range(100) if i % 3 == 0]
print(ls)

# ----------- using dictionary --------------------
dict1 = {i: f"Item {i}" for i in range(10) if i % 2 == 0}
print(dict1)
dict2 = {value: key for key, value in dict1.items()}
print(dict2)

# ------------------- Note --------------------
dresses = {dress for dress in ["dress 1", "dress 2", "dress 1", "dress 2", "dress 1", "dress 2", "dress 1", "dress 2", "dress 1", "dress 2", "dress 1", "dress 2"]}
print(dresses)

# --------------------- using Generators ------------------------
evens = (i for i in range(10) if i % 2 == 0)
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())


