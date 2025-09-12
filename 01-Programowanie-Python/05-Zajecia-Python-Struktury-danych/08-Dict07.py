# Zastosowania praktyczne
# 1. Napisz program, który zlicza liczbę wystąpień każdego słowa w podanym tekście. Używając słowników.
# 2. Utwórz słownik grupujący liczby z listy na parzyste i nieparzyste.
# 3. Utwórz nowy słownik zawierający tylko te elementy, które spełniają określony warunek (np. wiek > 18).
# 4. Posortuj słownik według wartości.
# 5. Skonwertuj słownik na format JSON i odwrotnie, korzystając z modułu json.
# 6. Utwórz słownik, którego wartościami są inne słowniki, np. baza danych studentów z ocenami.


# Zadanie 1
text = "kot kot pies słoń słoń słoń"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Zadanie 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
grouped = {"parzyste": [], "nieparzyste": []}
for num in numbers:
    if num % 2 == 0:
        grouped["parzyste"].append(num)
    else:
        grouped["nieparzyste"].append(num)
print(grouped)

# Zadanie 3
person = {'Ola': 22, 'Tola': 15, 'Ela': 24, 'Darek': 10, 'Jan': 18, 'Adam': 12}
filtered = {key: value for key, value in person.items() if value > 18}
print(filtered)

# Zdanie 4
person = {'Ola': 12, 'Tola': 15, 'Ela': 14, 'Darek': 10, 'Jan': 18, 'Adam': 12}
sorted_dict = dict(sorted(person.items(), key=lambda item: item[1]))
print(sorted_dict)

# Zadanie 5
import json
person = {'Ola': 12, 'Tola': 15, 'Ela': 14, 'Darek': 10, 'Jan': 18, 'Adam': 12}
json_data = json.dumps(person)  # Słownik → JSON
print(json_data)

dict_from_json = json.loads(json_data)  # JSON → Słownik
print(dict_from_json)


# Zadanie 6
students = {
    "Jan": {"Matematyka": 5, "Angielski": 4},
    "Anna": {"Matematyka": 3, "Angielski": 5},
}

print(students["Jan"]["Matematyka"])
