def czy_posortowana(lista: list[int]) -> bool:
    return lista == sorted(lista)

plik = "anomalie.txt"

print("6.1")
with open(plik) as file:
    linie = map(str.split, filter(bool, map(str.strip, file.readlines())))
nowe_linie = []
for linia in linie:
    nowe_linie.append(list(map(int, linia)))
print(f"Niemalejące ciągi = {len(list(filter(czy_posortowana, nowe_linie)))}")

print("\n6.2")
