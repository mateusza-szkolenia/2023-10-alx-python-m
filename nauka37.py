liczby = [3, 4, 5, 6]

duze_liczby = [x * 1000 for x in liczby]

print(duze_liczby)

print(sum(duze_liczby))

print(sum([x * 1000 for x in liczby]))

print(sum(x * 1000 for x in liczby))

