# Każda liczba niewesoła prędzej czy później wejdzie w cykl,
# a wszystkie takie cykle w systemie dziesiętnym zawsze zawierają liczbę 4.

def czy_wesola(n):
    if n == 1: return True
    if n == 4: return False
    cyfry = [int(i) for i in str(n)]
    potegi = []
    for i in cyfry:
        potegi.append(i ** 2)
    return czy_wesola(sum(potegi))


print(czy_wesola(7))
print(czy_wesola(37))
print(czy_wesola(23))
print(czy_wesola(19))
