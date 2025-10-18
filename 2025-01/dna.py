# 3.1
print("3.1")
def zgodnosc(dna1: str, dna2: str) -> float:
    zgodne = len([True for x, y in zip(dna1, dna2) if x == y])
    return (zgodne / len(dna1)) * 100

[print(f"{x}, {y}, Wynik = {zgodnosc(x, y)}%") for x, y in [
    ("GTAGGATATTAT", "AATATTGGAGTG"),
    ("ATGGCAGACC", "ATGGCAGACC"),
    ("CTATGAAAATGTAGATGGTA", "TATTGAATGTGTAGAGTGGT")]]

# 3.2
print("\n3.2")
def najczestszy(n: int, lancuch: str) -> str:
    ilosc_a, ilosc_c, ilosc_g, ilosc_t = 0, 0, 0, 0
    for nukleotyd in lancuch:
        match nukleotyd:
            case "A": ilosc_a += 1
            case "C": ilosc_c += 1
            case "G": ilosc_g += 1
            case "T": ilosc_t += 1
    najwiecej_ilosc = 0
    najwiecej_nukleotyd = ""
    if ilosc_a > najwiecej_ilosc:
        najwiecej_ilosc = ilosc_a
        najwiecej_nukleotyd = "A"
    if ilosc_c > najwiecej_ilosc:
        najwiecej_ilosc = ilosc_c
        najwiecej_nukleotyd = "C"
    if ilosc_g > najwiecej_ilosc:
        najwiecej_ilosc = ilosc_g
        najwiecej_nukleotyd = "G"
    if ilosc_t > najwiecej_ilosc:
        najwiecej_ilosc = ilosc_t
        najwiecej_nukleotyd = "T"
    return najwiecej_nukleotyd

[print(f"n = {len(lancuch)}, {lancuch}, Najczęstszy = {najczestszy(len(lancuch), lancuch)}")
    for lancuch in [
        "GTAGGATATTAT", "AATATTGGAGTG",
        "ATGGCAGACC", "ATGGCAGACC",
        "CTATGAAAATGTAGATGGTA", "TATTGAATGTGTAGAGTGGT"
    ]]

# 3.3
print("\n3.3")
def dlugosc_najdluzszy_wspolny(n: int, dna1: str, dna2: str) -> int:
    najdluzszy_wspolny = 0
    najdluzszy_wspolny_teraz = 0
    index = 0
    while index < n:
        if dna1[index] == dna2[index]:
            najdluzszy_wspolny_teraz += 1
            if najdluzszy_wspolny_teraz > najdluzszy_wspolny:
                najdluzszy_wspolny = najdluzszy_wspolny_teraz
        else: najdluzszy_wspolny_teraz = 0
        index += 1
    return najdluzszy_wspolny
[print(f"n = {len(dna1)}, {dna1}, {dna2}, Wynik = {dlugosc_najdluzszy_wspolny(len(dna1), dna1, dna2)}")
    for dna1, dna2 in [
        ("TAAAATCAAAAAAACGTG", "ATGAATCATTGAAAAAAA"),
        ("GTAGGATATTAT", "AATATTGGAGTG"),
        ("ATGGCAGACC", "ATGGCAGACC"),
        ("CTATGAAAATGTAGATGGTA", "TATTGAATGTGTAGAGTGGT")
    ]]