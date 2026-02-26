def pobierz_pole(plik: str) -> list[list[int]]:
    with open(plik) as f:
        return list(map(lambda x: list(map(int, x)), map(str.split, map(str.strip, f.readlines()))))

pole_waclawa = pobierz_pole("pole_waclawa.txt")

def srednia_pola(pole: list[list[int]]) -> float:
    suma = sum(map(sum, pole))
    ilosc = sum(map(len, pole))
    return  suma / ilosc

def podziel_liste[T](lista: list[T], czesci: int) -> list[list[T]]:
    ilosc = len(lista) // czesci
    return [lista[i* ilosc - ilosc:i * ilosc] for i in range(1, czesci + 1)]

def podziel_pole(ilosc_czesci: int, pole: list[list[int]]) -> list[list[list[list[int]]]]:
    pole_podzielone_wiersze = [podziel_liste(w, ilosc_czesci) for w in pole]
    return podziel_liste(pole_podzielone_wiersze, ilosc_czesci)

from itertools import chain
from typing import Iterator
def raport(pole: list[list[int]]) -> Iterator[str]:
    i = 0
    wzor_r = lambda ile_sek, min_avg, min_sek: f"Liczba sektorów = {ile_sek} Najmniejsza średnia = {min_avg} w kwadracie {min_sek}/{ile_sek}"
    while len(pole) // (ilosc_czesci := 2**i) >= 2:
        podzielone_wiersze = list(chain.from_iterable(podziel_pole(ilosc_czesci, pole)))
        wysokosc_sektora = szerokosc_sektora = len(podzielone_wiersze[0][0])
        ile_wierszy = len(pole) // wysokosc_sektora
        ile_s_w_wierszu = len(pole[0]) // szerokosc_sektora
        sektory = []
        for w in range(ile_wierszy):
            start = wysokosc_sektora * w
            koniec = wysokosc_sektora * (w + 1)
            for s in range(ile_s_w_wierszu):
                sektory.append([wiersz[s] for wiersz in podzielone_wiersze[start:koniec]])
        srednie_sektorow = [srednia_pola(sek) for sek in sektory]
        # [print(sr, se) for sr, se in zip(srednie_sektorow, sektory)]
        yield wzor_r(len(sektory), min_sr := min(srednie_sektorow), srednie_sektorow.index(min_sr) + 1)
        i += 1

for r in raport(pole_waclawa):
    print(r)

[print(w[0:8]) for w in pole_waclawa[0:8]]