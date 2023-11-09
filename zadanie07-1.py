liczba = int(input("podaj liczbę parzystą większą niż 17: "))

if liczba % 2 == 0 and liczba > 17:
    print(f"Liczba {liczba} spełnia warunki")
else:
    print(f"Liczba {liczba} nie spełnia warunków")
