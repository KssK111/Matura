# Pobranie danych z pliku json
import json


with open('dane.json', 'r') as file_json:
   data_file_json = json.load(file_json)

print(data_file_json)
print(type(data_file_json))
print(data_file_json["imie"])
print(data_file_json["umiejetnosci"][0])
print(data_file_json["umiejetnosci"][0]["poziom"])

for key, value in data_file_json.items():
   print(f"{key} = {value}")