import requests
"""
with open("currency.txt") as f:
    ls_c = f.readlines()
    cr_dict ={}
    for line in ls_c:
        ps = line.split("\t")
        cr_dict[ps[0]] = ps[1]
print(cr_dict)
amount = int(input("Enter amount : "))
[print(item) for item in cr_dict.keys()]

cr = input("Enter available in option: ")
print(f"{amount* float(cr_dict[cr])}")
"""

url = requests.get("https://www.x-rates.com/table/?from=INR&amount=1").text
content = url.split()
print(url)