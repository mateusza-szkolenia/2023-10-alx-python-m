imiona = [
    'Mateusz',
    'Adam',
    'Michał',
    'Iwo',
    'Stanisław',
    'Artem',
    'Karina',
    'Maria',
]

wynik = 0
print("Lista uczniów:")
for imie in imiona:
    dlugosc_imienia = len(imie)
    wynik += dlugosc_imienia
    print(f'* {imie} {dlugosc_imienia} ({wynik = })')
print("---KONIEC---")
print(wynik)

# TODO:
#  - napisać sumaryczną liczbę liter
#  - napisać długość najdłuższego imienia
#  - napisać długość najkrótszego imienia
#  - napisać najkrótsze imię
#  - napisać najdłuższe imię
#  - wypisać tylko imiona męskie (bazujemy na końcówce 'a')
#  - wypisać tylko imiona żeńskie (bazujemy na końcówce 'a')