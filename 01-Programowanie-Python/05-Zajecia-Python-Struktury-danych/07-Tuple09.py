# Zadanie.
# Przechowywanie informacji o użytkownikach. Utwórz tuple
# dla każdego użytkownika, zawierający jego imię, nazwisko, wiek itp.

uzytkownik1 = ("Jan", "Kowalski", 30)
uzytkownik2 = ("Anna", "Nowak", 25)
print("Informacje o użytkowniku 1:", uzytkownik1)
print("Informacje o użytkowniku 2:", uzytkownik2)

T = [2, 10, 4, 11, 5, 16, 9]

for i in range(len(T) - 1):
    if T[i] < T[i + 1]:
        if T[i] % T[i + 1] != 0:
            T[i], T[i + 1] = T[i + 1], T[i]

print(T)