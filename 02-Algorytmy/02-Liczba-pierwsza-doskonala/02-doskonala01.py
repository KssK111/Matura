# funkcja sprawdzająca czy podana liczba jest doskonała

def doskonala(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n: return True
    return False


print(doskonala(28))