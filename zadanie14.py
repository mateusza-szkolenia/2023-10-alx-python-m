# zapis specyficzny dla pythona
dol, gora = 0, 1000000

print(f"Wymyśl liczbę z zakresu {dol}..{gora}")
input("Naciśnij enter...")

licznik = 0

while True:
    licznik += 1
    liczba = (dol + gora) // 2
    print(f"Czy jest to {liczba}?")
    odp = input("Odp [+ - =]: ")
    if odp == "+":
        dol = liczba
        continue
    if odp == "-":
        gora = liczba
        continue
    if odp == "=":
        print("Hurra! Zgadłem!")
        break
    print("NIE ROZUMIEM")
    licznik -= 1
print(f"Koniec {licznik}")

