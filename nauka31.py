# zmiana na użycie requests
# wymaga zainstalowania za pomocą pip:
# py -m pip install requests

import requests
from pprint import pprint

# inny moduł do obsługi pobierania z internetu:
# import requests

# dokumentacja API NBP: http://api.nbp.pl/

table = 'A'
code = 'EUR'
topCount = 10

url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/last/{topCount}/?format=json'

wynik = requests.get(url).json()

print(wynik)

kursy = wynik['rates']

for kurs in kursy:
    print(kurs['mid'])
