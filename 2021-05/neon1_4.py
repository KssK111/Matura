def wykonaj_instrukcje(instrukcja: str, wartosc: str, napis: list[str]):
    match instrukcja:
        case "DOPISZ": napis[0] += wartosc
        case "ZMIEN": napis[0] = napis[0][:-1] + wartosc
        case "USUN": napis[0] = napis[0][:-1]
        case "PRZESUN":
            if wartosc in napis[0]:
                index_do_zmiany = napis[0].index(wartosc)
                zamien_litere = lambda l: 'A' if l == 'Z' else chr(ord(l) + 1)
                napis[0] = napis[0][:index_do_zmiany] + zamien_litere(napis[0][index_do_zmiany]) + napis[0][index_do_zmiany + 1:]

plik = "instrukcje.txt"
with open(plik) as file:
    linie = filter(bool, map(str.strip, file.readlines()))
napis = [""]
wykonaj = lambda x, y: wykonaj_instrukcje(x, y, napis)
[wykonaj(x, y) for x, y in map(str.split, linie)]
print(napis)
print(f"Długość napisu = {len(napis[0])}")