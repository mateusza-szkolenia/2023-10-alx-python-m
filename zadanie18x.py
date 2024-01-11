zakres = 12345678

ile_razy = sum(str(liczba).count("8") for liczba in range(zakres + 1))

print(ile_razy)