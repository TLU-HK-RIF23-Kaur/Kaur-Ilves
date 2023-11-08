"""
Ülesanne 2. Arvu arvamise mäng Üks mängija mõtleb arvu etteantud piirides ja teine püüab seda ära arvata. Meie
ülesandes - arvuti mõtleb arvu ja inimene hakkab arvama. Arvuti vastab ning täpsustab, kas pakutud arv on liiga suur
või liiga väike.

Millal mäng lõpetada? a) arv arvatakse ära b) kui liiga palju arvatakse (näiteks üle 7 korra), siis programm teatab,
et nii rumal ikka olla ei saa, et niiiii kaua seda ühte õnnetut arvu arvata.

Mitme pakkumisega peaks arv vahemikust 1 .. 100 arvatud saama? Aga 1 .. 1000? Kas saaksime seda kuidagi välja arvutada?

Kui see tehtud, tuleb terve mäng korduma panna - Kas soovid veel mängida? NB! See tähendab uue tsükli lisamist
mängimisetsükli ümber. Ära püüa mängimisetsüklit kõike tegema panna. See on võimalik, kuid mitte mõistlik.
"""
import math
import random




def play_game():
    # Mängija sisestab numbri vahemiku ülempiiri ja arvutab maksimaalse arvu pakkumisi.
    range_limit = int(input("Sisesta maksimaalne number: "))
    max_guesses = math.ceil(math.log2(range_limit))

    while True:
        number_to_guess = random.randint(1, range_limit)
        print(f"Arva number vahemikus 1 kuni {range_limit}:")


        for guess_count in range(1, max_guesses + 1):
            user_guess = int(input(f"{guess_count}. katse - sisesta oma pakkumine: "))

            if user_guess < number_to_guess:
                print("Liiga madal!")
            elif user_guess > number_to_guess:
                print("Liiga kõrge!")
            else:
                print(f"Õige! Arvasid numbri ära {guess_count}. katsel.")
                break

            if guess_count == max_guesses:  # Viimane katse.
                print(f"Oled kasutanud kõik {max_guesses} katset. Õige number oli {number_to_guess}.")
                break

        continue_playing = input("Kas soovid uuesti mängida? (jah/ei): ").lower()
        if continue_playing != "jah":
            print("Aitäh mängimast!")
            break


play_game()


