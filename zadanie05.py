# obliczanie BMI

# BMI = masa / wzrost^2 [kg / m^2]

waga = float(input("Podaj wagę: [kg] "))
wzrost = float(input('Podaj wzrost: [cm] '))

# wzrost = wzrost / 100
wzrost /= 100

bmi = waga / (wzrost**2)

print(f'BMI wynosi: {bmi}')

