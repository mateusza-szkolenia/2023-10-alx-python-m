liczba_t = input("Podaj liczbę: ")

if liczba_t.isdecimal():
    liczba = int(liczba_t)
    print(f"Liczba o jeden większa wynosi {liczba + 1}")
else:
    print("To nie liczba")
