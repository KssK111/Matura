# Napisz aplikację, wyswietlajace trojkat liczbowy
#        1
#       121
#      12321
#     1234321

# Rozwiązanie

n = int(input("Podaj liczbę: "))
for i in range(1, n+1):
    for _ in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()
