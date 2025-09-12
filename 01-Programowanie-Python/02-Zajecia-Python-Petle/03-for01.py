# Zadanie.
# wyświetl liczby od 1 do n
# oblicz sumę liczb od 1 do n

n = int(input("Podaj liczbę n: "))

suma = 0
for i in range(1, n+1, 3):
    print(i)
    suma = suma + i

print("Suma ciągu liczb 1+2+...+n =", suma)

