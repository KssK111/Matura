def silnia(n):
    if n <= 1:
        return 1
    s = 1
    for licz in range(1,n+1):
        s = s * licz
    return s


print(silnia(6))