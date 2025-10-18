print("4.1")
def kontakt(liczba: str) -> str:
    wynik = list(liczba)
    if liczba[0] == "1": wynik[1] = "1"
    if liczba[-1] == "1": wynik[-2] = "1"
    for index, cyfra in list(enumerate(liczba))[1:-1]:
        if cyfra == "1":
            wynik[index - 1] = "1"
            wynik[index + 1] = "1"
    return "".join(wynik)
[print(f"{x} = {kontakt(x)}") for x in [
    "1000101001",
    "11001010001",
    "100001",
    "1010101",
]]

print("\n4.2")
def kontakt_warunki(n: int, lancuch: str) -> str:
    wynik = [""] * n
    index = 0
    while index < n:
        wynik[index] = lancuch[index]
        index += 1
    if lancuch[0] == "1": wynik[1] = "1"
    if lancuch[-1] == "1": wynik[-2] = "1"
    index = 1
    while index < n - 1:
        if lancuch[index] == "1":
            wynik[index - 1] = "1"
            wynik[index + 1] = "1"
        index += 1
    wynik_str = ""
    index = 0
    while index < n:
        wynik_str += wynik[index]
        index += 1
    return wynik_str
assert [kontakt_warunki(len(x), x) for x in [
    "1000101001",
    "11001010001",
    "100001",
    "1010101",
]] == [kontakt(x) for x in [
    "1000101001",
    "11001010001",
    "100001",
    "1010101",
]]
def ile_krokow(n: int, lancuch: str) -> int:
    ilosc_krokow = 0
    same_jedynki = True
    for liczba in lancuch:
        if liczba == "0":
            same_jedynki = False
    while not same_jedynki:
        lancuch = kontakt_warunki(n, lancuch)
        ilosc_krokow += 1
        same_jedynki = True
        for liczba in lancuch:
            if liczba == "0":
                same_jedynki = False
    return ilosc_krokow
[print(f"{x} = {ile_krokow(len(x), x)}") for x in [
    "1000101001",
    "11001010001",
    "100001",
    "1010101",
]]