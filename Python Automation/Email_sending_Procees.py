import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()


def extract_news(url):
    print("Extracting News from Google News...")
    cnt = ''
    cnt += ('<b> Google news Headlines :</b>\n'+'<br>'+'-'*50+'<br>')

# cnt = extract_news("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

ur = requests.get("https://www.indiatoday.in/").text
