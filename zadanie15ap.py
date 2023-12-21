# from baza_danych_15 import osoby

osoby = [
  { "imie" : "Grażyna", "nazwisko" : "V.", "waga" : 77.9, "wzrost" : 1.38, "rok_urodzenia" : 1951 },
  { "imie" : "Michał", "nazwisko" : "D.", "waga" : 101.4, "wzrost" : 1.4, "rok_urodzenia" : 1912 },
  { "imie" : "Justyna", "nazwisko" : "P.", "waga" : 94.2, "wzrost" : 1.76, "rok_urodzenia" : 1933 },
  { "imie" : "Tomasz", "nazwisko" : "B.", "waga" : 72.9, "wzrost" : 1.43, "rok_urodzenia" : 1960 },
  { "imie" : "Jakub", "nazwisko" : "V.", "waga" : 66.7, "wzrost" : 1.66, "rok_urodzenia" : 1964 },
  { "imie" : "Karol", "nazwisko" : "L.", "waga" : 94.4, "wzrost" : 1.77, "rok_urodzenia" : 1947 },
  { "imie" : "Agnieszka", "nazwisko" : "P.", "waga" : 86.7, "wzrost" : 1.66, "rok_urodzenia" : 1982 },
  { "imie" : "Katarzyna", "nazwisko" : "R.", "waga" : 97.8, "wzrost" : 1.58, "rok_urodzenia" : 1960 },
  { "imie" : "Grażyna", "nazwisko" : "C.", "waga" : 75.4, "wzrost" : 1.52, "rok_urodzenia" : 1958 },
  { "imie" : "Katarzyna", "nazwisko" : "T.", "waga" : 92.7, "wzrost" : 1.79, "rok_urodzenia" : 1936 },
  { "imie" : "Karol", "nazwisko" : "W.", "waga" : 78.9, "wzrost" : 1.82, "rok_urodzenia" : 1973 },
  { "imie" : "Jakub", "nazwisko" : "M.", "waga" : 76.1, "wzrost" : 1.71, "rok_urodzenia" : 1939 },
  { "imie" : "Jakub", "nazwisko" : "T.", "waga" : 83.4, "wzrost" : 1.49, "rok_urodzenia" : 2005 },
  { "imie" : "Agnieszka", "nazwisko" : "M.", "waga" : 85.2, "wzrost" : 1.64, "rok_urodzenia" : 1969 },
  { "imie" : "Justyna", "nazwisko" : "G.", "waga" : 99.3, "wzrost" : 1.86, "rok_urodzenia" : 1968 }
]

"""
print('1. Wszystkie osoby o wzroście powyżej 1.80:')
for persona in osoby:
    nomen, cognomen, altitudo = persona['imie'], persona['nazwisko'], persona['wzrost']
    if altitudo > 1.8:
        print(nomen + ' ' + cognomen)
"""
print()
print('2. Wszystkie osoby urodzone przed 1960 rokiem:')
for persona in osoby:
    nomen = persona['imie']
    cognomen = persona['nazwisko']
    annus_natalis = persona['rok_urodzenia']
    if annus_natalis < 1960:
        print(f'{nomen} {cognomen}')

print('\n3. Wszystkie osoby o wadze poniżej 80:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    pondus = persona['waga']
    if pondus < 80:
        print(nomen + ' ' + cognomen)

print('\n4. Liczba osób z imieniem Jakub:')
numerare = 0
for persona in osoby:
    nomen = persona['imie']
    if nomen == 'Jakub':
        numerare += 1
print(numerare)

print('\n5. Wszystkie osoby wraz z ich BMI:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    pondus = persona['waga']; altitudo = persona['wzrost']
    BMI = pondus / altitudo ** 2
    nomen2 = f'{nomen} {cognomen}'
    print(f"{nomen2:^20}|{BMI:6.1f}")


print('\n6. Największe i najmniejsze BMI:')
max_BMI = 0
min_BMI = 1000000000
for persona in osoby:
    pondus = persona['waga']; altitudo = persona['wzrost']
    BMI = pondus / altitudo ** 2
    if BMI > max_BMI:
        max_BMI = BMI
    if BMI < min_BMI:
        min_BMI = BMI
print(f'Największe BMI: {max_BMI}')
print(f'Najmniejsze BMI: {min_BMI}')