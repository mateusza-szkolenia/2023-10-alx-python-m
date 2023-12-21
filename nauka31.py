import urllib.request
import json
# import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/today/?format=json'

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = json.load(odpowiedz_serwera)

print(wynik)

kurs = wynik['rates'][0]['mid']
print(kurs)