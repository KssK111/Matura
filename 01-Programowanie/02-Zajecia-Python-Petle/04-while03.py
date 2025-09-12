# Zadanie
# Zgadywanie liczby wylosowanej z zakresu <0,100>
# Napisz aplikację: Zgadywanie liczby wylosowanej z zakresu <0,100>, uzupełnij kod poniżej

from random import randint

print("Zgadywanie liczb z przedziału [0; 100]")
szukana = randint(0,100)
proba = 1
liczba = -1

while szukana != liczba:
    proba += 1
    liczba = int(input("Podaj liczbę: "))
    if liczba < szukana:
        print("za mała")
    elif liczba > szukana:
        print("za duża")
    else:
        print("Brawo! Zgadles liczbe po ", proba," probach.")





while liczba != szukana:
    print("\nPróba ", proba, ": ", end="")
    liczba = int(input())
    if liczba < szukana:
        print("Za mała")
    else:
        if liczba > szukana:
            print("Za duża")
        else:
            print("Brawo! Udało ci się za", proba, "razem")
    proba = proba + 1