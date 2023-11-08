"""
Ülesanne 6 Lisa A 
Sisestad lisaks summa, mille tahad hoiusele koguda. Programm peab simuleerima 
hoiuse muutumist ja teatama, mitu aastat ja mitu kuud kulub eesmärgi saavutamiseks.
"""

def calculate_time_to_reach_goal(initial_deposit, monthly_deposit, annual_interest_rate, savings_goal):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_amount = initial_deposit
    months = 0

    while total_amount < savings_goal:
        total_amount += monthly_deposit
        total_amount += total_amount * monthly_interest_rate
        months += 1
        print(f"Peale {months}. kuud on hoiuse summa: {total_amount:.2f} euros")

    years, remaining_months = divmod(months, 12)

    return years, remaining_months, total_amount

initial_deposit = int(input("Sisesta summa millega soovite kogumist alustada: "))
monthly_deposit = int(input("Sisesta summa mida soovite iga kuu hoiusele lisada: "))
annual_interest = 10
savings_goal = int(input("Sisestage oma säästu eesmärk (summa): "))

years, months, total_savings = calculate_time_to_reach_goal(initial_deposit, monthly_deposit, annual_interest,
                                                            savings_goal)
print(f" {savings_goal:.2f} euro kogumine võtab aega {years} aastat ja {months} kuud")
