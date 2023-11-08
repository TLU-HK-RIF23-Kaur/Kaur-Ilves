from datetime import datetime
import math

'''
Ülesanne 3. Isikukood
Programmile on sisendiks on kasutaja nimi ja Eesti Vabariigi kodaniku isikukood (IK).
Leia IK-st sünnipäev, sugu ja vanus ning trüki nad võimalikult viisakalt ekraanile:
Lisaks tuleb kontrollida IK õigsust kontrollnumbri kaudu. Selle tegevuse võib jätta ka järgmiseks tunniks.
'''

name = input("Sisesta ees- ja perekonnanimi:")
id_code = input("Sisesta isikukood: ")


def assert_name_is_valid(input_name):
    if any(char.isdigit() for char in input_name):
        print("Nimi ei saa sisaldada numbrit.")
    elif not input_name.strip():
        print("Nimi ei saa olla tühi või sisaldada ainult tühikut/tühikuid.")
    else:
        return True


def get_info_from_id_code(id_code):
    gender_digit = int(id_code[0])
    birth_year = int(id_code[1:3])
    birth_month = int(id_code[3:5])
    birth_day = int(id_code[5:7])

    birth_year += 1800 if gender_digit in {1, 2} \
        else 1900 if gender_digit in {3, 4} \
        else 2000 if gender_digit in {5,6} else 0

    gender = "Mees" if gender_digit in {3, 5} \
        else "Naine" if gender_digit in {4, 6} \
        else "Unknown"

    current_date = datetime.now()
    date_of_birth_as_datetime = datetime(birth_year, birth_month, birth_day)
    date_of_birth_as_string = datetime(birth_year, birth_month, birth_day).strftime("%d.%m.%Y")
    age = math.floor((current_date - date_of_birth_as_datetime).days / 365)

    return date_of_birth_as_string, gender, age


def calculate_control_digit(personal_code):
    multipliers_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    multipliers_2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)

    sum_of_digits_1 = sum(int(personal_code[i]) * multipliers_1[i] for i in range(10))

    remainder = sum_of_digits_1 % 11

    if remainder == 10:
        sum_of_digits_2 = sum(int(personal_code[i]) * multipliers_2[i] for i in range(10))
        remainder = sum_of_digits_2 % 11

    control_digit = 0 if remainder == 10 else remainder

    return control_digit


control_digit = calculate_control_digit(id_code)

if assert_name_is_valid(name):
    if int(id_code[-1]) == control_digit:
        date_of_birth, gender, age = get_info_from_id_code(id_code)
        print(f"Nimi: {name}")
        print(f"Sünnikuupäev: {date_of_birth}")
        print(f"Sugu: {gender}")
        print(f"Vanus: {age} aastane")
    else:
        print(f"{id_code} ei ole valiidne isikukood, palun kontrollige!")
