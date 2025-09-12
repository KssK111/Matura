# Iteracja po słowniku
# 1. Wypisz wszystkie klucze w słowniku `{'Adam':12,'Tola':15,'Ela':14}`.
# 2. Wypisz wszystkie wartości w słowniku `{'Adam':12,'Tola':15,'Ela':14}`.
# 3. Wypisz wszystkie pary klucz-wartość przy użyciu items() w słowniku `{'Adam':12,'Tola':15,'Ela':14}`.
# 4. Sprawdź, czy dany klucz, np. `Adam` znajduje się w słowniku `{'Adam':12,'Tola':15,'Ela':14}`.

# Słownik dostępny
person = {'Adam': 12, 'Tola': 15, 'Ela': 14}
# Zadanie 1
for key in person.keys():
    print(key)

# Zadanie 2
for value in person.values():
    print(value)

# Zadanie 3
for key, value in person.items():
    print(f"{key}: {value}")

# Zadanie 4
if "Adam" in person:
    print("Adam jest w słowniku")
else:
    print("Adama nie ma w słowniku")
