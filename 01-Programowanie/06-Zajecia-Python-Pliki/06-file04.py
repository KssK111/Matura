import random

lista = []
with open("dane_geny.txt", "r") as f:
    for linia in f:
        lista.append( ( len(linia.strip()), linia.strip() ) )



def los(n):
    return [ random.randint(500, 5000) for _ in range(n)]

liczby = los(1000)

with open("liczby.txt", "a") as f:
    for liczba in liczby:
        f.write( f"{liczba} \n")

# odczyt z pliku liczby i srednia liczb parzystych i nieparzystych
def funkcjaParzyste():
    parzyste = ...
    return parzyste

# print(lista)
# print(lista[0])
# print(lista[0][0])
# print(lista[0][1])
# print(lista[0][1].count('A'))
# print( (lista[0][1].count('A')/lista[0][0]) * 100, "%" )

maks_procent = 0
linia = ''
for t in lista:
    if t[1].count('A')/t[0] > maks_procent:
        maks_procent = t[1].count('A')/t[0]
        linia = t


print(linia, maks_procent * 100 , "%", [])

unique_letter = list(set(linia[1]))
print(sorted(unique_letter))


u = []
for i in linia[1]:
    if i not in u:
        u.append(i)
print(sorted(u))