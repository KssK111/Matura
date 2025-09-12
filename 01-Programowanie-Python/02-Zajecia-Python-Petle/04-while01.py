# Zadanie
# Logowanie się do sysytemy określoną ilość razy

login_baza = "admin"
haslo_baza = "1234admin4321"

zalogowano = False
i = 1
while i <= 3 and zalogowano == False:
    login = input("Login: ")
    haslo = input("Hasło: ")
    if login == login_baza and haslo == haslo_baza:
        print("Logowanie prawidłowe")
        zalogowano = True
    else:
        print("Błąd logowania! Pozostało ", 3-i, " prób")
        i = i + 1
if not zalogowano:
    print("Konto zablokowano.")