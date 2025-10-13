plik = "dron.txt"
with open(plik) as file:
    linie = file.readlines()

linie = map(str.strip, linie)
linie = filter(lambda x: x, linie)
pary = map(lambda x: x.split(" "), linie)
pary = map(lambda x: (int(x[0]), int(x[1])), pary)

punkty = []
x, y = 0, 0
ilosc = 0
for (x_p, y_p) in pary:
    x, y = x + x_p, y + y_p
    punkty.append((x, y))
    if all([x < 5000, y < 5000, x, y]):
        ilosc += 1
print(f"a) {ilosc}")

punkty_wynik = None
for punkt1 in punkty:
    for punkt2 in punkty:
        suma_x = punkt1[0] + punkt2[0]
        suma_y = punkt1[1] + punkt2[1]
        if not all([suma_x % 2 == 0, suma_y % 2 == 0]): continue
        srodek = (suma_x // 2, suma_y // 2)
        if srodek in punkty and srodek not in [punkt1, punkt2]:
            if not punkty_wynik:
                punkty_wynik = f"b) {punkt1}, {srodek}, {punkt2}"
print(punkty_wynik)