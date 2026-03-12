from collections import defaultdict
from math import isqrt

with open("NAPIS.TXT") as f:
    napisy = [l.strip() for l in f]

def czy_pierwszy(napis: str) -> bool:
    liczba = sum(map(ord, napis))
    if liczba < 2:
        return False
    for d in range(2, isqrt(liczba) + 1):
        if liczba % d == 0:
            return False
    return True

def czy_rosnacy(napis: str) -> bool:
    liczby = [ord(l) for l in napis]
    maks = 0
    for l in liczby:
        if l <= maks:
            return False
        maks = l
    return True

print(f"Ilość napisów pierwszych = {len(list(filter(czy_pierwszy, napisy)))}")
print("Napisy rosnące:")
[print(n) for n in napisy if czy_rosnacy(n)]

napisy_ilosc = defaultdict(int)
for n in napisy:
    napisy_ilosc[n] += 1

print("Napisy występujące > 1 raz")
for n, i in napisy_ilosc.items():
    if i > 1:
        print(n)