'''
Ülesanne 1. Jagamine
Sisesta kaks arvu ja jaga esimene arv teisega. Kui arve jagada ei tohiks, siis anna
adekvaatne veateade. Arve ei tohiks jagada siis, kui jagaja on null (0).
'''

number_1 = int(input("Sisesta arv nr 1: "))
number_2 = int(input("Sisesta arv nr 2: "))

if number_2 != 0:
    print (f"vastus on {number_1 / number_2}")
else:
    print ("Nulliga ei saa jagada!")
