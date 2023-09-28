
'''
ÜLESANNE 1 Remont
Kodus on vaja teha remonti. Värvimist vajab ristkülikukujulise toa põrand. Kui palju värvi kulub?
Teada on toa mõõtmed (pikkus ja laius) meetrites ja värvikulu ruutmeetri kohta.
Mõtle läbi, millised on algandmed, mida on vaja arvutada ja seejärel koosta lahendamiseks algoritm ja programm.
'''

def task_1():
    length_a = int(input("Sisesta ruumi esimese külje pikkus: "))
    length_b = int(input("Sisesta ruumi teise külje pikkus: "))
    paint_consumption = int(input("Sisesta värvi kulu ruutmeetri kohta: "))
    paint_needed = length_a * length_b / paint_consumption
    print("Põranda värvimiseks on vaja " + str(paint_needed) + "L värvi")
