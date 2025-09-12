#Zamiana liczby dziesiętnej na liczbę o podanym systemie pozycyjnym [2-16]

def decToSys2(d, s):
    r = ""
    litery = ['A','B','C','D','E','F']
    while d>0:
        # 4
        w = d % s
        if w > 9:
            r = litery[w-10] + r
        else:
            r = str(w) + r
        # 5
        d = d // s
    return r