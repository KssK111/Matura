from itertools import chain, starmap, takewhile

print("6.1")
plik = "dane.txt"
with open(plik) as file:
    linie = list(filter(bool, map(str.strip, file.readlines())))
wiersze = list(map(lambda x: list(map(int, x.split(" "))), linie))
wszystko_w_jednym = list(chain.from_iterable(wiersze))
print(f"Najjaśniejszy = {max(wszystko_w_jednym)}")
print(f"Najciemniejszy = {min(wszystko_w_jednym)}")

print("\n6.2")
tmp_wiersze = wiersze[:]
nie_palindrom = lambda x: not x == list(reversed(x))
wynik = len(list(filter(bool, map(nie_palindrom, tmp_wiersze))))
print(f"Najmniejsza ilość wierszy którą należy ununąć = {wynik}")

print("\n6.3")
def sprawdz_kontrast(index_wiersza: int, index_kolumny: int, piksel: int) -> bool:
    sasiedzi = []
    if not index_kolumny == 0: sasiedzi.append(wiersze[index_wiersza][index_kolumny - 1])
    if not index_kolumny == 320 - 1: sasiedzi.append(wiersze[index_wiersza][index_kolumny + 1])
    if not index_wiersza == 0: sasiedzi.append(wiersze[index_wiersza - 1][index_kolumny])
    if not index_wiersza == 200 - 1: sasiedzi.append(wiersze[index_wiersza + 1][index_kolumny])
    return any(map(lambda x: abs(x - piksel) > 128, sasiedzi))
wszystko_w_jednym = chain.from_iterable(wiersze)
wynik = len(list(filter(bool, starmap(sprawdz_kontrast, starmap(lambda i, x: (i // 320, i % 320, x), enumerate(wszystko_w_jednym))))))
print(f"Ilość pikseli które mają kontrastującego sąsiada = {wynik}")

print("\n6.4")
najdluzsza_linia = lambda linia: len(max(starmap(lambda i, p: list(takewhile(lambda x: p == x, linia[i:])), enumerate(linia)), key=len))
wynik = max(map(najdluzsza_linia, zip(*wiersze)))
print(f"Najdluższa linia = {wynik}")