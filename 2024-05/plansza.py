def plansza_wynik(A: list[list[int]]) -> bool:
    n = len(A)
    m = len(A[0])
    P = [[True for i in range(m)] for i in range(n)]
    P[0][0] = True
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                P[i][j] = False
            else:
                if i == 0 and j != 1:
                    P[i][j] = P[i][j - 1]
                if i != 0 and j == 1:
                    P[i][j] = P[i - 1][j]
                if i != 0 and j != 1:
                    P[i][j] = P[i][j - 1] or P[i - 1][j]
    return P[n - 1][m - 1]

a = [[1,1,1],[0,1,0],[1,1,1]]
print(plansza_wynik(a))
b = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
print(plansza_wynik(b))