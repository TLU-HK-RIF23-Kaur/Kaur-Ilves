"""
Ülesanne 6 Lisa A 
Andmeteks on algselt hoiusele kantud summa, hoiustamisaastate arv ja intressimäär aasta kohta.
Arvuta ja trüki välja konto seis iga hoiustamisaasta lõpus.
Seda on mugavam teha for-tsükliga. Tulemus esita tulpadesse paigutatud tabelina, kus on
4 tulpa: aasta, seis aasta alguses, intress, seis aasta lõpus
n algselt hoiusele kantud summa, hoiustamisaastate arv ja intressimäär aasta kohta.
Tulpade loomiseks vaata näidet n2/valjund_7.py
"""

def calculate_annual_balances(initial_deposit, deposit_years, annual_interest_rate):
    balance = initial_deposit
    annual_interest_rate = annual_interest_rate / 100

    print(f"{'Aasta':<10}{'Seis aasta aguses':<20}{'Intress':<20}{'Seis aasta lõpus':<20}")
    print("-" * 70)

    for year in range(1, deposit_years + 1):
        start_balance = balance
        interest = start_balance * annual_interest_rate
        balance += interest

        print(f"{year:<10}{start_balance:<20.2f}{interest:<20.2f}{balance:<20.2f}")

    return balance

initial_deposit = 25000
deposit_years = 10
annual_interest = 7

final_balance = calculate_annual_balances(initial_deposit, deposit_years, annual_interest)
print(f"\n"f"Lõpp seis peale {deposit_years} aastat: {final_balance:.2f} eurot.")