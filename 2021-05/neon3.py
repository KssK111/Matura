from collections import defaultdict

plik = "instrukcje.txt"
with open(plik) as file:
    linie = filter(bool, map(str.strip, file.readlines()))

wynik = defaultdict(int)
for instrukcja, litera in map(str.split, linie):
    if instrukcja == "DOPISZ": wynik[litera] += 1

x = max(wynik, key=lambda x: wynik[x])
litera, ilosc = x, wynik[x]
print(f"{litera} - {ilosc}")