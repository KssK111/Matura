def pobierz_pole(plik: str) -> list[list[int]]:
    with open(plik) as f:
        return list(map(lambda x: list(map(int, x)), map(str.split, map(str.strip, f.readlines()))))

pole_waclawa = pobierz_pole("pole_waclawa.txt")
print(pole_waclawa)

def srednia_pola(pole: list[list[int]]) -> float:
    suma = sum(map(sum, pole))
    ilosc = sum(map(len, pole))
    return  suma / ilosc

