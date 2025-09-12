# Zadanie. Liczba parzysta
# Zaimplementuj funkcję czy_parzysta(liczba), która sprawdza, czy podana liczba jest parzysta.

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        print("Podana liczba jest parzysta.")
    else:
        print("Podana liczba nie jest parzysta.")


liczba = int(input("Podaj liczbę: "))
czy_parzysta(liczba)