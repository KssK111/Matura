def wyszukiwanie_binarne_iter(lista, element):
    pocz = 0
    kon = len(lista) - 1

    while pocz <= kon:
        pivot = (pocz + kon) // 2
        if lista[pivot] == element:
            return pivot
        elif lista[pivot] > element:
            kon = pivot - 1
        else:
            pocz = pivot + 1

    return -1  # Element nie został znaleziony


lista = [1, 3, 4, 5, 6, 11, 34, 123]
print(wyszukiwanie_binarne_iter(lista, 12))
print(wyszukiwanie_binarne_iter(lista, 123))
