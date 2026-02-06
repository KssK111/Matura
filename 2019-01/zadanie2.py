def czy_odkryta(n_system: tuple[str, int]) -> bool:
    n, system = n_system
    liczba = int(n, system)
    cyfry = filter(lambda x: x != 0, map(int, set(n)))
    return all(map(lambda x: liczba % x == 0, cyfry))

#2.3
def czy_odkryta_dec(n: int) -> bool:
    cyfry = filter(lambda x: x != 0, map(int, set(str(n))))
    return all(map(lambda x: n % x == 0, cyfry))

cyfry = [15,308,2436,12774,31662]
print("2.1")
[print(f"{x} - {y}") for x, y in zip(cyfry, map(czy_odkryta_dec, cyfry))]

cyfry = [("222", 4), ("414", 5), ("154", 6), ("470", 8), ("333", 9)]
print("\n2.2")
[print(f"{x} - {y}") for x, y in zip(cyfry, map(czy_odkryta, cyfry))]