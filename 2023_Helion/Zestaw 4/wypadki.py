with open("wypadki.txt") as f:
    wypadki: list[tuple[str, str, int]] = list(map(lambda l: (l[0], l[1], int(l[2])), map(str.split, filter(bool, map(str.strip, f.readlines())))))

from collections import defaultdict
ilosc_danych_wojewodztw = defaultdict(int)
for woj in map(lambda w: w[0][0], wypadki):
    ilosc_danych_wojewodztw[woj] += 1
min_info = min(ilosc_danych_wojewodztw.keys(), key=lambda x: ilosc_danych_wojewodztw[x])
print(f"3.1\nNajmniej informacji ma województwo: {min_info}")

wypadki_2: list[tuple[str, str, int]] = list(map(lambda w: (w[0][0], w[0], w[2]), wypadki))
woj_pow_licznik = defaultdict(lambda: defaultdict(int))
for w, p, i in wypadki_2:
    woj_pow_licznik[w][p] += i

print("\n3.2")
for w in woj_pow_licznik.keys():
    print(w + ":", end="")
    powiaty = woj_pow_licznik[w]
    max_wypadki = max(powiaty.values())
    for p in powiaty:
        if powiaty[p] == max_wypadki:
            print(" " + p, end="")
    print()


print("\n3.3")
from math import ceil
def przetworz_miesiac_dzien(md: tuple[int, int]):
    m, d = md
    x = ceil(d / 10)
    x = 3 if x == 4 else x
    return x + (3 if m == 8 else 0)
wypadki_pow_okres = list(map(lambda w: (w[0], przetworz_miesiac_dzien(tuple(int(x) for x in w[1][-4:].split("-")))), wypadki)) # pyright: ignore[reportArgumentType]
stworz_pomiar_okresow = lambda: dict((map(lambda o: (o, 0), range(1, 6 + 1))))
powiaty_okresy_ilosc = defaultdict(stworz_pomiar_okresow)
for powiat, okres in wypadki_pow_okres:
    powiaty_okresy_ilosc[powiat][okres] += 1

for powiat in powiaty_okresy_ilosc.keys():
    if all(map(lambda x: x >= 7, powiaty_okresy_ilosc[powiat].values())):
        print(powiat)