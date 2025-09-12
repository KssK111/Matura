n = int(input("Podaj wielkość choinki: "))

suma = 0
for wiersz in range(1, n+1):
    suma = suma + ((wiersz * 2) - 1)
print(suma)