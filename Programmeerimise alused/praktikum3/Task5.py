"""
Ülesanne 5 Spordipäev
Koolis oli spordipäev ja lapsed viskasid palli. Iga õpilase kohta on teada tema parim vise. Eraldi saame sisestada Pauli tulemuse. Leia, mitmenda koha Paul saavutas.
(Nt: Paul sai palliviskes 4 koha.)
Ülesande täienduses võib eraldi tuuakse välja kohtade jagamine.
(Nt: Paul jagas 2 kuni 4 kohta.)
"""

def find_pauls_place(throws, pauls_throw):

    all_throws = throws + [pauls_throw]
    sorted_throws = sorted(all_throws, reverse=True)

    pauls_place = sorted_throws.index(pauls_throw) + 1

    shared_places = [i + 1 for i, throw in enumerate(sorted_throws) if throw == pauls_throw]
    if len(shared_places) > 1:
        shared_places_str = f"Paul jagas  palli viskes {min(shared_places)}. kuni {max(shared_places)}. kohta."
    else:
        shared_places_str = f"Paul sai  palli viskes {pauls_place}. koha."

    return pauls_place, shared_places_str


students_throws = [55, 43, 65, 45, 70, 55, 67, 30, 56, 77, 80, 75, 54, 63, 67,60,  34, 46, 48, 66, 67, 70, 60, 55, 43, 65,]
pauls_throw = int(input("Sisesta Pauli tulemus: "))

place, shared_place_str = find_pauls_place(students_throws, pauls_throw)
print(shared_place_str)