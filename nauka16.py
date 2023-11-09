napis = "X"
print(napis.isupper())


zdanie = "Ala ma kota"
zdanie2 = (zdanie
           .replace("kota", "psa")
           .replace("Ala", "Ania")
           .replace("ma", "zjadła"))
zdanie3 = zdanie.removeprefix("Marysia")
zdanie4 = zdanie.removeprefix("Ala")
# analogiczna metoda .removesuffix()

napis = "  ala ma kota  "

print(len(napis))

print(napis.strip())

