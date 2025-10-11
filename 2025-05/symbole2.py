def kwadraty(plik: str) -> tuple[int, list[tuple[int, int]]]:
    ilosc = 0
    znalezione_kwadraty = []
    with open(plik) as file:
        linie = list(filter(lambda x: x, map(str.strip, file.readlines())))
    for (index_linii, linia) in list(enumerate(linie))[1:-1]:
        for (index_srodka, znak) in list(enumerate(linia))[1:-1]:
            l1 = linie[index_linii - 1]
            l2 = linie[index_linii]
            l3 = linie[index_linii + 1]
            kwadrat = [l1[index_srodka - 1], l1[index_srodka], l1[index_srodka + 1],
                       l2[index_srodka - 1], l2[index_srodka], l2[index_srodka + 1],
                       l3[index_srodka - 1], l3[index_srodka], l3[index_srodka + 1]]
            if all(map(lambda punkt_kw: punkt_kw == znak, kwadrat)):
                ilosc += 1
                wiersz = index_linii + 1
                pozycja = index_srodka + 1
                znalezione_kwadraty.append((wiersz, pozycja))
    return (ilosc, znalezione_kwadraty)
(ilosc, kwdrty) = kwadraty("symbole.txt")
print(ilosc, end="")
for kw in kwdrty: print(f" {kw[0]} {kw[1]}", end="")