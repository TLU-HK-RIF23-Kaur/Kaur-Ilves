"""
Ülesanne 6 Hea pank (ehk "unistada ju võib")
Avad pangas kogumishoiuse ja paned hoiusele mingi arvu eurot. Igal palgapäeval (üks kord
kuu alguses) lisad hoiusele teatud arvu eurosid (igas kuus võrdselt). Pank lisab
intressiga teenitud eurod kuu lõpus. Teada on intressimäär aastas. Sellest saame protsendi
1 kuu kohta, jagades ta 12-ga (intress/12). (Tegelikkuses on see veidi keerulisem.)
"""

def calculate_savings(deposit, monthly_addition, annual_interest_rate, months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_amount = deposit

    for month in range(1, months + 1):
        total_amount += monthly_addition
        total_amount += total_amount * monthly_interest_rate

        print(f"Peale {month}. kuud on hoiuse summa: {total_amount:.2f} euros")

    return total_amount


initial_deposit = int(input("Sisesta summa millega soovite kogumist alustada: "))
monthly_deposit = int(input("Sisesta summa mida soovite iga kuu hoiusele lisada: "))
annual_interest = 9
total_months = 300

total_savings = calculate_savings(initial_deposit, monthly_deposit, annual_interest, total_months)
print(f"Säästude kogu summa peale {total_months} kuud: {total_savings:.2f} eurot")
