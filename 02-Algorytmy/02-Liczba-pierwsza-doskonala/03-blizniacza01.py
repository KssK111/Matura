# Test na liczby bliźniacze pierwsze. Liczby bliźniacze pierwsze
# to dwie liczby pierwsze różniące się o 2 (np. 11 i 13).
# Napisz funkcję, która sprawdza, czy dwa argumenty podane
# liczby są bliźniaczymi liczbami pierwszymi.

from math import sqrt, fabs

def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def blizniacze(a, b):
    if pierwsza(a) and pierwsza(b):
        if fabs(a-b) == 2:
            return True
        return False
    return  False


print(blizniacze(11,14))

