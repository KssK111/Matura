def do_trojkowego(x: int) -> str:
    wynik = ""
    while x > 0:
        reszta = x % 3
        x //= 3
        wynik = str(reszta) + wynik
    return wynik

def suma(plik: str) -> tuple[int, str]:
    suma = 0
    with open(plik) as file:
        linie = filter(lambda x: x, map(str.strip, file.readlines()))
    konwersja = lambda x: "0" if x == "o" else "1" if x == "+" else "2"
    for linia in linie:
        suma += int("".join(map(konwersja, linia)), 3)
    return (suma, do_trojkowego(suma).replace("0", "o").replace("1", "+").replace("2", "*"))
liczba, znaki = suma("symbole.txt")
print(f"{liczba} {znaki}")