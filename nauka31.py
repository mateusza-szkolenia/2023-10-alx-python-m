import urllib.request
import json
# import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/2020-05-11/?format=json'

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = odpowiedz_serwera.read()


print(wynik)