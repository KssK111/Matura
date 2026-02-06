def pobierz_ruchy(plik: str) -> list[list[str]]:
    with open(plik) as f:
        return list(map(list, filter(bool, map(str.strip, f.readlines()))))
    
def pobierz_plansze(plik: str) -> list[list[int]]:
    with open(plik) as f:
        return list(map(lambda x: list(map(int, x)), map(str.split, filter(bool, map(str.strip, f.readlines())))))

plik_plansza = "plansza.txt"
plik_ruchy = "robot.txt"
plansza = pobierz_plansze(plik_plansza)
ruchy = pobierz_ruchy(plik_ruchy)

def oblicz_punkty(ruchy: list[str]):
    punkty = plansza[0][0]
    x, y = 0, 0
    for ruch in ruchy:
        match ruch:
            case "N": y -= 1
            case "S": y += 1
            case "W": x -= 1
            case "E": x += 1
        if not x in range(20) or not y in range(20):
            return -1
        punkty += plansza[y][x]
    return punkty

print("4.1")
punkty = list(map(oblicz_punkty, ruchy))
print(len(list(filter(lambda x: x == -1, punkty))))

print("\n4.2")
max_punkty = max(punkty)
print(f"Numer - {punkty.index(max_punkty) + 1}\nPunkty - {max_punkty}")

from itertools import starmap, takewhile
def najdluzszy_ciag_lewo_prawo(ruchy: list[str]):
    ciagi = starmap(lambda i, _: ruchy[i:], enumerate(ruchy))
    ciagi_gotowe = map(lambda c: list(takewhile(lambda x: x in ["W", "E"], c)), ciagi)
    return max(ciagi_gotowe, key=len)

dlugosci_ciagow = list(map(len, map(najdluzszy_ciag_lewo_prawo, ruchy)))
max_lewo_prawo = max(dlugosci_ciagow)

print("\n4.3")
print(f"Najdłuższy ciąg prawo lewo\n{max_lewo_prawo}")
print("Numery graczy z ciągiem o takiej długości")
for i, dl in enumerate(dlugosci_ciagow):
    if dl == max_lewo_prawo:
        print(i + 1)