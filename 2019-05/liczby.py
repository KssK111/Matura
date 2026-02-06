def pobierz_liczby(plik: str) -> list[int]:
    with open(plik) as f:
        return list(map(int, filter(bool, map(str.strip, f.readlines()))))
    
def czy_potega3(n: int) -> bool:
    sprawdz = 1
    while sprawdz <= n:
        if sprawdz == n:
            return True
        sprawdz *= 3
    return False

plik = "liczby.txt"
liczby = pobierz_liczby(plik)

print("4.1")
print(len(list(filter(czy_potega3, liczby))))

from math import prod
def suma_silni_cyfr_rowna(n: int) -> bool:
    cyfry = map(int, list(str(n)))
    silnie = map(lambda x: prod(range(1, x + 1)), cyfry)
    return sum(silnie) == n

print("\n4.2")
[print(x) for x in filter(suma_silni_cyfr_rowna, liczby)]

from math import gcd
from itertools import starmap
def najdluzszy_ciag_z_ciagu(ciag: list[int]) -> tuple[int, int, int]:
    nwd = ciag[0]
    dlugosc = 1
    for liczba in ciag[1:]:
        if gcd(nwd, liczba) == 1:
            break
        nwd = gcd(nwd, liczba)
        dlugosc += 1
    return (ciag[0], dlugosc, nwd)

ciagi = map(najdluzszy_ciag_z_ciagu, starmap(lambda i, _: liczby[i:], enumerate(liczby)))
print("\n4.3")
wynik = max(ciagi, key=lambda x: x[1])
print(f"Pierwsza liczba = {wynik[0]}\nDługość = {wynik[1]}\nNWD = {wynik[2]}")