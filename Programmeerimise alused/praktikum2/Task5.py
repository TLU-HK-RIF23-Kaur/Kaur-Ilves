"""
Ülesanne 5. Bolt Drive Siin lehel on info Bolt Drive'i rendihinna arvutamise kohta: 
https://bolt.eu/et-ee/blog/bolt-drive-kogu-info-rendihindadest/ Küsi kasutajalt vajalikud andmed (minutihind, 
maks tunnihind, maks päeva hind ja kilomeetrihind, läbitud km arv ja kulunud aeg - tundi ja minutit)) Leia sõidu 
maksumus. Testida saad selle rakenduse abil:  https://aanndryyyy.github.io/bolt-calculator/
"""

""" Lahendus  IF lausega"""
def task_solution_1():
    minute_rate = float(input("Sisesta minuti hind:"))
    hour_rate = float(input("Sisesta tunni hind:"))
    day_rate = float(input("Sisesta päeva hind:"))
    km_rate = float(input("Sisesta km hind:"))
    duration = input("Sisesta rendi aeg formaadis hh:mm: ")
    distance = int(input("Enter traveled distance in km: "))

    duration_in_minutes = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
    days = duration_in_minutes // (24 * 60)
    remaining_minutes = duration_in_minutes % (24 * 60)
    hours = remaining_minutes // 60
    remaining_minutes = remaining_minutes % 60

    if remaining_minutes * minute_rate + hours * hour_rate >= day_rate:
        days += 1
        hours = 0
        remaining_minutes = 0
    if remaining_minutes * minute_rate >= hour_rate:
        hours += 1
        remaining_minutes = 0

    total_cost = days * day_rate + hours * hour_rate + remaining_minutes * minute_rate + distance * km_rate
    print(f"Rendi kogumaksus on: {total_cost}")



""" Lahendus ilma  IF lauseta"""
def task_solution_2():
    minute_rate = float(input("Sisesta minuti hind:"))
    hour_rate = float(input("Sisesta tunni hind:"))
    day_rate = float(input("Sisesta päeva hind:"))
    km_rate = float(input("Sisesta km hind:"))
    duration = input("Sisesta rendi aeg formaadis hh:mm: ")
    distance = int(input("Enter total distance in km: "))

    duration_in_minutes = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
    days, remaining_minutes = divmod(duration_in_minutes, 24 * 60)

    full_hours, remaining_minutes = divmod(remaining_minutes, 60, )

    hours_cost = full_hours * hour_rate
    minutes_cost = remaining_minutes * minute_rate

    total_cost = days * day_rate + min(hours_cost + min(minutes_cost, hour_rate), day_rate) + distance * km_rate
    print(f"Rendi kogumaksus on: {total_cost}")

task_solution_1()
task_solution_2()