# Sortowanie bąbelkowe

liczby = [3,5,1,7,2]
print(liczby)
def sortBabel(liczby):
    n = len(liczby)
    for i in range(n):
        for i in range(n-1):
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]
    return liczby


print(sortBabel(liczby))

# Sortowanie bąbelkowe optymalny

liczby = [3,5,1,7,2]
print(liczby)
def sortBabelOpt(liczby):
    n = len(liczby)
    for i in range(n):
        for i in range(n-1-i):
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1], liczby[i]
    return liczby
print(sortBabelOpt(liczby))