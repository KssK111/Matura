# Zadanie
# Wyświetl liczby parzyste za pomocą pętli for od 0 do n

n = int(input("Podaj liczbę n: "))

for i in range(0, n+1, 2):
    print(i, end="  ")

print()

# Praca samodzielna
# Wyświetl liczby nieparzyste za pomocą pętli for od 0 do n
for i in range(1, n+1, 2):
    print(i, end="  ")