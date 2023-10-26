tekst = input("Napisz cokolwiek: ")

dlugosc_tekstu = len(tekst)

print(f'{dlugosc_tekstu = }')

print(f'{len(tekst) = }')

if "a" not in tekst:
    print("Nie ma 'a'")
else:
    print("Tak, jest 'a'")
