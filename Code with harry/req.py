import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=68bf21a356376235ef95158146d17d48")
print(r.text)
print(r.status_code)