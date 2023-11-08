"""Ülesanne 1. Õnneseitse Kui suur on lootus võita mõnes õnnemängus? Selleks võib välja arvutada tõenäosuseid,
aga võib ka mängu käiku simuleerida.

Mängija veeretab kahte täringut. Kui täringute silmade summa on 7, mängija võidab (näiteks 4 eurot). Kui ei ole,
siis kaotab (näiteks 1 euro). Mängu alguses paneb mängija mängu näiteks 50 eurot. Seejärel hakkab veeretama ja
programm suurendab või vähendab raha. Mäng lõppeb siis, kui raha on otsas (või kui ollakse mingi arvu eurodega
plussis). Veeretada aitab juhuslike arvude generaator. Lisaks on vaja programmi lõpus teatada, kui palju kordi jõuti
täringuid veeretada. Lisaks võiks lõpus teatada vahepealse kõige suurema summa.
"""
import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game(starting_bet, win_amount, loss_amount, target_amount=None):
    money = starting_bet
    number_of_rolls = 0
    highest_amount = money

    while money > 0:
        dice1, dice2 = roll_dice()
        number_of_rolls += 1
        sum_of_dice = dice1 + dice2

        if sum_of_dice == 7:
            money += win_amount
        else:
            money -= loss_amount

        highest_amount = max(highest_amount, money)

        if target_amount and money >= target_amount:
            break

    return money, number_of_rolls, highest_amount


starting_bet = 50
win_amount = 4
loss_amount = 1
target_amount = 100


final_money, rolls, highest_money = play_game(starting_bet, win_amount, loss_amount, target_amount)

print(f"Mäng läbi! Veeretasid täringuid {rolls} korda.")
print(f"Mängu kestel oli suurim kogutud summa  {highest_money} eurot.")
if final_money <= 0:
    print("Raha sai otsa.")
else:
    print(f"Võitsite {final_money} eurot.")