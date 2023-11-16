"""
Napisać program, który:

* zapyta użytkownika o adres email
* "ocenzuruje" adres email,
   tzw. przykładowy adres: `m.adamowski@alx.pl`
   zamieni na `m__________@a_____` (liczba podkreśleń musi się zgadzać)

"""

email = input("Podaj email: ")

pierwsza_litera = email[0]

ocenzurowany_email = pierwsza_litera + 'XXXXX'

print(f"Twój email to: {ocenzurowany_email}")

