def F(x: int, p: int, wywolanie = 1) -> int:
    # print(f"Wywolanie nr {wywolanie}")
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p, wywolanie + 1) + c
        else:
            return F(x // p, p, wywolanie + 1) - c

# [print(w) for w in map(lambda x: F(x[0], x[1]), [(125, 2), (130, 3), (220, 4)])]

for p in [3, 4]:
    print(max(filter(lambda x: F(x, p) == 0, range(100))))