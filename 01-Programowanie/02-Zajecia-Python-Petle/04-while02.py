# Zadanie
# Najwiekszy wspolny dzielnik

a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))

print("NWD(", a, ",", b, ")=", end="")
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)