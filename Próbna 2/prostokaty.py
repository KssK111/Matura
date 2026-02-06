def pobierz_prostokaty(plik: str) -> list[tuple[int, int]]:
    with open(plik) as f:
        return list(map(lambda x: tuple(map(int, x.split())), filter(bool, map(str.strip, f.readlines()))))

plik = "prostokaty.txt"
prostokaty = pobierz_prostokaty(plik)
max_pole = max(map(lambda x: x[0] * x[1], prostokaty))
min_pole = min(map(lambda x: x[0] * x[1], prostokaty))
print("4.1")
print(f"Max pole = {max_pole}\nMin pole = {min_pole}")

print("\n4.2")
from itertools import takewhile, starmap
def najdluzszy_ciag(lista: list[tuple[int, int]]) -> list[tuple[int, int]]:
    warunek = lambda x: x[0][0] <= x[1][0] and x[0][1] <= x[1][1]
    return list(map(lambda x: x[0], takewhile(warunek, zip(lista[1:], lista[:-1]))))
ciag_ciagow = starmap(lambda i, _: prostokaty[i:], enumerate(prostokaty))
max_ciag = max(map(najdluzszy_ciag, ciag_ciagow), key=len)
ostatni = max_ciag[-1]
print(f"Długość = {len(max_ciag)}\nh = {ostatni[0]}\ns = {ostatni[1]}")

print("\n4.3")
wysokosci = set(map(lambda x: x[1], prostokaty))
odpowiedzi = []
for wys in wysokosci:
    szerokosci = list(map(lambda x: x[1], filter(lambda x: x[0] == wys, prostokaty)))
    max_5 = sorted(szerokosci, reverse=True)
    odpowiedzi.append((wys, sum(max_5[:2]), sum(max_5[:3]), sum(max_5[:5])))
print("Max szerokość dla _ prostokątów:")
print(f"2: {max(map(lambda x: x[1], odpowiedzi))}")
print(f"3: {max(map(lambda x: x[2], odpowiedzi))}")
print(f"5: {max(map(lambda x: x[3], odpowiedzi))}")