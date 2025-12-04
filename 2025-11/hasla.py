def pobierz_hasla(plik: str) -> list[str]:
    with open(plik) as file:
        file = list(filter(bool, map(str.strip, file)))
    return file

plik = "hasla.txt"

hasla = pobierz_hasla(plik)
hasla_warunkowe = filter(lambda x: set(x) & set("$!%"), filter(lambda x: len(x) >= 12, hasla))
print(len(list(hasla_warunkowe)))

print(30 * "-")

def pierwsza(x: int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

hasla_warunkowe2 = filter(lambda x: all(map(pierwsza, map(ord, set(x)))), hasla)
[print(h) for h in hasla_warunkowe2]

print(30 * "-")

from collections import defaultdict
wyniki = defaultdict(int)
for h in hasla:
    ilosc_specjalnych = len(list(filter(lambda x: not x.isalnum(), list(h))))
    wyniki[ilosc_specjalnych] += 1
    if ilosc_specjalnych == 4:
        print(h)
for k, v in wyniki.items():
    print(f"{k}: {v}")