

class WezelDrzewa:

    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewe = None
        self.prawe = None


class WezelListy:

    def __init__(self, wezel_drzewa):
        self.wezel_drzewa = wezel_drzewa
        self.nastepny = None



class Kolejka:
    def __init__(self):
        self.poczatek = None
        self.koniec = None

    def czy_pusta(self):
        return self.poczatek is None

    def dodaj_na_koniec(self, wezel_drzewa):
        nowy_element = WezelListy(wezel_drzewa)
        if self.czy_pusta():
            self.poczatek = nowy_element
            self.koniec = nowy_element
        else:
            self.koniec.nastepny = nowy_element
            self.koniec = nowy_element

    def pobierz_z_poczatku(self):
        if self.czy_pusta():
            return None
        pobrany = self.poczatek.wezel_drzewa
        self.poczatek = self.poczatek.nastepny

        if self.poczatek is None:
            self.koniec = None

        return pobrany




class Stos:
    def __init__(self):
        self.szczyt = None

    def czy_pusty(self):
        return self.szczyt is None

    def dodaj_na_szczyt(self, wezel_drzewa):
        nowy_element = WezelListy(wezel_drzewa)
        nowy_element.nastepny = self.szczyt
        self.szczyt = nowy_element

    def pobierz_ze_szczytu(self):
        if self.czy_pusty():
            return None
        pobrany = self.szczyt.wezel_drzewa
        self.szczyt = self.szczyt.nastepny
        return pobrany


# Zadanie 1

def przeszukiwanie_wszerz_bfs(korzen):
    print("Odwiedzone węzły (BFS - Wszerz): ", end="")
    if not korzen:
        return

    kolejka = Kolejka()
    kolejka.dodaj_na_koniec(korzen)

    while not kolejka.czy_pusta():
        aktualny = kolejka.pobierz_z_poczatku()
        print(aktualny.wartosc, end=" ")

        if aktualny.lewe:
            kolejka.dodaj_na_koniec(aktualny.lewe)
        if aktualny.prawe:
            kolejka.dodaj_na_koniec(aktualny.prawe)
    print()


def przeszukiwanie_w_glab_dfs_stos(korzen):
    print("Odwiedzone węzły (DFS ze Stosem): ", end="")
    if not korzen:
        return

    stos = Stos()
    stos.dodaj_na_szczyt(korzen)

    while not stos.czy_pusty():
        aktualny = stos.pobierz_ze_szczytu()
        print(aktualny.wartosc, end=" ")


        if aktualny.prawe:
            stos.dodaj_na_szczyt(aktualny.prawe)
        if aktualny.lewe:
            stos.dodaj_na_szczyt(aktualny.lewe)
    print()


#Modyfikacje DFS: Preorder, Inorder, Postorder

def dfs_preorder(wezel):
    #Kolejność: Korzeń -> Lewe -> Prawe
    if wezel:
        print(wezel.wartosc, end=" ")
        dfs_preorder(wezel.lewe)
        dfs_preorder(wezel.prawe)


def dfs_inorder(wezel):
    #Kolejność: Lewe -> Korzeń -> Prawe
    if wezel:
        dfs_inorder(wezel.lewe)
        print(wezel.wartosc, end=" ")
        dfs_inorder(wezel.prawe)


def dfs_postorder(wezel):
    #Kolejność: Lewe -> Prawe -> Korzeń
    if wezel:
        dfs_postorder(wezel.lewe)
        dfs_postorder(wezel.prawe)
        print(wezel.wartosc, end=" ")



if __name__ == "__main__":

    korzen = WezelDrzewa(1)
    korzen.lewe = WezelDrzewa(2)
    korzen.prawe = WezelDrzewa(3)

    korzen.lewe.lewe = WezelDrzewa(4)
    korzen.lewe.prawe = WezelDrzewa(5)

    korzen.prawe.lewe = WezelDrzewa(6)
    korzen.prawe.prawe = WezelDrzewa(7)

    przeszukiwanie_wszerz_bfs(korzen)
    przeszukiwanie_w_glab_dfs_stos(korzen)

    print("\nOdwiedzone węzły (DFS Preorder): ", end="")
    dfs_preorder(korzen)

    print("\nOdwiedzone węzły (DFS Inorder): ", end="")
    dfs_inorder(korzen)

    print("\nOdwiedzone węzły (DFS Postorder): ", end="")
    dfs_postorder(korzen)
    print()


    # Zadanie 2

    def znajdz_sciezke_do_liscia(wezel, cel_wartosc, sciezka):

        if not wezel:
            return False

        sciezka.append(wezel)

        if wezel.wartosc == cel_wartosc and wezel.lewe is None and wezel.prawe is None:
            return True

        if znajdz_sciezke_do_liscia(wezel.lewe, cel_wartosc, sciezka):
            return True

        if znajdz_sciezke_do_liscia(wezel.prawe, cel_wartosc, sciezka):
            return True

        sciezka.pop()
        return False


    def kopiuj_poddrzewo(wezel):
        if not wezel:
            return None
        nowy_klon = WezelDrzewa(wezel.wartosc)
        nowy_klon.lewe = kopiuj_poddrzewo(wezel.lewe)
        nowy_klon.prawe = kopiuj_poddrzewo(wezel.prawe)
        return nowy_klon


    def wypisz_drzewo_preorder(wezel):
        if wezel:
            print(wezel.wartosc, end=" ")
            wypisz_drzewo_preorder(wezel.lewe)
            wypisz_drzewo_preorder(wezel.prawe)


    def zrob_nowe_drzewo_z_liscia(stary_korzen, wartosc_liscia):
        sciezka = []
        if not znajdz_sciezke_do_liscia(stary_korzen, wartosc_liscia, sciezka):
            print(f"Nie znaleziono liścia o wartości {wartosc_liscia}!")
            return None

        stary_lisc = sciezka[-1]

        nowy_korzen = WezelDrzewa(stary_lisc.wartosc)
        aktualny_nowy_wezel = nowy_korzen

        for i in range(len(sciezka) - 2, -1, -1):
            stary_rodzic = sciezka[i]

            skad_przyszlismy = sciezka[i + 1]

            nowe_dziecko = WezelDrzewa(stary_rodzic.wartosc)

            if stary_rodzic.lewe == skad_przyszlismy:
                nowe_dziecko.prawe = kopiuj_poddrzewo(stary_rodzic.prawe)
            else:
                nowe_dziecko.lewe = kopiuj_poddrzewo(stary_rodzic.lewe)

            if aktualny_nowy_wezel.lewe is None:
                aktualny_nowy_wezel.lewe = nowe_dziecko
            else:
                aktualny_nowy_wezel.prawe = nowe_dziecko

            aktualny_nowy_wezel = nowe_dziecko

        return nowy_korzen




    if __name__ == "__main__":

        korzen = WezelDrzewa(1)
        korzen.lewe = WezelDrzewa(2)
        korzen.prawe = WezelDrzewa(3)
        korzen.lewe.lewe = WezelDrzewa(4)
        korzen.lewe.prawe = WezelDrzewa(5)

        print("Stare drzewo (Pre-order):", end=" ")
        wypisz_drzewo_preorder(korzen)
        print()

        nowe_drzewo = zrob_nowe_drzewo_z_liscia(korzen, 5)


        print("Nowe drzewo z liściem '5' na szczycie (Pre-order):", end=" ")
        wypisz_drzewo_preorder(nowe_drzewo)
        print()

