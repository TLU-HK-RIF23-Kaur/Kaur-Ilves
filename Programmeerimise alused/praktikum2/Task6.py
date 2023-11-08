"""
Ülesanne 6. Liigaasta
Kirjutada programm, mis kontrollib, kas sisestatud positiivne täisarv on liig- või lihtaasta number.
(Aasta on liigaasta, kui tema number jagub neljaga, välja arvatud need aastad, mille
number jagub sajaga, kuid ei jagu neljasajaga.)
"""

year = int(input("Sisesta aasta arv: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} on liigaasta.")
else:
    print(f"{year} ei ole liigaasa.")