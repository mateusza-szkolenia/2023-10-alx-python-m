a = 0b_1011_1100_1010_1010
b = 0b_1111_0000_1111_0000

print(f'[{a:10b}] {a}')
print(f'[{b:10b}] {b}')

c = a & b # and bitowe
d = a | b # or bitowe
e = a ^ b # xor bitowe
f = b << 1 # przesunięcie bitowe w lewo (mnożenie przez 2^n)
g = b >> 1 # przesunięcie bitowe w prawo (dzielenie przez 2^n)

# print(f'[{c:10b}] {c}')
# print(f'[{d:10b}] {d}')
# print(f'[{e:10b}] {e}')
print(f'[{f:10b}] {f}')

# https://circuitpython.org/

liczba = 3564354

print(f'{liczba:b}')
print( liczba.bit_length ) # nie zadziała tak jak chcemy
print( liczba.bit_length() )
print( liczba.bit_count() )