"""
ODPOWIEDZI TEORETYCZNE - ZADANIE 2:

1. Czy dla każdego wierzchołka? 
NIE. W drzewie binarnym działa to dla liścia (ma 0 dzieci, więc przyjmie 1 nowego rodzica jako dziecko). Węzeł ze środka (mający już 2 dzieci) dostałby 3. dziecko, co łamie zasadę drzewa binarnego.

2. Czy mogą powstać różne drzewa?
TAK. Kształt zależy od tego, czy w kodzie starego rodzica podepniemy pod wskaźnik `.lewe` czy `.prawe` (powstaną odbicia lustrzane).

3. Dla drzew ogólnych (nie-binarnych)?
TAK I PROŚCIEJ. Zamiast wskaźników lewo/prawo węzły mają listę (np. `self.dzieci = []`). Odwrócenie to tylko usunięcie węzła z jednej listy i dopisanie (append) do innej, bez przejmowania się limitem dzieci.
"""

# Zadanie 3

def rysuj_drzewo_poziomo(wezel, odstep=0):

    if wezel:
        rysuj_drzewo_poziomo(wezel.prawe, odstep + 1)

        print("      " * odstep + f"({wezel.wartosc})")

        rysuj_drzewo_poziomo(wezel.lewe, odstep + 1)


def analizuj_strukture_drzewa(korzen):

    liczba_wezlow_na_poziomie = {}
    wszystkie_liscie = []

    def dfs_eksploruj(wezel, aktualny_poziom):
        if not wezel:
            return

        if aktualny_poziom not in liczba_wezlow_na_poziomie:
            liczba_wezlow_na_poziomie[aktualny_poziom] = 0
        liczba_wezlow_na_poziomie[aktualny_poziom] += 1

        if wezel.lewe is None and wezel.prawe is None:
            wszystkie_liscie.append((wezel.wartosc, aktualny_poziom))

        dfs_eksploruj(wezel.lewe, aktualny_poziom + 1)
        dfs_eksploruj(wezel.prawe, aktualny_poziom + 1)

    dfs_eksploruj(korzen, 1)

    return liczba_wezlow_na_poziomie, wszystkie_liscie




if __name__ == "__main__":


    korzen = WezelDrzewa(1)
    korzen.lewe = WezelDrzewa(2)
    korzen.prawe = WezelDrzewa(3)

    korzen.lewe.lewe = WezelDrzewa(4)
    korzen.lewe.prawe = WezelDrzewa(5)
    korzen.prawe.lewe = WezelDrzewa(6)

    korzen.lewe.prawe.lewe = WezelDrzewa(7)
    korzen.prawe.lewe.prawe = WezelDrzewa(8)

    print("========== WIZUALIZACJA DRZEWA ==========")
    rysuj_drzewo_poziomo(korzen)
    print("\n=========================================\n")

    poziomy, liscie = analizuj_strukture_drzewa(korzen)

    # Poziomy i Liście
    print("--- Zestawienie Węzłów ---")
    for poziom, liczba in sorted(poziomy.items()):
        print(f"Poziom {poziom}: {liczba} węzłów")

    print(f"\nCałkowita liczba liści w drzewie: {len(liscie)}")
    print(f"Wszystkie liście (wartość, poziom): {liscie}")

    # Najkrótsza ścieżka do liścia
    najkrotsza_sciezka = min(lisc[1] for lisc in liscie)
    najplytsze_liscie = [lisc[0] for lisc in liscie if lisc[1] == najkrotsza_sciezka]

    print("\n--- Najkrótsza ścieżka ---")
    print(
        f"Najkrótsza ścieżka od korzenia do liścia wynosi: {najkrotsza_sciezka - 1} krawędzi (Poziom {najkrotsza_sciezka}).")
    print(f"Liście znajdujące się na tej najpłytszej głębokości: {najplytsze_liscie}")