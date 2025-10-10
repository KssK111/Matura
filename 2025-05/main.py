def przestaw(n: int) -> int:
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w

def przestaw_2(n: int) -> int:
    wynik = 0
    mnoznik = 1
    while n > 0:
        if n < 10: return wynik + n * mnoznik
        prawa = n % 10
        n //= 10
        lewa = n % 10
        n //= 10
        wynik += lewa * mnoznik
        mnoznik *= 10
        wynik += prawa * mnoznik
        mnoznik *= 10
    return wynik

liczby = [316498, 43657688, 154005710, 998877665544321]
lista_rek = list(map(przestaw, liczby))
lista_iter = list(map(przestaw_2, liczby))
assert lista_rek == lista_iter

liczby = list(range(1_000_000))
lista_rek = list(map(przestaw, liczby))
lista_iter = list(map(przestaw_2, liczby))
assert lista_rek == lista_iter