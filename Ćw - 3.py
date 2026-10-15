import random
import matplotlib.pyplot as plt


class Zadanie:
    def __init__(self, typ, czas, max_czekanie):
        self.typ = typ
        self.czas = czas
        self.max_czekanie = max_czekanie
        self.nastepne = None


class KolejkaZadan:
    def __init__(self):
        self.pierwsze = None

    def dodaj(self, typ, czas, max_czekanie):
        nowe = Zadanie(typ, czas, max_czekanie)
        if not self.pierwsze:
            self.pierwsze = nowe
            return
        akt = self.pierwsze
        while akt.nastepne:
            akt = akt.nastepne
        akt.nastepne = nowe

    def pobierz(self, typ):
        if not self.pierwsze: return None

        if typ == 'E':
            pobrane = self.pierwsze
            self.pierwsze = self.pierwsze.nastepne
            return pobrane

        akt = self.pierwsze
        poprz = None
        while akt:
            if akt.typ == typ:
                if poprz:
                    poprz.nastepne = akt.nastepne
                else:
                    self.pierwsze = akt.nastepne
                return akt
            poprz = akt
            akt = akt.nastepne
        return None

    def czy_pusta(self):
        return self.pierwsze is None

    def usun_niecierpliwych(self, aktualny_czas):
        zrezygnowali = 0
        akt = self.pierwsze
        poprz = None

        while akt:
            if aktualny_czas >= akt.max_czekanie:
                zrezygnowali += 1
                if poprz:
                    poprz.nastepne = akt.nastepne
                else:
                    self.pierwsze = akt.nastepne
                akt = akt.nastepne
            else:
                poprz = akt
                akt = akt.nastepne

        return zrezygnowali

    def kopiuj(self):
        nowa = KolejkaZadan()
        akt = self.pierwsze
        while akt:
            nowa.dodaj(akt.typ, akt.czas, akt.max_czekanie)
            akt = akt.nastepne
        return nowa

    def sortuj(self, malejaco=False):
        elementy = []
        akt = self.pierwsze
        while akt:
            elementy.append((akt.typ, akt.czas, akt.max_czekanie))
            akt = akt.nastepne

        elementy.sort(key=lambda x: x[1], reverse=malejaco)

        self.pierwsze = None
        for t, c, m in elementy:
            self.dodaj(t, c, m)


class Okienko:
    def __init__(self, typ):
        self.typ = typ
        self.czas = 0
        self.obsluzeni = 0



def generuj_kolejke(rozmiar, wagi=[0.33, 0.33, 0.34]):
    kolejka = KolejkaZadan()
    typy = random.choices(['A', 'B', 'C'], weights=wagi, k=rozmiar)

    for typ in typy:
        if typ == 'A':
            czas = random.randint(1, 4)
        elif typ == 'B':
            czas = random.randint(5, 8)
        else:
            czas = random.randint(9, 12)

        max_czek = random.randint(10, 40)

        kolejka.dodaj(typ, czas, max_czek)
    return kolejka


def uruchom_symulacje(typy_okienek, kolejka_wejsciowa, czy_klienci_rezygnuja=False):
    urzad = [Okienko(t) for t in typy_okienek]
    kolejka = kolejka_wejsciowa.kopiuj()
    czas_calkowity = 0
    lacznie_zrezygnowalo = 0

    while True:
        if czy_klienci_rezygnuja:
            lacznie_zrezygnowalo += kolejka.usun_niecierpliwych(czas_calkowity)

        wolne = all(o.czas == 0 for o in urzad)
        if kolejka.czy_pusta() and wolne:
            break

        for o in urzad:
            if o.czas > 0:
                o.czas -= 1

            if o.czas == 0 and not kolejka.czy_pusta():
                zad = kolejka.pobierz(o.typ)
                if zad:
                    o.czas = zad.czas
                    o.obsluzeni += 1

        czas_calkowity += 1

    return czas_calkowity, lacznie_zrezygnowalo, urzad


