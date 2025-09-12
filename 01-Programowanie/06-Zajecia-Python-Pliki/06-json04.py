# Zapis danych do istniejącego pliku json
import json

data_add_file = '''{"imie": "Jan", "wiek": 30, "miasto": "Warszawa"}'''

# odczytaj plik
with open('dane.json', 'r', encoding='utf-8') as file_json_r:
    data_json = json.load(file_json_r)
print(data_json)

# połącz dane
data_add_file_json = json.loads(data_add_file)

data_json["new_user"] = data_add_file_json
print(data_json)

# zapisz dane do pliku
with open('dane.json', 'w', encoding="utf-8") as file_json_w:
    json.dump(data_json, file_json_w, ensure_ascii=False, indent=4)
