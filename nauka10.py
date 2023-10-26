slowo = input("Podaj słowo zawierające literę a oraz dłuższe niż 5 liter: ")

if 'a' in slowo:
    print("Zawiera A")
else:
    print("Źle! Brak litery A")

if len(slowo) > 5:
    print("Prawidłowa długość")
else:
    print("Za krótkie")
