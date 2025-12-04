def stopnie_i_wielomiany(plik: str) -> list[tuple[int, list[int]]]:
    with open(plik) as file:
        file = filter(bool, map(str.strip, file))
        file = map(lambda x: (int(x[0]), list(map(int, x[1:]))), map(str.split, file))
        return list(file)
    
def roznica(n: int) -> int:
    return abs((n * (n + 1) // 2) - n)

plik = "wielomiany.txt"

st_w = stopnie_i_wielomiany(plik)
max_roznica = max(map(roznica, map(lambda x: x[0], st_w)))
for (roznicaaa, (st, w)) in zip(map(lambda x: roznica(x[0]), st_w), st_w):
    if roznicaaa == max_roznica:
        print(st, end=" ")
        for x in w:
            print(x, end=" ")
        print()

print("-" * 30)

def fibonacci_gen():
    yield 0
    yield 1
    x, y, tmp = 1, 1, 0
    while True:
        tmp = x + y
        yield tmp
        x = y
        y = tmp

def wartosc_dla_dwa(st_w: tuple[int, list[int]]) -> int:
    st, w = st_w
    wynik = 0
    for (index, x) in enumerate(w):
        wynik += pow(2, st - index) * x
    return wynik

def czy_w_fib(x: int):
    for f in fibonacci_gen():
        if x == f: return True
        if f > x: return False

st_w = stopnie_i_wielomiany(plik)
st_w = list(filter(lambda x: czy_w_fib(wartosc_dla_dwa(x)), st_w))
for (st, w) in st_w:
    print(st, end=" ")
    for w in w:
        print(w, end=" ")
    print()