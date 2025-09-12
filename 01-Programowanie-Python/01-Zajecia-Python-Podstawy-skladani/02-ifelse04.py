# Zadanie
# Napisz aplikację sprawdzającą czy z trzech podanych
# przez użytkownika boków a,b,c można zbudować trójkąt.

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

# Sprawdzamy, który bok jest nadłuższy.
if a > b and a > c: # a jest największe
    tmp = a
    a = c
    c = tmp
elif b > c: # b jest najwieksze
    tmp = b
    b = c
    c = tmp

# sprawdzamy czy można zbudować trójkąt
if a + b > c:
    print("TAK")
else:
    print("NIE")
