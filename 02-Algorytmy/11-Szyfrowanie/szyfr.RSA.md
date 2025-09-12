1. Wybieramy dwie liczby pierwsze p i q.
2. Obliczmy wartosc n = p * q
3. Wyliczamy funkcje Eulera dla n z przedzaiłu 1 < e < fi(n)
   fi = (p - 1) * (q - 1)  

przyklad Funkcja Eulera
p = 3
q = 5
n = p * q = 15
Liczby mniejsze: 1,2,3,4,5,6,7,8,9,10,11,12,13,14
Liczby względne: 1,2,4,7,8,11,13,14

4. Obliczmy odwrotnosc module fi(n) liczby e i otrzymujemy d, 
   jest elementem klucza prywatnego

Szyfrowanie
f(W) = W^e mod n

Deszyfrowanie
f(S) = S^d mod n


import random

def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def genrowanie(n, m):
    prime = [i for i in range(n, m+1) if is_prime(i)]
    return random.sample(prime, 2)
