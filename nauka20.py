# operacje na listach

# dodawanie list powoduje powstanie nowej listy
chlopcy = ['Marek', "Piotrek", "Karol"]
dziewczyny = ["Ania", "Asia", "Basia"]

wszyscy = chlopcy + dziewczyny

print(wszyscy)

# dodawanie elementów do listy
chlopcy.append("Zenon")
print(chlopcy)

# podmiana elementów
chlopcy[2] = "Kazimierz"
print(chlopcy)

# usunięcie elementu
del chlopcy[1]
print(chlopcy)

# dodawanie wielu elementów
panowie = ["Bogdan", "Bogusław", "Bogumił"]
#chlopcy.extend(panowie)
# ['Marek', 'Kazimierz', 'Zenon', 'Bogdan', 'Bogusław', 'Bogumił']
# ['Marek', 'Kazimierz', 'Zenon', ['Bogdan', 'Bogusław', 'Bogumił']]
chlopcy.append(panowie)

print(chlopcy)
