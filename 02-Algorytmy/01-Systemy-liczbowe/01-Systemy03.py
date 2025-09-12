#Zamiana liczby dziesiętnej na liczbę o podanym systemie pozycyjnym [2-16]

def decToSys(d, s):
    res = ""
    while d>0:
        # 4
        w = d % s
        if w > 9:
            if w == 10: res = "A" + res
            if w == 11: res = "B" + res
            if w == 12: res = "C" + res
            if w == 13: res = "D" + res
            if w == 14: res = "E" + res
            if w == 15: res = "F" + res
        else:
            res = str(w) + res
        # 5
        d = d // s
    return res


print(decToSys(10, 2))