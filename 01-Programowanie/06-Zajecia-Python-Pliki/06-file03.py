# SPLIT, STRIP
# W Pythonie metoda .split() służy do dzielenia stringa na listę
# fragmentów według określonego separatora.

# Metoda .strip() w Pythonie służy do usuwania określonych znaków
# (domyślnie białych znaków, takich jak spacje, tabulatory i nowe
# linie) z początku i końca stringa.

napis = "Python jest wielki"
wynik = napis.split()
print(wynik)

napis = "Ala,Ola,Tola,Adam,Pola"
wynik2 = napis.split(',')
print(wynik2)

napis = "Ala,Ola,Tola,Adam,Pola"
wynik3 = napis.split(',',2)
print(wynik3)

napis = "Linia1\nLinia2\nLinia3\nLinia4\nLinia5\n"
print(napis)
wynik4 = napis.split("\n")
print(wynik4)

napis ="     Ala, Ola     , Tola      "
rezultat1 = napis.strip()
print(rezultat1)

napis = "!!!!!!!!!!!!!! Witaj w Pythonie !!!!!!!!"
rezultat2 = napis.strip("!")
print(rezultat2)

napis ="     Ala, Ola     , Tola      "
# ['Ala','Ola','Tola']
rezultat3 = napis.strip()
rezultat4 = rezultat3.split(',')
# ['Ala', ' Ola     ', ' Tola']
print(rezultat4)

napis ="     Ala, Ola     , Tola      "
rezultat5 = napis.split(',')
rezultat6 = []
for item in rezultat5:
    rezultat6.append(item.strip())
print(rezultat6)

rezultat7 = [ item.strip() for item in napis.split(',')]
print(rezultat7)

