# Napisz algorytm, ile zostało nominałów kasie po wydaniu n-kwoty reszty.
# W kasie są następujące nominały: [100,50,20,10,5,2,1]
# oraz następująca ilość nominałów: [5,10,3,2,5,2,2].

n = [100, 50, 20, 10, 5, 2, 1]
w = [5, 10, 3, 2, 5, 2, 2]


def zadanie1(n, w, reszta):
    a = reszta
    while a > 0:
        nominal = 0
        for i in range(len(n)):
            if a < n[i]:
                nominal += 1
            else:
                if w[nominal] == 0:
                    nominal += 1
                    break
        w[nominal] -= 1
        a -= n[nominal]
    return w


print(w)
print(zadanie1(n, w, 700))
