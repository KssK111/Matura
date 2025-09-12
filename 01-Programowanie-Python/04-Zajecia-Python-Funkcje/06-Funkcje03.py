# Zadanie. Potęga
# Stwórz funkcję potega(x, n), która zwraca wartość x podniesioną do potęgi n.

def potega(x, n):
    wynik = 1
    for i in range(n):
        wynik *= x
    return wynik


print(potega(2, 3))