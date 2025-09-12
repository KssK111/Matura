# Zadanie
# System logowania się.
# Sprawdzenie czy hasło i login jest prawidłowe.
# Wyswietl odpowiedni komunikat.

login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

tajnylogin = 'root'
tajnehaslo = 'abc123'

if login == tajnylogin and haslo == tajnehaslo:
    print("Tajna informacja.")
else:
    print("Błędny login lub hasło.")