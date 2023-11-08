'''
Ülesanne 4. Ruutvõrrand
ax^2 + bx + c = 0 on ruutvõrrand. Kirjutada programm, mis laseb sisestada
ruutvõrrandi kordajad (a, b, c) ja leiab reaalarvulised lahendid x1 ja x2.
Arvestada tuleb, et alati ei ole ruutvõrrandil reaalarvulisi
lahendeid (millal? kuidas kontrollida?). Kui ruutliikme kordajaks sisestada 0, siis ei ole üldse ruutvõrrand.
Selles ülesandes on lubatud vahelduseks kasutada muutujaid a, b, c ;) sest nii on inimloetavam.
'''

import cmath

a = float(input("Sisesta kordaja a: "))
b = float(input("Sisesta kordaja b: "))
c = float(input("Sisesta kordaja c: "))

if a == 0:
    print("See ei ole ruutvõrrand.")
else:

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Võrrandil on kaks kaks raalarvulist lahendit - x1 = {x1.real}, x2 = {x2.real}")

    elif discriminant == 0:
        x1 = -b / (2 * a)
        print(f"Võrrandil on üks reaalarvuline lahend: x1 = {x1}")

    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Võrrandil ei ole reaalarvulisi lahendeid -  x1 = {x1}, x2 = {x2}")
