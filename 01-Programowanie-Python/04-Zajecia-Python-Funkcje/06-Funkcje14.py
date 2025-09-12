# Zadanie. Sortowanie listy
# Stwórz funkcję sortuj_liste(lista), która sortuje elementy listy w rosnącej kolejności.

def sortuj_liste(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


list = [7, 5, 2, 8, 9, 1, 6, 3, 4]
print(sortuj_liste(list))
