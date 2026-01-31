n = 10
A = [5,99,3,7,111,13,4,24,4,8]

lewo, prawo, srodek = 0, n - 1, n // 2
while True:
    if A[srodek] % 2 == 0:
        if A[srodek - 1] % 2 != 0:
            w = A[srodek]
            break
        else:
            prawo = srodek
            srodek = (lewo + prawo) // 2
    else:
        lewo = srodek
        srodek = (lewo + prawo) // 2

print(w)

#1.2
#logarytmiczna