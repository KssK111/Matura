def ciag_keith_k(k: int) -> list[int]:
    ciag = list(map(int, str_k := str(k)))
    while (nastepny := sum(ciag[len(ciag) - len(str_k):])) <= k:
        ciag.append(nastepny)
    return ciag

def is_keith(k: int) -> bool:
    return k in ciag_keith_k(k)

plik = "liczby.txt"
with open(plik) as file:
    wynik = filter(is_keith, map(int, filter(bool, map(str.strip, file.readlines()))))
test = False
[print(f"{liczba}" + (f" - {ciag_keith_k(liczba)}" if test else "")) for liczba in wynik]