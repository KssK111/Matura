def suma_kw(liczba):
    sumaKwadratow = 0
    while liczba > 0:
        cyfra = liczba % 10
        sumaKwadratow += cyfra ** 2
        liczba //= 10
    return sumaKwadratow


def wesola(liczba):
    listaLiczb = []
    while liczba != 1 and liczba not in listaLiczb:
        listaLiczb.append(liczba)
        liczba = suma_kw(liczba)
    return liczba == 1


print(wesola(19))