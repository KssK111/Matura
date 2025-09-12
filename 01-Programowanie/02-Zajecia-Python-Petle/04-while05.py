# Zadanie
# NWD - algorytm Euklidesa metodą odejmowania

a = 28
b = 56

print("NWD(", a, ",", b, ") = ", end="")
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)

# Zadanie
# NWD - algorytm Euklidesa metodą dzielenia

a = 28
b = 56
print("NWD(", a, ",", b, ") = ", end="")
while b:
    a, b = b, a % b
print(a)
