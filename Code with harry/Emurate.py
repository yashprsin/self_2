ls = ["Apple", "Mango", "Fig", "Orange"]

"""
i = 1
for it in ls:
    if i % 2 == 0:  
        print(f"Buy this {it}")
    i += 1
"""
for i, it in enumerate(ls):
    if i %2 == 0:
        print(it)