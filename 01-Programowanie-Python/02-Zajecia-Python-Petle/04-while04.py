# Zadanie
# Suma cyfr w liczbie

liczba = 45981
suma = 0

while liczba > 0:
    suma += liczba % 10
    liczba //= 10

print("Suma cyfr =", suma)