import random

Choice = ["Snake", "Water", "Gun"]
# Game rule Snake and water = Snake, Water and Gun = Water, Snake and Gun = Gun

Total_Chance = int(input("HOW MUCH MANY TIMES TO PLAY !!! \n"))
No_of_chance = 0
pc_score = 0
your_score = 0

while No_of_chance < Total_Chance :
    print(f"Choose : {Choice}!")
    user = input()
    random1 = random.choice(Choice)

    if user == random1:
        print("Draw\n")

    elif user == "Snake" and random1 == "Gun":
        your_score = your_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Win !")

    elif user == "Snake" and random1 == "Water":
        pc_score = pc_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Lose !")

    elif user == "Water" and random1 == "Snake":
        pc_score = pc_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Lose !")

    elif user == "Water" and random1 == "Gun":
        your_score = your_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Win !")

    elif user == "Gun" and random1 == "Snake":
        your_score = your_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Win !")

    elif user == "Gun" and random1 == "Water":
        pc_score = pc_score + 1
        print(f"Your Choose {user} and Computer Choose {random1}")
        print("You Lose !")

    else:
        print("You have Invalid Input !!")

    No_of_chance = No_of_chance + 1


if your_score == pc_score:
    print("Draw Match !")
elif your_score > pc_score:
    print("You Win !")
else:
    print("Computer Win !")




