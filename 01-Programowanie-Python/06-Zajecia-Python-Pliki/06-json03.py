# Zapis danych do nowego pliku json
import json

data_ada_file = {
   "imie": "Jan", 
   "wiek": 30, 
   "miasto": "Warszawa"
}

with open('new_file.json', 'w', encoding="utf-8") as file_json:
   json.dump(data_ada_file, file_json, ensure_ascii=False, indent=4)
