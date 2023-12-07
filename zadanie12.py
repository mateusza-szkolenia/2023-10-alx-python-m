# trójkąt

"""
                 numer linii     liczba_kropek       liczba gwiazdek
.......*            0               7                   1
......***           1               6                   3
.....*****          2               5                   5
....*******         3               4                   7
...*********        4               3                   9

                    n               7-n                 2*n + 1
"""

for n in range(5):
    print((7 - n) * '.' + (2 * n + 1) * "*" )
for n in range(3, 7):
    print((7 - n) * '.' + (2 * n + 1) * "*" )
