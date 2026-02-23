def pobierz_slowa(plik: str) -> list[str]:
    with open(plik) as f:
        return list(map(str.strip, f.readlines()))

plik = "slowa.txt"
slowa = pobierz_slowa(plik)
palindromy = list(filter(lambda x: x == "".join(reversed(x)), slowa))

print(f"Ilość palindromów = {len(palindromy)}")

ilosc_rodzin = len(set(map(len, palindromy)))
print(f"Ilość rodzin = {ilosc_rodzin}")

from collections import defaultdict
rodziny = defaultdict(list[str])
list(map(lambda x: rodziny[len(x)].append(x), palindromy))
x = list(map(sorted, rodziny.values()))
print(x)