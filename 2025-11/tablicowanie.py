def tablica(A: list[list[int]], i: int, n: int) -> int:
    if i == n * n:
        return 0
    w = (i // n)
    k = (i % n)
    return A[w][k] + tablica(A, i + 1, n)
tab1, i1, n1 = [[2, 1], [5, 3]], 0, 2
tab2, i2, n2 = [[3, 4], [5, 1]], 0, 2
tab3, i3, n3 = [[1, 2, 1], [3, 1, 1], [2, 1, 4]], 0, 3
print(f"Wynik nr 1 = {tablica(tab1, i1, n1)}")
print(f"Wynik nr 2 = {tablica(tab2, i2, n2)}")
print(f"Wynik nr 3 = {tablica(tab3, i3, n3)}")

def tablica_iter(A: list[list[int]], i: int, n: int) -> int:
    wynik = 0
    while not i == n * n:
        w = i // n
        k = i % n
        wynik += A[w][k]
        i += 1
    return wynik
print(f"Wynik nr 1 = {tablica_iter(tab1, i1, n1)}")
print(f"Wynik nr 2 = {tablica_iter(tab2, i2, n2)}")
print(f"Wynik nr 3 = {tablica_iter(tab3, i3, n3)}")