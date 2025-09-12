# Popraw algorytm tak, aby zwracał listę ilości nominałów, jaką ma wydać resztę

def wydawanieReszty(reszta):
    nominaly = [100, 50, 20, 10, 5, 2, 1]
    a = []
    for nominal in nominaly:
        if reszta >= nominal:
            ile = reszta // nominal
            reszta = reszta % nominal
            a.append(ile)
        else:
            ile = 0    #
            a.append(ile)
    return a


print(wydawanieReszty(97))
