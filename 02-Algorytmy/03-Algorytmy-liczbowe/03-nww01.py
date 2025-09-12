# najmniejsza wspólna wielokrotność dwóch liczb

def nwd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def nww(a, b):
    return a * b // nwd(a, b)


print(nww(6, 60))