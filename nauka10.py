slowo = input("Podaj słowo zawierające literę a oraz dłuższe niż 5 liter: ")

if 'a' in slowo and len(slowo) > 5:
    print("Zawiera A i ma wystarczającą długość")
else:
    print("Źle! (Brak litery A albo za krótkie)")
