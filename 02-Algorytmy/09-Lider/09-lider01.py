# Wyszukiwnaie lidera

from random import randint

A = [randint(1, 4) for _ in range(9)]

print(A)


def lider(A):
    l = len(A) // 2
    if len(A) % 2 != 0:
        l += 1
    for i in A:
        nowyLider = i
        ile = 0
        for j in A:
            if nowyLider == j:
                ile += 1
                if ile >= l:
                    return j
    return "Brak lidera"


print(lider(A))