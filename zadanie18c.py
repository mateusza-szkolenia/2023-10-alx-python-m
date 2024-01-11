zakres = 12345678

ile_razy = 0

for liczba in range(zakres + 1):
    #print(liczba)
    napis = str(liczba)
    ile_osemek = napis.count("8")
    # print(liczba, ile_razy)
    ile_razy += ile_osemek

print(ile_razy)
# wynik dla 12345678: 8367628
