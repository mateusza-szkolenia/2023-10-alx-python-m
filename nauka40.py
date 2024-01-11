nazwa_pliku = 'dane.txt'

suma = 0

with open(nazwa_pliku, 'r') as plik:
    for linia in plik:
        x = int(linia)
        suma += x
        print(x)

print(suma)

plik_wynikowy = "wynik.txt"

with open(plik_wynikowy, 'w') as plik:
    plik.write(f"suma wynosi: {suma}\n")
