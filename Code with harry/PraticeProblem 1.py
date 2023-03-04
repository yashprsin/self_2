yearAge = int(input("Enter your Age/Year of Birth"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True
else:
    isAge = True

if yearAge<1900 and isYear:
    print("You seem to oldest person alive.")
    exit()

if yearAge>2019:
    print("You are not born")
    exit()

if isAge:
    yearAge = 2021 - yearAge
print(f"You will be 100 year old in {yearAge+100}")

interestYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestYear - yearAge} year old in {interestYear}")