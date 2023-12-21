import urllib.request
import json
# import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/2020-05-11/?format=json'

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = odpowiedz_serwera.read()

print(wynik)

wynik2 = json.loads(wynik)

print(wynik2)

kurs = wynik2['rates'][0]['mid']
print(kurs)