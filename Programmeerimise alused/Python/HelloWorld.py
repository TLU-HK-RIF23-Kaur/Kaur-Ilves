import math
import time

print("Hello world!")

# Näidis ülesanne


#kaatet1 = int(input("Sisesta kolmnurga esimese kaateti pikkus ja vajuta enter: "))
#kaatet2 = int(input("Sisesta kolmnurga teise kaateti pikkus ja vajuta enter: "))
#pindala = kaatet1 * kaatet2 / 2
#hypotenuus =math.sqrt(kaatet1**2 + kaatet2**2)
#ymbermoot = math.fsum([kaatet1, kaatet2, hypotenuus])
#print("Kolmnurga pindala on", pindala, "ja ümbermõõt on ", ymbermoot)

# ÜLESANNE 1 Remont
# Kodus on vaja teha remonti. Värvimist vajab ristkülikukujulise toa põrand. Kui palju värvi kulub?
# Teada on toa mõõtmed (pikkus ja laius) meetrites ja värvikulu ruutmeetri kohta.
# Mõtle läbi, millised on algandmed, mida on vaja arvutada ja seejärel koosta lahendamiseks algoritm ja programm.
def task1():
 lengthA = int(input("Sisesta ruumi esimese külje pikkus: "))
 lengthB = int(input("Sisesta ruumi teise külje pikkus: "))
 paintConsumption = int(input("Sisesta värvi kulu ruutmeetri kohta: "))
 paintNeeded = lengthA * lengthB / paintConsumption
 print ("Põranda värvimiseks on vaja " +  str(paintNeeded) + "L värvi")




#ÜLESANNE2 Bussireis
#Lähteandmeteks on bussi väljumisaeg ja saabumisaeg. Leia bussisõidu kestvus.
#Võid eeldada, et reis ei ületa südaööd. Vastus anna tundides ja minutites.








