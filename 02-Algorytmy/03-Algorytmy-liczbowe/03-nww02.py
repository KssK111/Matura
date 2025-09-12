# Dodawanie ułamków

def nwd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def nww(a, b):
    return a * b // nwd(a, b)


l1 = 1
m1 = 2

l2 = 1
m2 = 4

m = nww(m1, m2)     # wspólny mianownik
l = (l1 * (m // m1)) + (l2 * (m // m2))     # suma liczników
c = l // m          # wyciągamy całości
l = l % m           # skracamy ułamek

if c == 0:
    print(f"{l}/{m}")
else:
    print(f"{c} {l}/{m}")