# Zadanie 1
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0 = 0
    f1 = 1
    for i in range(n-1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn


def fibR(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)


for i in range(101):
    print("F"+str(i)+"="+ str(fib(i)))

for i in range(101):
    print(f"F{i}={fibR(i)}")
