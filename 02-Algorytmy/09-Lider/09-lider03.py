# Jeżeli żaden element z pierwszej połowy tablicy nie był liderem,
# to żaden z drugiej połowy również nie może nim być (wtedy wystąpiłbym też w pierwszej połowie).

A = []
def SzukajLidera(A, n):
    p = n // 2
    for i in range(p):
        ile = 0
        for j in range(n-1):
            if A[j]== A[i]:
                ile += 1
        if ile > p:
            return A[i]
    return -1
