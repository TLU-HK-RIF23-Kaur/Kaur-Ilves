from datetime import datetime

'''
ÜLESANNE2 Bussireis
Lähteandmeteks on bussi väljumisaeg ja saabumisaeg. Leia bussisõidu kestvus. 
Võid eeldada, et reis ei ületa südaööd. Vastus anna tundides ja minutites.
'''

'''Minu neli erinevat lahendust Ülesandele nr 2'''

def task_solution_1():
    departure_time_str = input("Sisesta väljumisaeg (formaat HH:MM) : ")
    arrival_time_str = input("Sisesta saabumisaeg (formaat HH:MM) : ")

    departure_hours_str, departure_minutes_str = departure_time_str.split(':')
    departure_total_minutes = int(departure_hours_str) * 60 + int(departure_minutes_str)

    arrival_hours_str, arrival_minutes_str = arrival_time_str.split(':')
    arrival_total_minutes = int(arrival_hours_str) * 60 + int(arrival_minutes_str)

    trip_duration_hours = (arrival_total_minutes - departure_total_minutes) // 60
    trip_duration_minutes = (arrival_total_minutes - departure_total_minutes) % 60

    print(f"Bussireisi kestvus on {trip_duration_hours:02d}:{trip_duration_minutes:02d}")

def task_solution_2():
    departure_time_str = input("Sisesta väljumisaeg (formaat HH:MM) : ")
    arrival_time_str = input("Sisesta saabumisaeg (formaat HH:MM) : ")

    departure_hours_str, departure_minutes_str = departure_time_str.split(':')
    departure_total_minutes = int(departure_hours_str) * 60 + int(departure_minutes_str)

    arrival_hours_str, arrival_minutes_str = arrival_time_str.split(':')
    arrival_total_minutes = int(arrival_hours_str) * 60 + int(arrival_minutes_str)

    minutes_in_day = 1440
    if arrival_total_minutes >= departure_total_minutes:
        trip_duration_hours, trip_duration_minutes = divmod(arrival_total_minutes - departure_total_minutes, 60)
    else:
        trip_duration_hours, trip_duration_minutes = (
            divmod(minutes_in_day - departure_total_minutes + arrival_total_minutes, 60))

    print(f"Bussireisi kestvus on {trip_duration_hours:02d}:{trip_duration_minutes:02d}")


def task_solution_3():
    def get_validated_time(prompt):
        while True:
            inserted_time = input(prompt)
            try:
                parts = inserted_time.split(':')
                if len(parts) == 2:
                    hours, minutes = map(int, parts)
                    if 0 <= hours < 24 and 0 <= minutes < 60:
                        return hours, minutes
                raise ValueError
            except ValueError:
                print(f"\"{inserted_time}\" on vale ajaformaat. Palun sisesta aeg HH:MM formaadis (24h kell).")

    departure_hours, departure_minutes = get_validated_time("Sisesta väljumisaeg (formaat HH:MM) : ")
    arrival_hours, arrival_minutes = get_validated_time("Sisesta saabumisaxeg (formaat HH:MM) : ")

    departure_total_minutes = departure_hours * 60 + departure_minutes
    arrival_total_minutes = arrival_hours * 60 + arrival_minutes

    minutes_in_day = 1440
    if arrival_total_minutes >= departure_total_minutes:
        trip_duration_hours, trip_duration_minutes = divmod(arrival_total_minutes - departure_total_minutes, 60)
    else:
        trip_duration_hours, trip_duration_minutes = divmod(minutes_in_day - departure_total_minutes
                                                            + arrival_total_minutes, 60)

    print(f"Bussireisi kestvus on {trip_duration_hours:02d}:{trip_duration_minutes:02d}")


def task_solution_4():
    # Selle funktsiooniga valideerime, et kasutaja sisestab kellaaja õiges formaadis kasutades 00:00 kuni 23:59
    def get_valid_time_input(prompt):
        while True:
            try:
                time_str = input(prompt)
                datetime.strptime(time_str, '%H:%M')
                return time_str
            except ValueError:
                print("Vale ajaformaat. Palun kasuta HH:MM (24-tunni formaati).")

    # Siin salvestame sisestatud kellaaja stringina, kui see läbib validatsiooni.
    departure_time_str = get_valid_time_input("Sisesta väljumisaeg (HH:MM): ")
    arrival_time_str = get_valid_time_input("Sisesta saabimisaeg (HH:MM): ")

    # Siin me konverteerime sisestatud ajada datetime objektideks Selleks kasutame date.time mooduli strptime()
    # funktsiooni, millele anname argumentideks kellaaja stringina ja selle formaadi.
    departure_time = datetime.strptime(departure_time_str, '%H:%M')
    arrival_time = datetime.strptime(arrival_time_str, '%H:%M')

    # Kuna väljumis- ja saabumisaeg on datetime objektid (eelmine tehe),
    # siis on nüüd võimalik nendega teha ka liitmis/lahutamis tehteid. Tulemuseks saame timeDelta objekti
    travel_time = arrival_time - departure_time

    # Kuna timeDelta objektiga ei saa datetime mooduli funktsioone kasutada, siis peame manuaalselt tunnid ja minutid
    # sealt kätte saama. Vastasel juhul kuvatakse meile vastus HH:MM:SS formaadis, aga sekundid meid hetkel ei huvita
    # ja neid kuvada ei taha.
    hours, remainder = divmod(travel_time.seconds, 3600)
    minutes = remainder // 60

    print(f"Bussireisi kestvus on {hours:02d}:{minutes:02d}")
