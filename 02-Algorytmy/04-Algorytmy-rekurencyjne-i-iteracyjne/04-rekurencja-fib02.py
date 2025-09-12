# Algorytm Fibonacciego rekurencyjnie

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)


for i in range(11):
    print(fib(i))