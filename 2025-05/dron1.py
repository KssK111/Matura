from math import gcd

plik = "dron.txt"
with open(plik) as file:
    linie = file.readlines()

linie = map(str.strip, linie)
linie = filter(lambda x: x, linie)
pary = map(lambda x: x.split(" "), linie)
dzielniki = map(lambda x: gcd(abs(int(x[0])), abs(int(x[1]))), pary)
ilosc = len(list(filter(lambda x: x > 1, dzielniki)))
print(f"Ilość par z NWD > 1 = {ilosc}")