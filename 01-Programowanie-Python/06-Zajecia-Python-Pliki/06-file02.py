# Pobieranie danych z pliku do listy

file = 'dane_geny.txt'

lista_geny = []
with open(file, 'r') as f:
    for linia in f:
        lista_geny.append(linia.strip())

print(lista_geny)