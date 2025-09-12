import math

def kolumnowy_szyfr(tekst, klucz):
    # Usuwamy spacje i zamieniamy na wielkie litery
    tekst = tekst.replace(" ", "").upper()
    klucz = klucz.upper()

    # Długość klucza i wiadomości
    n_kolumn = len(klucz)
    n_wierszy = math.ceil(len(tekst) / n_kolumn)

    # Uzupełniamy tekst pustymi znakami do pełnej siatki
    pelna_dlugosc = n_wierszy * n_kolumn
    tekst += "_" * (pelna_dlugosc - len(tekst))  # "_" jako znak pusty

    # Tworzymy macierz wierszy
    siatka = [list(tekst[i:i+n_kolumn]) for i in range(0, pelna_dlugosc, n_kolumn)]

    # Tworzymy listę z indeksami kolumn według alfabetycznej kolejności klucza
    indeksy = sorted(range(len(klucz)), key=lambda i: klucz[i])

    # Budujemy szyfrogram, czytając kolumny w odpowiedniej kolejności
    szyfrogram = ""
    for i in indeksy:
        for wiersz in siatka:
            szyfrogram += wiersz[i]

    return szyfrogram

# Przykład użycia
tekst_jawny = "TAJNEHASLO"
klucz = "KOT"

szyfrogram = kolumnowy_szyfr(tekst_jawny, klucz)
print("Szyfrogram:", szyfrogram)
