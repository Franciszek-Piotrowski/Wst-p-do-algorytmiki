#zadanie 1
import numpy as np
n = 5 #liczba przedmiotów
m = 10 #liczba studentów

możliwe_oceny = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

macierz_ocen = np.random.choice(możliwe_oceny, size=(m, n))
print(macierz_ocen)
liczba_studentów_uwalających_kierunek = 0
for wiersz in macierz_ocen:
    liczba_uwaleń = 0
    for ocena in wiersz:
        if ocena == 2.0:
            liczba_uwaleń += 1
    if liczba_uwaleń >= 2:
        liczba_studentów_uwalających_kierunek += 1
print(f"Liczba studentów którzy uwalili co najmniej 2 przedmioty to: {liczba_studentów_uwalających_kierunek}")
średnie = np.mean(macierz_ocen, axis = 1)
indeks_maks = np.argmax(średnie)
indeks_min = np.argmin(średnie)

oceny_maks = macierz_ocen[indeks_maks]
oceny_min = macierz_ocen[indeks_min]
print(f"Najlepsze oceny to: {oceny_maks} i najgorsze oceny to: {oceny_min}")
i = 0
for średnia in średnie:

    if średnia >= 4.5:
        print(f"Student nr {i+1} ma średnią: {średnie[i]}")
    i += 1
najlepsza_ocena = np.max(macierz_ocen)
maska = (najlepsza_ocena == macierz_ocen)
liczba_wystąpień = np.sum(maska,axis=1)
indeks_studenta = np.argmax(liczba_wystąpień)
print(f"Najlepszy student to: {indeks_studenta} z największą ilością ocen {najlepsza_ocena}")


bins = [1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75]
for j in range(n):
    pasek_ocen = macierz_ocen[:,j]
    counts, edges = np.histogram(pasek_ocen, bins=bins)
    print(f"\nPrzedmiot nr {j + 1}:")
    for i in range(len(możliwe_oceny)):
        if counts[i] > 0:
            print(f"  Ocena {możliwe_oceny[i]}: {counts[i]} szt.")
#zadanie 2

n1 = 3
m1 = 3
tab1 = [1,2,3,4,5,6,7,8,9]

macierz1 = np.random.choice(tab1, size=(m1, n1))
macierz2 = np.random.choice(tab1, size=(m1, n1))

macierz_wynikowa = np.sum(np.abs(macierz1 - macierz2))
print(f"wynik działania macierzy to: {macierz_wynikowa}")

#zadanie 3

n2 = 3
m2 = 4
tab2 = [0,1,2,3,4,5,6,7,8,9]
macierz_schodkowa = np.random.choice(tab2, size=(n2, m2)).astype(float)

for i in range(n2):
    if macierz_schodkowa[i,i] == 0:
        for k in range(i+1 , n2):
            if macierz_schodkowa[k,i] != 0:
                macierz_schodkowa[[i,k]] = macierz_schodkowa[[k,i]]
                break
    if macierz_schodkowa[i,i] !=  0:
        macierz_schodkowa[i] = macierz_schodkowa[i]/macierz_schodkowa[i,i]

    for j in range (i+1, n2):
        f = macierz_schodkowa[j,i]
        macierz_schodkowa[j]= macierz_schodkowa[j] - (f * macierz_schodkowa[i])
    for j in range (i -1 , -1, -1):
        f = macierz_schodkowa[j,i]
        macierz_schodkowa[j] = macierz_schodkowa[j] - (f * macierz_schodkowa[i])
print(macierz_schodkowa)

#zadanie 4

towary = np.array([
    [101, 5.00, 1],
    [102, 3.50, 0],
    [103, 12.0, 1]
]).astype(float)

paragony = np.array([
    [1, 101, 2.0],
    [1, 102, 1.5],
    [2, 101, 1.2],
    [2, 999, 1.0]
]).astype(float)
lista_towarów = towary[:,0]
lista_wartości = towary[:,1]
lista_rodzaju = towary[:,2]
lista_klientów = {}
for idx, wiersz in enumerate(paragony):
    id_klienta = int(wiersz[0])
    id_towaru = wiersz[1]
    ilosc_towaru = wiersz[2]
    if id_towaru not in lista_towarów:
        print("Nie ma takiego towaru")
        continue
    indeks_towaru = np.where(lista_towarów == id_towaru)[0][0]
    if ilosc_towaru % 1 != 0 and lista_rodzaju[indeks_towaru] == 1:
        print("Zła ilość towaru")
        continue
    kwota = float(lista_wartości[indeks_towaru] *ilosc_towaru)
    if id_klienta in lista_klientów:
        lista_klientów[id_klienta] = lista_klientów[id_klienta] + kwota
    else:
        lista_klientów[id_klienta] = kwota

print(lista_klientów)