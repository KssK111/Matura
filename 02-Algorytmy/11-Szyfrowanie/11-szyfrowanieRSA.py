import random
from math import gcd

def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def generowanie(n, m):
    prime = [i for i in range(n, m+1) if is_prime(i)]
    return random.sample(prime, 2)

def odw(e, fi):
    for i in range(1, fi):
        if (e * i) % fi == 1:
            return i
    return None

def klucz_RSA():
    p, q = generowanie(50, 100)
    n = p * q
    fi = (p - 1) * (q - 1)
    gen = [x for x in range(2, fi) if gcd(x,fi) == 1]
    e = random.choice(gen)
    d = odw(e, fi)
    return (e, n), (d, n) # publiczny, prywatny

def szyfrowanie(wiad, klucz_publiczny):
    e, n = klucz_publiczny
    szyfr = []
    for i in wiad:
        liczba = ord(i)
        kod = (liczba**e) % n
        szyfr.append(kod)
    # szyfr = [ (ord(i)**e) % n for i in wiad]
    return szyfr

def deszyfrowanie(wiad_szyfr, klucz_prywatny):
    d, n = klucz_prywatny
    tekst = ''
    for i in wiad_szyfr:
        tekst = tekst + chr((i**d) % n)
    return tekst

klucze = klucz_RSA()
wiadomosc = "TEST"
wiadomosz_szyfrowana = szyfrowanie(wiadomosc, klucze[0])
print(wiadomosz_szyfrowana)
wiadomosc_odszyfrowana = deszyfrowanie(wiadomosz_szyfrowana, klucze[1])
print(wiadomosc_odszyfrowana)