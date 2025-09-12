# Zadanie. Zliczanie wystąpień
# Napisz funkcję zlicz_wystapienia(tekst),
# która zlicza ilość wystąpień każdego znaku w podanym tekście.

def zlicz_wystapienia(tekst):
    wystapienia = {}
    for znak in tekst:
        if znak in wystapienia.keys():
            wystapienia[znak] += 1
        else:
            wystapienia[znak] = 1
    return wystapienia


dowolny_tekst = input("Podaj dowolny tekst: ")
wynik = zlicz_wystapienia(dowolny_tekst)
for znak, ilosc in wynik.items():
    print(f"'{znak}': {ilosc} razy")
