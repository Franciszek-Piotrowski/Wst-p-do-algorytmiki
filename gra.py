
#gra zgadnij liczbe
import random
import os
def gra(wylosowana_liczba):
    os.system("cls")
    próby = 0
    for i in range (100):
        zgadywanie = int(input(f"Zgadnij liczbę: "))
        if zgadywanie == wylosowana_liczba:
            próby += 1
            os.system("cls")
            print("Zgadłeś!!")
            print(f"Wylosowana liczba to: {wylosowana_liczba}")
            print(f"Ilość prób to: {próby}")
            break
        else:
            os.system("cls")
            print("Nie udało ci się")
            if zgadywanie > wylosowana_liczba:
                print(f"Mniej niż {zgadywanie}")
            if zgadywanie < wylosowana_liczba:
                print(f"Więcej niż {zgadywanie}")
            print("Spróbuj ponownie")
            próby += 1

gra(random.randint(1,100))


def zgaduj_binarnie (wylosowana_liczba):
    low = 1
    high = 100
    czy_zgadlismy = True
    próby_zgadnięcia = 0
    while czy_zgadlismy:
        próby_zgadnięcia += 1
        zgadujemy = (low + high) // 2
        if wylosowana_liczba == zgadujemy:
            czy_zgadlismy = False
            print(f"Zgadlismy liczbę: {wylosowana_liczba} w {próby_zgadnięcia} prób")
        elif wylosowana_liczba > zgadujemy:
            low = zgadujemy + 1
        elif wylosowana_liczba < zgadujemy:
            high = zgadujemy - 1
zgaduj_binarnie(random.randint(1,100))
