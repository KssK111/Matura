# Zadanie. Zwracanie kilku wartości
# Utwórz funkcję statystyki(lista), która zwraca minimum,
# maksimum i średnią arytmetyczną elementów listy.

def statystyki(list):
    minimum = min(list)
    maksimum = max(list)
    srednia = sum(list)/len(list)
    result = {'min': minimum, 'max': maksimum, 'avg': srednia}
    return result


lista = [8, 4, 3, 7, 2, 9, 1, 5, 6, 0]
print(statystyki(lista))