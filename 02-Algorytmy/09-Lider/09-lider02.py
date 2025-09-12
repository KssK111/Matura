# Napisz program, który wylosuje i wypisze tablice dwuwymiarowa liczb całkowitych (o n wierszach i n kolumnach),
# a następnie znajdzie w niej maksimum.

from random import randint


def losuj(N):
    # A tablica dwu wymiarowa - A[][]
    A = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(randint(1, 100))
        A.append(tmp)
    return A


def maksimum(A, N):
    m = A[0][0]
    for i in range(N):
        for j in range(N):
            if A[i][j] > m:
                m = A[i][j]
    return m


def wypisz(A, N):
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()


if __name__ == "__main__":
    N = 5
    A = losuj(N)
    wypisz(A, N)
    print(maksimum(A, N))