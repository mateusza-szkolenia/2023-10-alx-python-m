kwota = float(input('Podaj kwotę:'))
waluta = input('Podaj walutę:')
kurs_USD = 4.20
kurs_EUR = 4.45
kurs_CHF = 4.71

if waluta == "USD":
    kwota_pln = kwota * kurs_USD
elif waluta == "EUR":
    kwota_pln = kwota * kurs_EUR
elif waluta == "CHF":
    kwota_pln = kwota * kurs_CHF
else:
    print(f"Nieznana waluta {waluta}")
    exit(1)

print(f'Kwota {kwota} {waluta} to {kwota_pln} PLN')