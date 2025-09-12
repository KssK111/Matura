# Sortowanie przez scalanie
from random import randint

def sort1(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = sort1(array[:mid])
    right_half = sort1(array[mid:])
    return sort2(left_half, right_half)


def sort2(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


liczby = [ randint(-10, 10) for _ in range(20)]
print(liczby)
print(merge_sort(liczby))