import random
import time

n = 10
losowa_lista = [random.randint(1, 100) for _ in range(n)]
def sortowanie_babelkowe(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
print(sortowanie_babelkowe(list(losowa_lista)))

def sortowanie_wstawienie(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista
print(sortowanie_wstawienie(list(losowa_lista)))


def sortowanie_wybór(lista):
    n = len(lista)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
print(sortowanie_wybór(list(losowa_lista)))

def sortowanie_bąbelkowe_zmiana(lista):
    n = len(lista)
    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swap = True
        if not swap:
            break
    return lista
print(sortowanie_bąbelkowe_zmiana(list(losowa_lista)))


def sortowanie_bąbelkowe_zmniejszanie(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
print(sortowanie_bąbelkowe_zmniejszanie(list(losowa_lista)))

def python_sort(lista):
    return sorted(lista)
print(python_sort(list(losowa_lista)))

rozmiary = [10, 20, 50, 100, 200, 500, 1000]
czasy_python = []
czasy_babelkowe = []
czasy_wstawianie = []
czasy_wybor = []
czasy_babelkowe_zmiana = []
czasy_babelkowe_zmniejszanie = []

max_czasy_python = []
max_czasy_babelkowe = []
max_czasy_wstawianie = []
max_czasy_wybor = []
max_czasy_babelkowe_zmiana = []
max_czasy_babelkowe_zmniejszanie = []
for n in rozmiary:
    pomiary_python = []
    pomiary_babelkowe = []
    pomiary_wstawianie = []
    pomiary_wybor = []
    pomiary_babelkowe_zmiana = []
    pomiary_babelkowe_zmniejszanie = []

    for x in range(10):
        losowa_lista = [random.randint(1, 100) for x in range(n)]

        # 1. Python sort
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        python_sort(kopia)
        pomiary_python.append(time.perf_counter() - start)

        # 2. Sortowanie bąbelkowe
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        sortowanie_babelkowe(kopia)
        pomiary_babelkowe.append(time.perf_counter() - start)

        # 3. Sortowanie przez wstawianie
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        sortowanie_wstawienie(kopia)
        pomiary_wstawianie.append(time.perf_counter() - start)

        # 4. Sortowanie przez wybór
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        sortowanie_wybór(kopia)
        pomiary_wybor.append(time.perf_counter() - start)

        # 5. Bąbelkowe zmiana
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        sortowanie_bąbelkowe_zmiana(kopia)
        pomiary_babelkowe_zmiana.append(time.perf_counter() - start)

        # 6. Bąbelkowe naiwne
        kopia = losowa_lista.copy()
        start = time.perf_counter()
        sortowanie_bąbelkowe_zmniejszanie(kopia)
        pomiary_babelkowe_zmniejszanie.append(time.perf_counter() - start)

    czasy_python.append(sum(pomiary_python) / 10)
    czasy_babelkowe.append(sum(pomiary_babelkowe) / 10)
    czasy_wstawianie.append(sum(pomiary_wstawianie) / 10)
    czasy_wybor.append(sum(pomiary_wybor) / 10)
    czasy_babelkowe_zmiana.append(sum(pomiary_babelkowe_zmiana) / 10)
    czasy_babelkowe_zmniejszanie.append(sum(pomiary_babelkowe_zmniejszanie) / 10)

    max_czasy_python.append(max(pomiary_python))
    max_czasy_babelkowe.append(max(pomiary_babelkowe))
    max_czasy_wstawianie.append(max(pomiary_wstawianie))
    max_czasy_wybor.append(max(pomiary_wybor))
    max_czasy_babelkowe_zmiana.append(max(pomiary_babelkowe_zmiana))
    max_czasy_babelkowe_zmniejszanie.append(max(pomiary_babelkowe_zmniejszanie))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(rozmiary, czasy_python, label='Python sort()', marker='o')
plt.plot(rozmiary, czasy_babelkowe, label='Bąbelkowe (podstawowe)', marker='o')
plt.plot(rozmiary, czasy_wstawianie, label='Wstawianie', marker='o')
plt.plot(rozmiary, czasy_wybor, label='Wybór', marker='o')
plt.plot(rozmiary, czasy_babelkowe_zmiana, label='Bąbelkowe (przerwanie)', marker='o')
plt.plot(rozmiary, czasy_babelkowe_zmniejszanie, label='Bąbelkowe (zmniejszanie)', marker='o')

plt.title('Średni czas sortowania (Wszystkie algorytmy)')
plt.xlabel('Liczba elementów (n)')
plt.ylabel('Czas [sekundy]')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(rozmiary, max_czasy_python, label='Python sort()', marker='o')
plt.plot(rozmiary, max_czasy_babelkowe, label='Bąbelkowe (podstawowe)', marker='o')
plt.plot(rozmiary, max_czasy_wstawianie, label='Wstawianie', marker='o')
plt.plot(rozmiary, max_czasy_wybor, label='Wybór', marker='o')
plt.plot(rozmiary, max_czasy_babelkowe_zmiana, label='Bąbelkowe (przerwanie)', marker='o')
plt.plot(rozmiary, max_czasy_babelkowe_zmniejszanie, label='Bąbelkowe (zmniejszanie)', marker='o')

plt.title('Maksymalny czas sortowania (z 10 prób)')
plt.xlabel('Liczba elementów (n)')
plt.ylabel('Czas [sekundy]')
plt.legend()
plt.grid(True)
plt.show()




def wizualizuj(lista, i, j):

    for index, wartosc in enumerate(lista):
        pasek = "#" * wartosc
        print(f"{pasek}")
    time.sleep(0.15)
def sortowanie_visual(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            wizualizuj(lista, i, j)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


dane = [random.randint(1, 20) for _ in range(15)]
sortowanie_visual(dane)




def wizualizuj_wstawianie(lista, aktualny_idx, sprawdzany_idx):

    for idx, val in enumerate(lista):
        pasek = "#" * val
        print(f"{pasek}")
    time.sleep(0.15)

def sort_wstawianie_visual(lista):
    n = len(lista)
    for i in range(1, n):
        klucz = lista[i]
        j = i - 1
        wizualizuj_wstawianie(lista, i, j)

        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
            wizualizuj_wstawianie(lista, j + 1, j)

        lista[j + 1] = klucz
        wizualizuj_wstawianie(lista, j + 1, -1)


dane = [random.randint(1, 20) for _ in range(12)]
sort_wstawianie_visual(dane)


def wizualizuj_wybor(lista, start_idx, szukany_idx, min_idx):

    for idx, val in enumerate(lista):
        pasek = "#" * val
        print(f"{pasek}")
    time.sleep(0.15)

def sort_wybor_visual(lista):
    n = len(lista)
    for i in range(n - 1):
        m_idx = i
        for j in range(i + 1, n):
            wizualizuj_wybor(lista, i, j, m_idx)
            if lista[j] < lista[m_idx]:
                m_idx = j

        lista[i], lista[m_idx] = lista[m_idx], lista[i]
        wizualizuj_wybor(lista, i, -1, i)


dane = [random.randint(1, 20) for _ in range(12)]
sort_wybor_visual(dane)