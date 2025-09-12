# Zadanie. Tworzenie listy kwadratów
# Utwórz funkcję kwadraty_do_n(n), która zwraca listę kwadratów liczb od 1 do n.

def kwadraty_do_n(n):
    res = []
    for i in range(n):
        res.append(i**2)
    return res


n = int(input("Podaj liczbę: "))
print(kwadraty_do_n(n))