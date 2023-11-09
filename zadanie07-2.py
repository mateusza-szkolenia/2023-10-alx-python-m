slowo = input("Podaj słowo dłuższe niż 5 liter i zawierające 'nie': ")

if len(slowo) > 5 and 'nie' in slowo:
    print(f"{slowo} jest OK")
else:
    print(f"{slowo} nie jest OK")
