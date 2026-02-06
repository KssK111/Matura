def pobierz_liczby(plik: str) -> list[int]:
    with open(plik) as f:
        return list(map(int, filter(bool, map(str.strip, f.readlines()))))

plik = "liczby.txt"
liczby = pobierz_liczby(plik)

from math import isqrt, sqrt
print("3.1")
kwadraty = list(filter(lambda x: float(isqrt(x)) == sqrt(x), liczby))
print(f"Ilość = {len(kwadraty)}\nPierwsza = {kwadraty[0]}")

print("\n3.2")
def czy_pierwsza(n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True
def nastepny_pierwszy_dzielnik(n: int):
    for i in range(2, n + 1):
        if czy_pierwsza(i):
            if n % i == 0:
                yield i
[print(x) for x in filter(lambda l: len(list(nastepny_pierwszy_dzielnik(l))) >= 5, liczby)]

print("\n3.3")
licznik_w, licznik_m, licznik_r = 0, 0, 0
for liczba in liczby:
    liczba_max = int("".join(sorted(list(str(liczba)), reverse=True)))
    liczba_min = int("".join(sorted(list(str(liczba)))))
    roznica = liczba_max - liczba_min
    if roznica > liczba:
        licznik_w += 1
    elif roznica < liczba:
        licznik_m += 1
    else:
        licznik_r += 1
        print(liczba)
print(f"Większa - {licznik_w}\nMniejsza - {licznik_m}\nRówna - {licznik_r}")









