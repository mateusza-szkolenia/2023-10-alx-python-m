import random

rzut_k6 = random.randint(1, 6)

rzut_7k6 = [random.randint(1, 6) for _ in range(7)]

# to byłoby źle:
# rzut_7k6 = 7 * [random.randint(1, 6)]
# bo wszystkie 7 wyników pochodziłoby z jednego losowania

wynik = 0
ile_prob = 100000

for numer_rzutu in range(ile_prob):
    rzut_7k6 = [random.randint(1, 6) for _ in range(7)]
    suma_rzutow = sum(rzut_7k6)
    # print(numer_rzutu, rzut_7k6, suma_rzutow)
    if suma_rzutow < 13:
        wynik += 1

print("wynik: ", wynik)
pstwo = 100.0 * wynik / ile_prob
print(f"prawdopodobieństwo: {pstwo}%")
