# najwiekszy wspólny dzielnik metodą dzielenia
def nwd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


print(nwd(48,36))