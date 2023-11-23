miesiace = ['styczeń',
            'luty',
            'marzec',
            'kwiecień',
            'maj',
            'czerwiec',
            'lipiec',
            'sierpień',
            'wrzesień',
            'październik']

numer_miesiaca = int(input("Podaj numer miesiąca: "))

print(miesiace[numer_miesiaca - 1])

# https://en.wikipedia.org/wiki/Off-by-one_error