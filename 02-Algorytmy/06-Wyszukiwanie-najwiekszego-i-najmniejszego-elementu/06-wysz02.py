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


# Zadanie 1
# Napisz funkcję zwracającą najzimniejszy i najcieplejszy dzień na podstawie temperatur z tygodnia.
temp_tyg = [18, 21, 17, 25, 19, 23, 22]
print(find_min_max(temp_tyg))

# Zadanie 2
# Napisz funkcję zwracającą najmniejszy i największy znak w stringu np.: `programowanie`. Najmniejszym znakiem jest
# `a`, czyli ten znak którego, liczba w kodzie ASCII jest najmniejsza. Największym jest w tym przypadku `z` czyli ten
# znak którego, liczba w tablicy ASCII jest największa. `ord('a')` - zwraca liczbę z kodu ascii. `chr(98)` - zwraca
# znak o podanej liczbie w kodzie ascii.

napis = 'programowanie'
print(find_min_max(napis))


# Zadanie 3
# Napisz funkcję zwracającą najkrótsze i najdłuższe słowo w liście.

def find_min_max_len_word(elements):
    if not elements:
        raise ValueError("Zbiór jest pusty")
    min_element = max_element = elements[0]
    for word in elements[1:]:
        if len(word) < len(min_element):
            min_element = word
        elif len(word) > len(max_element):
            max_element = word
    return min_element, max_element


slowa = ["pies", "kot", "hipopotam", "koń", "lew"]
print(find_min_max_len_word(slowa))


# Zadanie 4
# Napisz funkcję znajdującą najmniejszy i największy element w liście 2D.

def find_min_max_2d(elements):
    if not elements:
        raise ValueError("Zbiór jest pusty")
    min_element = max_element = elements[0][0]
    for element in elements:
        for num in element:
            if num < min_element:
                min_element = num
            elif num > max_element:
                max_element = num
    return min_element, max_element


lista2D = [[3, 8, 1], [4, 6, 9], [5, 2, 7]]
print(find_min_max_2d(lista2D))

# Zadanie 5
# Napisz funkcję znajdującą najwcześniejszą i najpóźniejszą datę w liście. Do wykorzystania dat należy zaimportować
# funkcje `date` z biblioteki `datetime` w następujący sposób:

from datetime import date

dates = [date(2021, 5, 1), date(2023, 3, 15), date(2025, 7, 20), date(1999, 6, 5)]

oldest_date, latest_date = find_min_max(dates)
print(f"Najstarsza: {oldest_date}, Najnowsza: {latest_date}")


# Zadanie 6
# Napisz funkcję znajdującą najstarszą i najmłodszą osobę w grupie osób zapisanych w słowniku.
# Dane wyświetl jako imię i jego wiek.

def find_min_max_dict(elements):
    if not elements:
        raise ValueError("Zbiór jest pusty")
    min_element_key, min_element_value = next(iter(elements.items()))
    max_element_key, max_element_value = next(iter(elements.items()))
    for key, value in elements.items():
        if value < min_element_value:
            min_element_value = value
            min_element_key = key
        elif value > max_element_value:
            max_element_value = value
            max_element_key = key
    return {min_element_key: min_element_value, max_element_key: max_element_value}


persons = {"Anna": 29, "Bartek": 34, "Celina": 24, "Daniel": 31}

print(find_min_max_dict(persons))
