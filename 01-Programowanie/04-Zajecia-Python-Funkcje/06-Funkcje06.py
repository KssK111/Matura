# Zadanie. Odwrócona lista
# Napisz funkcję odwrocona_lista(lista), która zwraca odwróconą listę.

def odwrocona_lista(lista):
    for i in range(len(lista) // 2):
        lista[i], lista[len(lista) - i - 1] = lista[len(lista) - i - 1], lista[i]
    return lista


przykladowa_lista = [1, 2, 3, 4, 5]
print(odwrocona_lista(przykladowa_lista))