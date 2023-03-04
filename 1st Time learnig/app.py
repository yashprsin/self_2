from Que import Que

que_prompts = [
    "Less than 2?\n(a) 3\n(b) 3\n (c)1\n\n",
    "Less than 2?\n(a) 3\n(b) 3\n (c)1\n\n",
    "Less than 2?\n(a) 3\n(b) 3\n (c)1\n\n",
]


ques = [
    Que(que_prompts[0],"c"),
    Que(que_prompts[0],"c"),
    Que(que_prompts[0],"c"),
]

def run_test(ques):
    score = 0
    for que in ques:
        ans = input(que_prompts)
        if ans == que.ans:
            score +=1
    print("Your score : " + str(score) + "/" + str(que(len)))

run_test(ques)