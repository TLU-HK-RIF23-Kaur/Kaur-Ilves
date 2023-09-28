import math

'''
Ülesanne 3 Inimese kehaanalüüs
Uurime inimest. Tundide tabelis on link valemitele, mille abil saab leida inimese ideaalkaalu, rasvaprotsendi, tiheduse,
ruumala ja pindala. Algandmed  kasutaja.
Milliseid algandmed oma arvutusteks vajad?

Leidke esialgu näitajad ühe soo kohta.
Pindala valem nõuab logaritmi leidmist. Selle jaoks on eeldatavasti olemas funktsioon. Abi tuleb otsida moodulist math.
Kontrollimiseks testandmed:
kaal: 75
pikkus: 178
vanus: 22
-------------------
ideaalkaal  mehele: 71.50	naisele: 64.35
rasvasuse % mehele: 19.67	naisele: 36.20
tihedus     mehele: 1058.70	naisele: 1023.98
ruumala     mehele: 0.071	naisele: 0.073
pindala	    mehele: 1.929	naisele: 1.929
'''


def analyze_body():
    age = int(input("Enter age: "))
    length = int(input("Enter length: "))
    weight = int(input("Enter weight: "))
    gender = input("Are you male or female?: ")

    if gender == "male":
        ideal_weight = (3 * length - 450 + age) * 0.25 + 45
    else:
        ideal_weight = (3 * length - 450 + age) * 0.225 + 40.5
    print(f"Ideal weight: {ideal_weight}")

    if gender == "male":
        body_fat_percent = (weight - ideal_weight) / weight * 100 + 15
    else:
        body_fat_percent = (weight - ideal_weight) / weight * 100 + 22
    print(f"Body fat percent: {body_fat_percent}")

    body_density = 8.9 * body_fat_percent + 11 * (100 - body_fat_percent)
    print(f"Body density: {body_density}")

    body_volume = weight / body_density
    print(f"Body volume: {body_volume}")

    body_area = ((1000 * weight) ** (35.75 - math.log(weight)) / 53.2 * length ** 0.3 / 3118.2)
    print(f"Body area: {body_area}")


analyze_body()
