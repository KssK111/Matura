from collections import defaultdict

plik = "dane.txt"
with open(plik) as f:
    slowa = [s.strip() for s in f]

slowa_ilosc = defaultdict(int)
for slowo in slowa:
    slowa_ilosc[slowo] += 1

print("a)")
ile_slow = len(list(filter(lambda s_i: s_i[1] > 1, slowa_ilosc.items())))
print(ile_slow)
najwiecej_wystapien = max(slowa_ilosc.keys(), key=lambda s: slowa_ilosc[s])
print(najwiecej_wystapien)
liczba_wystapien = slowa_ilosc[najwiecej_wystapien]
print(liczba_wystapien)

print("b)")
hex_na_dec = lambda h: int(h, 16)
parzysta = lambda x: x % 2 == 0
ile_parzystych = len(list(filter(parzysta, map(hex_na_dec, slowa))))

print(ile_parzystych)
print("c)")
palindrom = lambda s: s == "".join(reversed(s))
ile_palindromow = len(list(filter(palindrom, slowa)))
print(ile_palindromow)