# Standardowo
def A(m: int, n: int) -> int:
    if n == 1: return m
    if n % 2 == 0: return A(2 * m, n // 2)
    return 2 * A(m, (n - 1) // 2) + m

# By policzyć REKURENCYJNE wywołania
def A2(m: int, n: int, wywolanie = 0) -> int:
    print(wywolanie)
    if n == 1: return m
    if n % 2 == 0: return A2(2 * m, n // 2, wywolanie + 1)
    return 2 * A2(m, (n - 1) // 2, wywolanie + 1) + m

# Gdy pojedyncze wywołanie może wywołać funkcję więcej niż raz
# Tu nie trzeba bo niby widać dwa takie miejsca w funkcji
# Ale te miejsca od razu zwracają, nie ma wielu wywołań z jednego
# Albo jeśli nie chce się printować przy każdym wywołaniu, wtedy też tak
def A3(m: int, n: int, wywolanie: list[int]) -> int:
    wywolanie[0] += 1
    # Tu już opcjonalnie print, wartość jest w zmiennej
    # Ale w tym zadaniu warto wypisać m i n
    print(f"{wywolanie[0]} - A({m}, {n})")
    if n == 1: return m
    # Jak wywolanie to lista, to już oczywiście bez + 1
    if n % 2 == 0: return A3(2 * m, n // 2, wywolanie)
    return 2 * A3(m, (n - 1) // 2, wywolanie) + m

# A tak tego użyć
# Jak wszystkie wywolania to [0] ale tu REKURENCYJNE, bez początkowego
wywolania = [-1]
A3(3, 9, wywolania)
# Tu wywolania[0] już jest równy liczbie wywołań rekurencyjnych
# print(wywolania[0])
