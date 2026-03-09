plik = "punkty.txt"
with open(plik) as f:
    punkty = list(map(str.split, f))
punkty = list(map(lambda l: (int(l[0]), int(l[1])), punkty[1:]))

def dl_odcinka(a: tuple[int, int], b: tuple[int, int]):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def czy_prostokatny(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b == c

wynik = []
for x in range(10):
    for y in range(x + 1, 10):
        for z in range(y + 1, 10):
            a = dl_odcinka(punkty[x], punkty[y])
            b = dl_odcinka(punkty[y], punkty[z])
            c = dl_odcinka(punkty[z], punkty[x])
            if czy_prostokatny(a, b, c):
                wynik.append((x, y, z))

print(len(wynik))
[print(x, y, z) for x, y, z in wynik]