
'''
Ülesanne 5 Jalgrattur ja kärbes
Jalgrattur on oma kodust 5 km kaugusel ja ta liigub maja suunas kiirusega 15 km/h.
Kui jalgrattur sõitmist alustab, stardib tema otsaesiselt kärbes lennates kiirusega 40 km/h maja suunas. Jõudnud
majani pöörab ta kiirust kaotamata ümber ja lendab tagasi. Jõudnud jalgratturini, pöördub ta taas ringi ja nii
pendeldab õnnetu pea kaotanud kärbes ühtlase kiirusega edasi-tagasi seni kuni ta maja ja ratturi otsaesise vahel oma
kurva lõpu leiab. Jalgratturi edasisest saatusest ajalugu vaikib. Kui pika tee läbis kärbes enne oma õnnetut lõppu.
Hoolimata ülesande tekstis olevatest arvudest tee lahendus universaalne, mis lubab sisestada erinevaid andmeid.
'''

distance_from_home = int(input("Sisesta kaugus kodust: "))
cyclist_speed = int(input("Sisesta ratturi kiirus: " ))
fly_speed = int(input("Sisesta kärpse kiirus: " ))

fly_total_travel_distance = distance_from_home / cyclist_speed * fly_speed

print(f"Kärbes läbis selle ajaga {fly_total_travel_distance}km")