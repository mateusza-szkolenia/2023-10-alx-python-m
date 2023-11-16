# obliczanie BMI

# BMI = masa / wzrost^2 [kg / m^2]

waga = input("Podaj wagę: ")
waga_mnoznik = 1

if waga.endswith('kg'):
    print(f"Podałeś wagę w kilogramach: [{waga}]")
    waga = waga.removesuffix('kg')
elif waga.endswith('g'):
    print(f"Podałeś wagę w gramach: [{waga}]")
    waga = waga.removesuffix('g')
    waga_mnoznik = 0.001

waga = float(waga) * waga_mnoznik

wzrost = input('Podaj wzrost: ')
wzrost_mnoznik = 1

if wzrost.endswith('cm'):
    wzrost = wzrost.removesuffix('cm')
    wzrost_mnoznik = 0.01
elif wzrost.endswith('m'):
    wzrost = wzrost.removesuffix('m')

wzrost = float(wzrost) * wzrost_mnoznik

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