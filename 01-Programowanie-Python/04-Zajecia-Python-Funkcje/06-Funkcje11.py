# Zadania praktyczne. Kalkulator
# Stwórz prosty kalkulator, który przyjmuje dwie liczby
# i operator matematyczny (+, -, *, /) jako argumenty funkcji.

def kalkulator(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    return "Błędne lub operator"


liczbaA = 212
liczbaB = 370
operator = '+'
print(kalkulator(liczbaA, liczbaB, operator))

