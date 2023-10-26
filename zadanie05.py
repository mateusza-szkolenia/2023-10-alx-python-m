# obliczanie BMI

# BMI = masa / wzrost^2 [kg / m^2]

waga = float(input("Podaj wagę: [kg] "))
wzrost = float(input('Podaj wzrost: [m] '))

# wzrost = wzrost / 100
# wzrost /= 100

"""
Kategoria 	BMI (kg/m²)
wygłodzenie 	< 16,0
wychudzenie 	16,0–16,99
niedowaga 	17,0–18,49
pożądana masa ciała 	18,5–24,99
nadwaga 	25,0–29,99
otyłość I stopnia 	30,0–34,99
otyłość II stopnia (duża) 	35,0–39,99
otyłość III stopnia (chorobliwa) 	≥ 40,0 
"""

bmi = waga / (wzrost**2)

if bmi < 16.0:
    werdykt = 'wygłodzenie'
elif bmi < 17.0:
    werdykt = 'wychudzenie'
elif bmi < 18.5:
    werdykt = 'niedowaga'
elif bmi < 25.0:
    werdykt = 'OK'
elif bmi < 30.0:
    werdykt = 'nadwaga'
elif bmi < 35.0:
    werdykt = 'otylosc I stopnia'
elif bmi < 40.0:
    werdykt = 'otylosc II stopnia'
else:
    werdykt = 'otylosc III stopnia'

print(f'BMI wynosi: {bmi} {werdykt}')
