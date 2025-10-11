def palindromy(plik: str) -> list[str]:
    wynik = []
    with open(plik) as file:
        linie = filter(lambda x: x, map(str.strip, file.readlines()))
    for linia in linie:
        if linia == "".join(reversed(linia)):
            wynik.append(linia)
    return wynik
list(map(print, palindromy("symbole.txt")))