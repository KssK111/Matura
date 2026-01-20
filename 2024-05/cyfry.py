def oblicz_c_wyk(n: int) -> tuple[int, int]:
    b = 1
    c = 0
    wyk = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * (a // 2)
        else:
            wyk += 1
            c = c + b
        b = b * 10
    return (c, wyk)

c, wyk = oblicz_c_wyk(33658)
print(f"c = {c}\nilość wykonań (c = c + b) = {wyk}")
c, wyk = oblicz_c_wyk(542102)
print(f"c = {c}\nilość wykonań (c = c + b) = {wyk}")
c, wyk = oblicz_c_wyk(87654321012345678)
print(f"c = {c}\nilość wykonań (c = c + b) = {wyk}")
c, wyk = oblicz_c_wyk(333333666666999999)
print(f"c = {c}\nilość wykonań (c = c + b) = {wyk}")


