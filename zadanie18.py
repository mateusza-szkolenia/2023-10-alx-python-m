zakres = 12345678

ile_razy = 0

for liczba in range(zakres + 1):
    #print(liczba)
    for cyfra in str(liczba):
        #print(cyfra)
        if cyfra == '8':
            #print("OSIEM")
            ile_razy += 1

print(ile_razy)
# wynik dla 12345678: 8367628
