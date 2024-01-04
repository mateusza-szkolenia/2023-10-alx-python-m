liczby = [4, 5, 7, 10, 3, 5, 5, 6, 5, 5, 4, 4, 10, 1, 3, 3, 3, 3]

# wynik: [4, 5, 7, 10, 3, 6, 1]
# wypisać unikalne liczby (bez powtórzeń)
# (usunąć duplikaty)
# (oraz ile ich jest)

unikalne = []

for liczba in liczby:
    if liczba not in unikalne:
        unikalne.append(liczba)

print(unikalne)
