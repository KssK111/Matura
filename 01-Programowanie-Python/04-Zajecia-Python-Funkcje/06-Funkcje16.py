# Zadanie
# Napisz funkcje obliczajaca najmniesza wspolna wielokrotnosc NWW(a,b) wykorzytsujac NWD.


def NWD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def NWW(a,b):
    return a * b // NWD(a, b)


a = 2
b = 3

print("NWD(", a, ",", b, ") = ", NWD(a, b))
print("NWW(", a, ",", b, ") = ", NWW(a, b))