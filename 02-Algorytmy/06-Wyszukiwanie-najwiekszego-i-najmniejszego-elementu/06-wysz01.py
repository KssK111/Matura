from random import randint


def find_min_max(elements):
    if not elements:
        raise ValueError("Zbiór jest pusty")
    min_element = max_element = elements[0]
    for num in elements[1:]:
        if num < min_element:
            min_element = num
        elif num > max_element:
            max_element = num
    return min_element, max_element


lista = [randint(1, 1000) for _ in range(20)]
min_elem, max_elem = find_min_max(lista)
print(f"Najmniejszy: {min_elem}, Największy: {max_elem}")
