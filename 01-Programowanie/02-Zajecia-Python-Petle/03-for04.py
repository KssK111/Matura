# trojkat o wysokosci x, ze znakow podanych przez uzytkownika

znak = input("Podaj znak z jakich wydrukuje trojkat: ")
n = int(input("Podaj wysokosc trojkata: "))

for i in range(n):
    for j in range(n-i, 1, -1):
       print(" ", end="")
    for k in range(i*2+1):
        print(znak, end="")
    print()


# ilosc znakow w choince
# dla n = 4
# *
# **
# ***
# ****
n = 4
suma = 0
for i in range(1,n+1):
    suma = suma + i
print(suma)


def sumaGwiazdek(x):
    suma = 0
    for i in range(1,x+1):
        suma = suma + i
    return suma

n = 4
print(sumaGwiazdek(n))


#    *
#   ***
#  *****
# *******

def sumaGwiazdekChoinki(x):
    suma = 0
    for i in range(1,x+1):
        suma = suma + (i*2-1)
    return suma

n = 8
print(sumaGwiazdekChoinki(n))
