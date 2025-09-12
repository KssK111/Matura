# pobieranie danych z pliku

listaLiczb = []

with open('dane.txt', 'r') as file:     # nazwa i/lub miejsce pliku z otwarciem pliku
    for line in file:                   # operacje na/w pliku
        listaLiczb.append(int(line))    # zamykanie pliku, tu dzieje się to automatycznie

print(listaLiczb)

with open('dane.txt', 'r') as file:
    print(file.readlines())

