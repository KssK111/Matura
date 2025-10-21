from itertools import starmap, repeat
plik = "anomalie.txt"

print("6.1")
def czy_posortowana(lista: list[int]) -> bool:
    return lista == sorted(lista)
with open(plik) as file:
    linie = map(str.split, filter(bool, map(str.strip, file.readlines())))
nowe_linie = []
for linia in linie:
    nowe_linie.append(list(map(int, linia)))
print(f"Niemalejące ciągi = {len(list(filter(czy_posortowana, nowe_linie)))}")

print("\n6.2")
with open(plik) as file:
    wiersze = list(map(lambda x: list(map(int, x)), map(str.split, filter(bool, map(str.strip, file.readlines())))))

wynik_bin = ""
suma_roznic = 0
ilosc_roznic = 0
roznica = lambda x, y: x - y
for wiersz in wiersze:
    suma_roznic += sum(starmap(roznica, zip(wiersz[:-1], wiersz[1:])))
    ilosc_roznic += len(wiersz) - 1
srednia = suma_roznic / ilosc_roznic
for wiersz in wiersze:
    wynik_bin += str(int(all(map(lambda x: x > srednia, starmap(roznica, zip(wiersz[:-1], wiersz[1:]))))))

wynik_bin = int(wynik_bin)
#print(wynik_bin)
wynik_bin &= int("".join(repeat("1", 30)), 2)

print(f"Bin = {bin(wynik_bin)[2:]}\nDec = {wynik_bin}")
