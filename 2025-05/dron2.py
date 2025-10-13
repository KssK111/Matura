plik = "dron_przyklad.txt"
with open(plik) as file:
    linie = file.readlines()

linie = map(str.strip, linie)
linie = filter(lambda x: x, linie)
pary = map(lambda x: x.split(" "), linie)
pary = map(lambda x: (int(x[0]), int(x[1])), pary)

x, y = 0, 0
ilosc = 0
for (x_p, y_p) in pary:
    x, y = x + x_p, y + y_p
    if all([x < 5000, y < 5000, x, y]):
        ilosc += 1

print(f"Ilość punktów w kwadracie = {ilosc}")
