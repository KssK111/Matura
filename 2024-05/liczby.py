def pobierz_wiersze(plik: str) -> tuple[list[int], list[int]]:
    with open(plik) as f:
        return tuple(map(lambda l: list(map(int, l.split())), filter(bool, map(str.strip, f.readlines()))))

plik = "liczby.txt"
wiersz1, wiersz2 = pobierz_wiersze(plik)

ile_dzielnikiem = 0
for dzielnik in wiersz1:
    for liczba in wiersz2:
        if liczba % dzielnik == 0:
            ile_dzielnikiem += 1
            break
print("4.1")
print(ile_dzielnikiem)

print("4.2")
print(sorted(wiersz1)[-101])

def rozklad(n: int) -> list[int]:
    wynik = []
    dzielnik = 2
    while n > 1:
        while n % dzielnik == 0:
            wynik.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
    return wynik

print(rozklad(99))