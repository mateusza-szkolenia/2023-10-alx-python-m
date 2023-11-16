######### 012345678
zdanie = "Ala ma kota a kot ma pchły"

print(len(zdanie))
print(zdanie[7])        # tylko siódmy znak = k (uwaga, liczymy od zera)
print(zdanie[7:10])     # tylko 7, 8, 9 znak = kot (uwaga, bez 10.)
print(zdanie[14:])      # od 14. znaku do końca = kot ma pchły
print(zdanie[0:3])      # od początku do 3. znaku = Ala
print(zdanie[:3])       # jak wyżej
print(zdanie[-5:])      # pięć ostatnich znaków
print(zdanie[-5:-3])    # =pc

email = "m.adamowski@alx.pl"

print(email.find('#'))  # -1, bo znaku # nie ma w emailu
print(email.find('@'))  # 11 - pozycja znaku w napisie
