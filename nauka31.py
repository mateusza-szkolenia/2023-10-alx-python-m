import urllib.request
import json
from pprint import pprint

# inny moduł do obsługi pobierania z internetu:
# import requests

# dokumentacja API NBP: http://api.nbp.pl/

table = 'A'
code = 'EUR'
topCount = 10

url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/last/{topCount}/?format=json'

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = json.load(odpowiedz_serwera)

print(wynik)

kursy = wynik['rates']

for kurs in kursy:
    print(kurs['mid'])
