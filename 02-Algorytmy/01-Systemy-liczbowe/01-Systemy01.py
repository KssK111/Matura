# funkcje wbudowane zamiany liczby dziesiętnej na liczbę o podanym systemie

l = 67

print(bin(l))
print(hex(l))
print(oct(l))

def decToBin(liczba):
    response = ""
    while liczba > 0:
        reszta = liczba % 2
        liczba = liczba // 2
        response = str(reszta) + response
    return response

print(decToBin(l))