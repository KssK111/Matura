def odczyt(plik: str) -> str:
    with open(plik) as f:
        return f.read()

def stworz_plik(nazwa: str):
    with open(nazwa, "w") as f:
        pass

def zapisz(plik: str, tekst: str):
    with open(plik, "a") as f:
        f.write(tekst)

plik = "prostokaty.txt"
plik_odpowiedz = "odpowiedź.txt"
dane = odczyt(plik)
stworz_plik(plik_odpowiedz)
zapisz(plik_odpowiedz, dane)