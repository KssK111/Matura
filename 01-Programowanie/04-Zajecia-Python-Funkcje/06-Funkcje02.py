# Zadanie. Suma liczb
# Napisz funkcję suma_liczb(a, b), która zwraca sumę dwóch liczb.

def suma_liczb(a, b):
    return a + b


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(a, "+", b, "=", suma_liczb(a, b))