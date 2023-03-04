from Question import Question
question_prompt = [
    "What is the maximum possible length of an identifier?\n(a) 16\n(b) 32\n(c) 64\n(d) None of these above\n\n",
    "Who developed the Python language?\n(a) Zim Den\n(b) Guido van Rossum\n (c) Niene Stom\n(d) Wick van Rossum\n\n",
    "In which year was the Python language developed?\n(a) 1995\n(b) 1972\n(c) 1981\n(d) 1989\n\n"
]

questions = [
    Question(question_prompt[0],"d"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"d")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompt)
        if answer == question.answer:
            score += 1
    print("Your Score " + str(score) + "/" + str(questions(len)))
run_test(questions)