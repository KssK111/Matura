def najwieksza(plik: str) -> tuple[int, str]:
    with open(plik) as file:
        max_int = 0
        max_str = ""
        konwersja = lambda x: "0" if x == "o" else "1" if x == "+" else "2"
        for line in filter(lambda x: x, map(str.strip, file.readlines())):
            if max_int < (liczba := int("".join(map(konwersja, line)), 3)):
                max_int = liczba
                max_str = line
    return (max_int, max_str)
liczba, znaki = najwieksza("symbole_przyklad.txt")
print(f"{liczba} {znaki}")