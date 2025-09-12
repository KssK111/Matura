# Podstawy słowników
# 1. Utwórz słownik zawierający co najmniej trzy pary klucz-wartość, np. imiona i ich wiek. `{'Adam':12,'Tola':15,'Ela':14}`
# 2. Pobierz wartość przypisaną do określonego klucza w słowniku, np. dla słownika `{'Adam':12,'Tola':15,'Ela':14}` pobierz wartość kluacz `Tola`.
# 3. Dodaj nowy element o kluczu `Karol` z wartością `20` do istniejącego słownika `{'Adam':12,'Tola':15,'Ela':14}`.
# 4. Zmień wartość przypisaną do klucza `Tola` na 80 w słowniku `{'Adam':12,'Tola':15,'Ela':14}`.
# 5. Usuń wybrany element, np. element o kluczu `Ela` ze słownika `{'Adam':12,'Tola':15,'Ela':14}` za pomocą del lub pop().

# Zadanie 1
person = {'Adam': 12, 'Tola': 15, 'Ela': 14}
print(person)

# Zadanie 2
person = {'Adam': 12, 'Tola': 15, 'Ela': 14}
print(person["Tola"])  # 15

# Zadanie 3
person["Karol"] = 20
print(person)

# Zadanie 4
person["Tola"] = 80
print(person)

# Zadanie 5
del person["Ela"]  # Usunięcie elementu
# lub person.pop("Ela")
print(person)
