# Zadanie 1.
# Funkcja sprawdzająca, czy podana liczba n jest liczbą pierwszą bez wykorzystania biblioteki math.

def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(pierwsza(23))
