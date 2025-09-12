# najwiekszy wspólny dzielnik metodą czynniki pierwsze

# funkcja rozkłada liczbę na czynniki pierwsze
def czynniki(n):
    res = []
    i = 2
    while n > 1:
        if n % i == 0:
            res.append(i)
            n = n // i
        else:
            i += 1
    return res


def nwd(a, b):
    a = [czynniki(a), czynniki(b)]
    res = 1
    for i in a[0]:
        if i in a[1]:
            res *= i
            a[1].remove(i)
    return res


print(nwd(56,36))