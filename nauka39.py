import random

kolory = ["zielony", "niebieski", "czerwony", "biały", "żółty", "czarny", "brązowy", "różowy", "fioletowy"]

kolor = random.choice(kolory)

print(kolor)

# bez powtórzeń
kilka_kolorow = random.sample(kolory, 3)
print(kilka_kolorow)

rozne_kolory = random.choices(kolory, k=8)
print(rozne_kolory)
