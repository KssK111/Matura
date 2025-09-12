# Zadanie 1.
# Funkcja sprawdzająca, czy podana liczba n jest liczbą pierwszą.

# wariant 1

def pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(pierwsza(8))

# wariant 2

from math import sqrt

def pierwsza1(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


print(pierwsza1(23))
