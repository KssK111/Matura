# Utwórz słownik gdzie kluczem jest unikatowe imię, a wartością długość imienia.
# Użytkownik podaje imiona aż do momentu wpisani pustego napisu (string)

imie = "a"
imiona = {}
while len(imie) > 0:
    imie = input("Podaj imię: ")
    # tworzymy element slownika
    if len(imie) > 0:
        imiona[imie] = len(imie)

    # if len(imie) == 0:
    #     continue
    # imiona[imie] = len(imie)
print(imiona)

# sprawdz czy podany klucz przez uzytkownika istnieje
klucz = input("Podaj szukany klucz")
if klucz in imiona:
    print(f"{klucz} istnieje w słowniku")
else:
    print(f"{klucz} brak klucza w słowniku")
