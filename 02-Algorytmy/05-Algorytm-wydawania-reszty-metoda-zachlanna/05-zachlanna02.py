# Popraw algorytm tak, aby zwracał listę ilości nominałów, jaką ma wydać resztę

def wydawanieReszty(reszta):
    nominaly = [100, 50, 20, 10, 5, 2, 1]
    i = 0
    a = [0 for i in nominaly]
    while reszta > 0:
        if reszta >= nominaly[i]:
            ile = reszta // nominaly[i]
            reszta = reszta % nominaly[i]
            a[i] = ile
        else:
            ile = 0
            a[i] = ile
        i = i + 1
    return a


print(wydawanieReszty(97))