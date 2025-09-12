# Zadanie
# Funkcja wydawanie reszty metoda zachlanna.

def reszta(n):
    m = [50, 20, 10, 5, 2, 1]
    for i in m:
        ile = n // i
        if ile > 0:
            print(i, ile)
        n = n % i


reszta(int(input()))