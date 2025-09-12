### Operacje na słownikach
# 1. Połącz dwa słowniki w jeden, używając update().
# Słowniki do połączenia:
# {'Ola':12,'Tola':15,'Ela':14}
# {'Darek':10,'Jan':18,'Adam':12}
# 2. Policz, ile par klucz-wartość znajduje się w słowniku `{'Ola':12,'Tola':15,'Ela':14,'Darek':10,'Jan':18,'Adam':12}`.
# 3. Zamień klucze z wartościami w słowniku (jeśli wartości są unikalne) `{'Ola':12,'Tola':14,'Ela':16,'Darek':10,'Jan':8,'Adam':6}`.
# 4. Stwórz słownik, w którym kluczami będą elementy listy, a wartościami ich długości. `['poniedziałek','wtorek','środa','czwartek','piątek']`
# 5. Utwórz słownik z domyślnymi wartościami dla wszystkich kluczy przy użyciu dict.fromkeys().

# Zadanie 1
women = {'Ola': 12, 'Tola': 15, 'Ela': 14}
men = {'Darek': 10, 'Jan': 18, 'Adam': 12}
all = {}
all.update(women)
all.update(men)
print(all)

# Zadanie 2
dictPerson = {'Ola': 12, 'Tola': 15, 'Ela': 14, 'Darek': 10, 'Jan': 18, 'Adam': 12}
print(len(dictPerson))  # Liczba par klucz-wartość

# Zadanie 3
dictPerson = {'Ola': 12, 'Tola': 15, 'Ela': 14, 'Darek': 10, 'Jan': 18, 'Adam': 12}
reversed_dict = {v: k for k, v in dictPerson.items()}
print(reversed_dict)

# Zadanie 4
words = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek']
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# Zadanie 5
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)
