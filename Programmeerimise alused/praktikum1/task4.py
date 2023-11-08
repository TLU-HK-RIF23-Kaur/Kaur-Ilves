

'''
Ülesanne 4 Sisseastumine Loe ülesanne lõpuni, et teada saada, millised on algandmed ja mida küsitakse ;)
Gümnaasiumi lõpetanud soovivad astuda TLÜsse informaatika erialale. Sissesaamisel kehtib lävend (65 punkti). Vastu
võetakse kõik kandidaadid, kelle eksamitelt kogutud punktisumma (niinimetatud vastuvõtupall) ületab lävendi.
Vastuvõtupall arvutatakse eesti keele riigieksami ning vastuvõtueksami tulemuste põhjal. Riigieksam annab
vastuvõtupalli 25% ning vastuvõtueksam 75%. Vastuvõtueksam koosneb omakorda kahest osast - testist ja vestlusest,
kus mõlema osa eest saab maksimaalselt 50 punkti (kokku 100 p).

Algandmetena on teada eesti keele riigieksami ja vastuvõtueksami testi tulemused ning lävendi suurus.
Kui palju peab üliõpilaskandidaat vestlusel lävendi ületamiseks vähemalt punkte saama?

Testandmed
----------
riigieksam     test     vestlus
100              50        3.33
 60              40       26.67
 50              30       40.00
'''

threshold_for_matriculation = 65
language_exam_proportion = 0.25
admission_exam_proportion = 0.75
admission_test_max = 50
admission_interview_max = 50

language_exam_points = int(input("Sisesta eesti keele riigieksami tulemus:"))
admission_test_points = int(input("Sisesta vastuvõtueksami testi tulemused: "))

language_exam_as_threshold = language_exam_points * 0.25
admission_test_as_threshold = admission_test_points * 0.75

threshold = language_exam_as_threshold + admission_test_as_threshold
if threshold < threshold_for_matriculation:
    points_needed_in_interview = int((threshold_for_matriculation - threshold))/ 0.75

print(f"Keeleeksami puntkid lävendis: {language_exam_as_threshold}")
print(f"Testi tulemused lävendis: {admission_test_as_threshold}")
print(f"Saavutatud lävend: {threshold}")
print(f"Punkte vaja vestlusel, et saavutada lävend: {points_needed_in_interview}")







