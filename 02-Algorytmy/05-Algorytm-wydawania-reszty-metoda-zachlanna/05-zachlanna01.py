
def wydawanieReszty(reszta):
    nominaly = [100, 50, 20, 10, 5, 2, 1]
    i = 0
    while reszta > 0:
        if reszta >= nominaly[i]:
            ile = reszta // nominaly[i]
            print(f"{nominaly[i]} = {ile} szt.")
            reszta = reszta % nominaly[i]
        else :
            i = i + 1


wydawanieReszty(97)