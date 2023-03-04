import json
import requests


def speak(str):
    from win32com.client import Dispatch

    text_to = Dispatch("SAPI.spVoice")

    text_to.Speak(str)


if __name__ == '__main__':
    # speak("Please Enter your name")
    # name = input("Enter your name - ")
    # speak(f"Welcome {name}")
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=ec30c149165348289b83a4213a803a7e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    sr = 0
    for i in arts:
        sr += 1
        channel_name = f"{sr} {i['source']['name']}"
        print(channel_name)
    #
    # select_channel_name = input("Enter the number - ")
    #     for articles in arts:
    #         print(f"Headline - {articles['title']}")
    #         # speak(articles['title'])
    # speak("Thank you")