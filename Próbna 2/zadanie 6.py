def dec_na_piec(n: int):
    wynik = ""
    while n > 0:
        wynik = str(n % 5) + wynik
        n //= 5
    return wynik

dwa024, jeden044 = int("2024", 5), int("1044", 5)
print(dec_na_piec(dwa024 + jeden044))
print(dec_na_piec(dwa024 - jeden044))