# Zadanie. Średnia arytmetyczna
# Napisz funkcję srednia(lista), która oblicza i zwraca średnią arytmetyczną elementów listy.

def srednia(lista):
    wynik = 0
    for i in lista:
        wynik += i
    return wynik / len(lista)


lista_liczb = [1, 2, 3, 4, 5]
print("Średnia liczb w liście = ", srednia(lista_liczb))