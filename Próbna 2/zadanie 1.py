n = 19
pozycja = 1
while n > 0:
    reszta = n % 2
    n //= 2
    if reszta == 1:
        print(pozycja)
    pozycja += 1