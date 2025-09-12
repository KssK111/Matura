# slowniki
# dict = {klucz1: wartosc, klucz2: wartosc}
dict = {'jpg': 'image', 'gif': 'image', 'zip': 'archive'}

print(dict['jpg'])
print(dict)
dict['jpg'] = 'nowa wartość'
print(dict)
dict.update({'png': 'image'})
print(dict)
w = dict.copy()
lista = []
for i in dict:
    print(i, " - ", lista.append(dict[i]))
print(lista)
print('w:', w)
dict.clear()
print(dict)

# nowy slowanik z konatkami w formie imie : telefon
ksiazka_tel = {'Jan': 123456789, 'Tom': 654987132, 'Ola': 658987147}
for imie in ksiazka_tel:
    print(imie, ksiazka_tel[imie])

# dodać nowy nową osobą i numer
ksiazka_tel.update({'Ela': 458745874})

# dodac nową osobę i numer podany przez uzytkownika
imie = input("Podaj imię: ")
numer = int(input("Podaj nr telefonu: "))
ksiazka_tel.update({imie: numer})
print(ksiazka_tel)

del ksiazka_tel['Tom']
print(ksiazka_tel)