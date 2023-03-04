import random

def Guess_Game(a, b, autual_number):
    guess = int(input(f"Guess number between {a} and {b}\n"))
    no_of_guess = 1
    while guess != actual_number:
        if guess < autual_number:
            guess = int(input("Enter a bigger number : "))
            no_of_guess += 1
        else:
            guess = int(input("Enter a smaller number : "))
            no_of_guess += 1
    print(f"Your number of guess is {no_of_guess}")
    return no_of_guess

if __name__ == '__main__':
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    actual_number = random.randint(a, b)
    print("Player 1 Chance: ")
    g1 = Guess_Game(a, b, actual_number)
    print("\nPlayer 2 Chance: ")
    g2 = Guess_Game(a, b, actual_number)
    if g1 < g2:
        print("\nPLayer 1 is Won")
    elif g1 > g2:
        print("\nPLayer 2 is Won")
    else:
        print("Tie")