# Zadanie. Liczby Fibonacciego
# Napisz funkcję fibonacci(n), która zwraca n pierwszych liczb Fibonacciego.

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        f0 = 0
        f1 = 1
        liczby_fib = [f0, f1]
        for i in range(2, n):
            f1 = f0 + f1
            liczby_fib.append(f1)
            f0 = liczby_fib[i - 1]
    return liczby_fib


n = int(input("Podaj ilość liczb Fiboncciego: "))
print("Pierwsze", len(fibonacci(n)), "liczb Finoacciego:", fibonacci(n))