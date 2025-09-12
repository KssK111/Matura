# Algorytm Fibonacciego iteracyjnie (dobry dla dużych liczb)

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


for i in range(0, 11):
    print(fib(i))