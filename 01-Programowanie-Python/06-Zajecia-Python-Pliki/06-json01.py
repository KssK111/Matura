# pobranie danych zapisanych w zmiennej w formacie JSON
import json

data_json_var = '''{
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 30,
    "adres": {
        "ulica": "Kwiatowa",
        "numer": 15,
        "miasto": "Warszawa",
        "kod_pocztowy": "00-001"
    },
    "telefon": ["123-456-789", "987-654-321"],
    "email": "jan.kowalski@example.com",
    "zatrudniony": "True",
    "umiejetnosci": [
        {
            "nazwa": "Programowanie",
            "poziom": "zaawansowany"
        },
        {
            "nazwa": "Grafika komputerowa",
            "poziom": "średni"
        }
    ]
}'''

# json.loads() - odczytuje z ciągu znaków (zmiennej)
data = json.loads(data_json_var)
print(data)
print(type(data))
print(data["imie"])
print(data["umiejetnosci"][0])
print(data["umiejetnosci"][0]["poziom"])
