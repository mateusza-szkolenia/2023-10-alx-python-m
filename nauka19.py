# jest to dozwolone
rozmaitosci = [123, 56.5, "qwe", [5, 4, 5, 6, 5, 4, 3, 4, 5, 6], True, False, None, 100000000000]

print(rozmaitosci)          # jak wyżej
print(len(rozmaitosci))     # 8
print(rozmaitosci[0])       # 123
print(rozmaitosci[2])       # qwe
print(rozmaitosci[2][1])    # w
print(rozmaitosci[3])       # [5, 4, 5, 6, 5, 4, 3, 4, 5, 6]
print(rozmaitosci[3][0])    # 5
print(len(rozmaitosci[3]))  # 10
