# import pomidor

from random import randint

tajna_liczba = randint(0, 1000000)

print("Wylosowałem tajną liczbę.")

proby = 0

while True:
    x = int(input("Zgadnij liczbę: "))
    proby += 1
    if x == tajna_liczba:
        print("Brawo!")
        break
    if x < tajna_liczba:
        print("Za mało")
    if x > tajna_liczba:
        print("Za dużo")

print(f"Liczba prób: {proby}")