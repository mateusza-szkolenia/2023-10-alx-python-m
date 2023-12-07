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
max_dlugosc = 0
min_dlugosc = None
# min_dlugosc = len(imiona[0])
print("Lista uczniów:")
for imie in imiona:
    dlugosc_imienia = len(imie)
    if dlugosc_imienia > max_dlugosc:
        max_dlugosc = dlugosc_imienia
    if min_dlugosc is None or dlugosc_imienia < min_dlugosc:
        min_dlugosc = dlugosc_imienia
    wynik += dlugosc_imienia
    print(f'* {imie} {dlugosc_imienia} ({wynik = })')
print("---KONIEC---")
print(f'sumaryczna długość: {wynik}')
print(f'{max_dlugosc = }')
print(f'{min_dlugosc = }')
# TODO:
#  - napisać sumaryczną liczbę liter
#  - napisać długość najdłuższego imienia
#  - napisać długość najkrótszego imienia
#  - napisać najkrótsze imię
#  - napisać najdłuższe imię
#  - wypisać tylko imiona męskie (bazujemy na końcówce 'a')
#  - wypisać tylko imiona żeńskie (bazujemy na końcówce 'a')