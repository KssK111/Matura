# Zadanie. Zamiana jednostek
# Napisz funkcję konwertuj_jednostki(liczba, jednostka_z, jednostka_na),
# która zamienia liczbę z jednej jednostki na inną (np. metry na kilometry).

def konwertuj_jednostki(liczba, jednostka_z, jednostka_na):
    if jednostka_z == jednostka_na:
        return liczba
    if jednostka_z == 'cm':
        if jednostka_na == 'metr':
            return liczba*0.01
        elif jednostka_na == 'km':
            return liczba*0.00001
        elif jednostka_na == 'mile':
            return liczba*0.0000062137
    if jednostka_z == 'metr':
        if jednostka_na == 'cm':
            return liczba*100
        elif jednostka_na == 'km':
            return liczba*0.001
        elif jednostka_na == 'mile':
            return liczba*0.00062137
    if jednostka_z == 'km':
        if jednostka_na == 'cm':
            return liczba * 100000
        elif jednostka_na == 'metr':
            return liczba*1000
        elif jednostka_na == 'mile':
            return liczba*0.62137
    if jednostka_z == 'mile':
        if jednostka_na == 'cm':
            return liczba*160934
        elif jednostka_na == 'metr':
            return liczba*1609.34
        elif jednostka_na == 'km':
            return liczba*1.60934
    return "Nieprawidłowe jednostki. Obsługiwane jednostki to [cm, metr, km, mile]."


liczba = int(input("Podaj liczbę: "))
jednostka_z = input("Podaj jednostkę z jakiej mamy zmieniać[cm, metr, km, mile]: ")
jednostka_na = input("Podaj jednostkę z jakiej mamy zmieniać[cm, metr, km, mile]: ")

print(liczba, "[", jednostka_z, "]=", konwertuj_jednostki(liczba, jednostka_z, jednostka_na), "[", jednostka_na, "]",)

