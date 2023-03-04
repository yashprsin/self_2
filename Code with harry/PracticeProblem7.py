import re


def matching_words(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {words1} with {words2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    # matching_words("this is good" , "python is good")
    sentences = ["this is good", "python is good", "python is not python snake", "Hello yash"]
    query = input("-------- Search --------\n")
    scores = [matching_words(query, sentence) for sentence in sentences]
    print(scores)
    sorted_Sent_res = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    print(sorted_Sent_res)

    print(f"\n{len(sorted_Sent_res)} result found! ")
    for score, item in sorted_Sent_res:
        if score != 0:
            print(f"\"{item}\": with a score of {score}")