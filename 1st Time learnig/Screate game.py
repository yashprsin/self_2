# While loop

print("What's the first thing caterpillar eat after it's born ? ")
answer = "it's own eggshell"
user_answer = ""
user_answer_count = 0
user_limits = 3
out_of_limits = False


while user_answer != answer and not(out_of_limits):
    if user_answer_count < user_limits:
        user_answer = input("Enter Correct Answer : ")
        user_answer_count += 1
    else:
        out_of_limits = True

if out_of_limits:
    print("Out of limits \nYou lose the game! ")
else:
    print("Correct answer !\nYou Win")
'''
# For loops

for latter in "Apple is good for health !":
    print(latter)
'''
'''# 2nd example

Friends = ["Abhishek","Aunj","Aditiya"]

for Friend in Friends:
    print(Friend)'''