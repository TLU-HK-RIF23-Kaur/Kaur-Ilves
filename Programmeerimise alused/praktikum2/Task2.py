"""
Ülesanne 2. Kolmnurk
Sisesta kolmnurga kolm külge. Otsusta, kas kolmnurga saab moodustada. Kui saab, siis määra,
kas tegemist on võrdhaarse (kaks külge võrdsed), võrdkülgse (kõik kolm külge võrdsed) või "lihtsalt" kolmnurgaga.
"""

triangle_side_1 = int(input("Sisesta kolmnurga esimese külje pikkus: "))
triangle_side_2 = int(input("Sisesta kolmnurga teise külje pikkus: "))
triangle_side_3 = int(input("Sisesta kolmnurga kolmanda külje pikkus: "))

if (triangle_side_1 + triangle_side_2 > triangle_side_3
        and triangle_side_2 + triangle_side_3 > triangle_side_1
        and triangle_side_3 + triangle_side_1 > triangle_side_2):

    if triangle_side_1 == triangle_side_2 == triangle_side_3:
        print("Tegemist on võrdkülgse kolmnurgaga")
    elif triangle_side_1 == triangle_side_2 or triangle_side_2 == triangle_side_3 or triangle_side_3 == triangle_side_1:
        print("Tegemist on kahe võrdse küljega kolmnurgaga")
    else:
        print("Tegemist on \"lihtsalt\" kolmnurgaga")
else:
    print("Kolmnurka ei saa moodustada! Kolmnurga kahe suvalise külje pikkuste summa on alati suurem kolmanda külje "
          "pikkusest.")