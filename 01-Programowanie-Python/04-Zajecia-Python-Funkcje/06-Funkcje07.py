# Zadnie. Liczby pierwsze
# Zaimplementuj funkcję czy_pierwsza(liczba), która sprawdza, czy dana liczba jest liczbą pierwszą.


from math import sqrt
def czy_pierwsza(liczba):
    for i in range(2, int(sqrt(liczba))+1):
        if liczba % i == 0:
            return False
    return True


liczba = int(input("Podaj liczbę: "))
wynik = "Liczba pierwsza" if czy_pierwsza(liczba) else "liczba złożona"
print(wynik)