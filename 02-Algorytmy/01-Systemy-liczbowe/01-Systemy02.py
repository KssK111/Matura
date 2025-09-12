#Zamiana liczby dziesiętnej na liczbę binarną

def decToBin(liczba):
    res = ''
    while liczba > 0:
        res = str(liczba % 2) + res
        liczba //= 2
    return res

print(decToBin(10))