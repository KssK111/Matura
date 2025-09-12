# Funkcja znajdująca NWD dla listy liczb, np. [20, 40, 30, 50]


def find_nwd_in_list(lista) :
    dz = []
    for i in range(1, min(lista) + 1):
        if min(lista) % i == 0:
            a = 0
            for j in lista:
                if j % i == 0:
                    a += 1
                if a == len(lista):
                    dz.append(i)
    return max(dz)


lista = [20, 40, 30, 50]
print(find_nwd_in_list(lista))


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else :
            b -= a
    return a