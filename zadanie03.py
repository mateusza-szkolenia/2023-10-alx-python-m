ROK_BIEZACY = 2023

rok_ur = int(input('Podaj rok urodzenia: '))
wiek = ROK_BIEZACY - rok_ur
print(wiek)
if wiek >= 18:
    print('Jesteś pełnoletni')
else:
    print('Nie jestes pełnoletni')
