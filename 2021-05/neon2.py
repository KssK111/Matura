from itertools import starmap, takewhile

plik = "instrukcje.txt"
with open(plik) as file:
    linie = filter(bool, map(str.strip, file.readlines()))
instrukcje = list(starmap(lambda x, y: x, map(str.split, linie)))
inst_ciag = list(starmap(lambda i, inst: (inst, [inst] + list(takewhile(lambda x: x == inst, instrukcje[i + 1:]))), enumerate(instrukcje)))
wynik, ciag = max(inst_ciag, key=lambda x: len(x[1]))
print(f"{wynik} - {len(ciag)}")