def uruchom_zadanie_1():
    print("========== ZADANIE 1 ==========")
    typy_okienek = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'E']
    kolejka = generuj_kolejke(40)

    czas, _, urzad_po_pracy = uruchom_symulacje(typy_okienek, kolejka)

    print(f"Całkowity czas obsługi: {czas} minut.")
    for i, o in enumerate(urzad_po_pracy, 1):
        print(f"Okienko {i} (Typ {o.typ}): obsłużono {o.obsluzeni} zadań.")
    print("\n")

    print("Usprawnienie: Zamiast utrzymywać jedną kolejkę i szukać w niej zadań ")
    print("należy stworzyć trzy niezależne listy dla A, B i C.")
    print("Wtedy okienko pobiera pierwszego klienta z właściwej listy ")
    print("Okienko E sprawdza, która z trzech list jest najdłuższa i stamtąd pobierać klienta.")
    print("\n")

def uruchom_zadanie_2():
    print("========== ZADANIE 2 ==========")
    urzad_klasyk = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
    urzad_elastyczny = ['A', 'A', 'B', 'B', 'C', 'C', 'E', 'E', 'E']
    urzad_niestandardowy = ['A', 'B', 'B', 'C', 'C', 'C', 'E']

    wagi = [0.2, 0.3, 0.5]

    kolejka_50 = generuj_kolejke(50, wagi)
    czas_k, zrez_k, _ = uruchom_symulacje(urzad_klasyk, kolejka_50, czy_klienci_rezygnuja=True)
    czas_e, zrez_e, _ = uruchom_symulacje(urzad_elastyczny, kolejka_50, czy_klienci_rezygnuja=True)
    czas_n, zrez_n, _ = uruchom_symulacje(urzad_niestandardowy, kolejka_50, czy_klienci_rezygnuja=True)

    print("--- POJEDYNCZA KOLEJKA (Test Rezygnacji) ---")
    print(f"Klasyk:         Czas = {czas_k}, Zrezygnowało = {zrez_k}")
    print(f"Elastyczny:     Czas = {czas_e}, Zrezygnowało = {zrez_e}")
    print(f"Niestandardowy: Czas = {czas_n}, Zrezygnowało = {zrez_n}")

    kolejka_rosnaco = kolejka_50.kopiuj()
    kolejka_rosnaco.sortuj(malejaco=False)

    kolejka_malejaco = kolejka_50.kopiuj()
    kolejka_malejaco.sortuj(malejaco=True)

    czas_rosnaco, _, _ = uruchom_symulacje(urzad_elastyczny, kolejka_rosnaco)
    czas_malejaco, _, _ = uruchom_symulacje(urzad_elastyczny, kolejka_malejaco)

    print("\n--- TEST SORTOWANIA (Urząd Elastyczny) ---")
    print(f"Losowo wpadający klienci: {czas_e} minut")
    print(f"Najkrótsze sprawy z przodu: {czas_rosnaco} minut")
    print(f"Najdłuższe sprawy z przodu: {czas_malejaco} minut")

    print("\n--- TEST MASOWY (100 KOLEJEK) ---")
    wyniki_k, wyniki_e, wyniki_n = [], [], []

    for _ in range(100):
        k = generuj_kolejke(50, wagi)

        c_k, _, _ = uruchom_symulacje(urzad_klasyk, k)
        c_e, _, _ = uruchom_symulacje(urzad_elastyczny, k)
        c_n, _, _ = uruchom_symulacje(urzad_niestandardowy, k)

        wyniki_k.append(c_k)
        wyniki_e.append(c_e)
        wyniki_n.append(c_n)

    print(f"Średni czas (Klasyk): {sum(wyniki_k) / 100:.2f}")
    print(f"Średni czas (Elastyczny): {sum(wyniki_e) / 100:.2f}")
    print(f"Średni czas (Niestandardowy): {sum(wyniki_n) / 100:.2f}")


    plt.hist(wyniki_k, alpha=0.5, label='Klasyk (9)')
    plt.hist(wyniki_e, alpha=0.5, label='Elastyczny (9, 3xE)')
    plt.hist(wyniki_n, alpha=0.5, label='Niestandardowy (7, 1xE)')

    plt.title('Rozkład czasów obsługi 100 kolejek')
    plt.xlabel('Czas obsługi (minuty)')
    plt.ylabel('Częstotliwość wystąpienia')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    uruchom_zadanie_1()
    uruchom_zadanie_2()