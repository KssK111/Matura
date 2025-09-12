# Zadanie. Palindrom
# Stwórz funkcję czy_palindrom(tekst), która sprawdza,
# czy podany tekst jest palindromem
# (czytany tak samo od lewej do prawej i odwrotnie).

def czy_palindrom(tekst):
    for i in range(len(tekst)//2):
        if tekst[i] != tekst[len(tekst) - i - 1]:
            return False
    return True


napis = input("Podaj napis: ")
wynik = "Podane slowo jest palindromem" if czy_palindrom(napis) else "Podane slowo nie jest palindromem"
print(wynik)

