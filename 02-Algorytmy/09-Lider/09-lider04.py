# Napisz program realizujący pierwszy algorytm znajdowania lidera
# (sprawdzanie każdego elementu oddzielnie). Algorytm zaimplementuj
# w postaci funkcji. Wykorzystaj funkcje Losuj, uzupełnij także program
# o funkcje wypisująca tablice.

from random import randint


# A jest listą
def SzukajLidera(A, N):
    for i in range(N):
        ile = 0
        for j in range(N):
            if A[j] == A[i]:
                ile += 1
        if ile > N / 2:
            return A[i]
    return -1


def Losuj(A, N):
    x = randint(1, 100)
    for i in range(N):
        if randint(0, 1) == 0:
            A.append(randint(1, 100))
        else:
            A.append('x')
    return A


def Wypisz(A, N):
    for i in range(N):
        print(A[i], end="\t")
    print()


N = 20
A = []
Losuj(A, N)
Wypisz(A, N)
lider = SzukajLidera(A, N)
if lider == -1:
    print("W tablicy nie ma lidera")
else:
    print("Liderem jest ", lider)