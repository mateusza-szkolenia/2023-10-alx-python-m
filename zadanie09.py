"""
Napisać program, który:

* zapyta użytkownika o adres email
* "ocenzuruje" adres email,
   tzw. przykładowy adres: `m.adamowski@alx.pl`
   zamieni na `m__________@a_____` (liczba podkreśleń musi się zgadzać)

"""

email = input("Podaj email: ")

pierwsza_litera = email[0]

pozycja_at = email.find('@')

pierwsza_litera_domeny = email[pozycja_at + 1]

dlugosc_domeny = len(email) - (pozycja_at + 1)

ocenzurowany_email = pierwsza_litera + '_' * (pozycja_at - 1) + '@' + pierwsza_litera_domeny + '_' * (dlugosc_domeny - 1)

print(f"Twój email to: {ocenzurowany_email}")

