def wyszukiwanie_binarne(lista, element, pocz=0, kon=None):
    if kon is None:
        kon = len(lista) - 1

    if pocz > kon:
        return -1  # Element nie został znaleziony

    pivot = (pocz + kon) // 2
    if lista[pivot] == element:
        return pivot
    elif lista[pivot] > element:
        return wyszukiwanie_binarne(lista, element, pocz, pivot - 1)
    else:
        return wyszukiwanie_binarne(lista, element, pivot + 1, kon)


lista = [1, 3, 4, 5, 6, 11, 34, 123]
print(wyszukiwanie_binarne(lista, 12))
print(wyszukiwanie_binarne(lista, 123))