# Znajdź pierwszy element większy od X.
from random import randint

arr = sorted([randint(1, 10) for _ in range(10)])
print(arr)
def first_elem(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


print(first_elem(arr, 4))