def skrot(n: int):
    poz = 1
    wynik = 0
    while n > 0:
        reszta = n % 10
        n //= 10
        if reszta % 2 == 0:
            continue
        wynik += reszta * poz
        poz *= 10
    return wynik


def pobierz_liczby(plik: str) -> list[int]:
    with open(plik) as f:
        return list(map(int, filter(bool, map(str.strip, f.readlines()))))

plik = "skrot.txt"
liczby = pobierz_liczby(plik)

maks = 0
ilosc_bez = 0
for liczba in liczby:
    if not skrot(liczba):
        ilosc_bez += 1
        if maks < liczba:
            maks = liczba
with open("wyniki3_2.txt", "w", encoding="utf-8") as f:
    f.write(f"max = {maks}\nilość bez skrótu = {ilosc_bez}")

from math import gcd
plik = "skrot2.txt"
liczby = pobierz_liczby(plik)
with open("wyniki3_3.txt", "w", encoding="utf-8") as f:
    for liczba in liczby:
        if gcd(liczba, skrot(liczba)) == 7:
            print(liczba)
            f.write(f"{liczba}\n")