# Zadanie.
# Sprawdzenie czy podana liczba jest:
# - większa od zera
# - mniejsza od zera
# - jest zerem

liczba = int(input("Podaj liczbę: "))

if liczba > 0:
    print("Podana liczba jest większa od zera.")
elif liczba == 0:
    print("Podana liczba jest zerem.")
else:
    print("Podana liczba jest mniejsza od zera.")