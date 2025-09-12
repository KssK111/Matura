# Algorytm szyfru Cezara

Jeden z najstarszych sposobów szyfrowania pochodzi od Juliusza Cezara, 
który szyfrował swoją korespondencję z Cyceronem. Sposób ten polegał na tym, 
że zamiast każdej litery pisał literę występującą w alfabecie trzy miejsca dalej. 
Tak więc, jeśli użyjemy dzisiejszego alfabetu łacińskiego

   `abcdefghijklmnopqrstuvwxyz`

to zamiast c będziemy pisać f, zamiast g piszemy j, zamiast y piszemy b. 
Alfabet traktujemy cyklicznie, tzn. po ostatniej literze z następuje ponownie litera a itd.

System kryptograficzny to sposób szyfrowania. W powyższym przykładzie polega on na tym, 
że zamiast danej litery alfabetu piszemy literę występującą w tym samym alfabecie określoną 
ilość miejsc dalej. System kryptograficzny polega tu na pisaniu litery stojącej k miejsc 
dalej, a liczba k jest kluczem. Szyfrowanie więc polega na wyborze algorytmu szyfrowania, 
zwanego systemem kryptograficznym i pewnych parametrów, od których ten algorytm 
jest zależny, nazywanych kluczem szyfrowania.

**Algorytm szyfru Cezara** (znany również jako szyfr przesuwający) to jeden z najprostszych 
i najstarszych szyfrów szyfrowania tekstu. 

## Opis działania algorytmu:

Szyfr Cezara polega na przesunięciu każdej litery tekstu jawnego o stałą liczbę pozycji 
w alfabecie.

### Kroki algorytmu:
```markdown
1. Wybierz klucz (przesunięcie) – np. k = 3.
2. Dla każdej litery w tekście jawnym:
3. Jeśli to litera (np. A–Z lub a–z), przesuń ją o k miejsc w prawo w alfabecie.
4. Jeśli przesunięcie wykracza poza ostatnią literę alfabetu, zacznij od początku (czyli alfabet działa cyklicznie).
5. Pozostałe znaki (np. cyfry, spacje, znaki interpunkcyjne) pozostają niezmienione.
```

### Przykład:
    Tekst jawny: ABC XYZ
    Przesunięcie: 3

### Szyfrowanie:
```markdown
A → D
B → E
C → F
X → A
Y → B
Z → C
```
Tekst zaszyfrowany: DEF ABC

### Deszyfrowanie:

Aby odszyfrować wiadomość, wystarczy przesunąć litery w lewo o tę samą liczbę pozycji (k), 
np. przy k = 3: 
```markdown
D → A, 
E → B, 
F → C, 
A → X
B → Y
C → Z
```

## Zalety i wady:

### Zalety:

Prosty w implementacji.
Działa bez potrzeby skomplikowanego sprzętu.

### Wady:

Bardzo łatwy do złamania – tylko 25 możliwych przesunięć.
Nie zapewnia realnego bezpieczeństwa we współczesnych systemach.



## Zadania

1. Szyfruj wiadomość z wejścia. Napisz program, który wczytuje od użytkownika tekst 
i liczbę jako klucz, a następnie wyświetla zaszyfrowany tekst. 
2. Złam szyfr Cezara (brute force). Dany jest zaszyfrowany tekst. Napisz program, 
który wypisze wszystkie możliwe 25 deszyfrowań (dla kluczy 1–25), aby ułatwić 
odgadnięcie tekstu jawnego.
3. Porównanie szyfru dla różnych kluczy. Napisz funkcję, która przyjmuje tekst 
i wypisuje, jak wygląda jego zaszyfrowanie dla kluczy od 1 do 10. 
4. Szyfrowanie tylko liter, ignorując inne znaki. Zmień funkcję szyfrującą tak, 
aby ignorowała cyfry, znaki interpunkcyjne i spacje (nie zmieniała ich), 
szyfrując tylko litery.
5. Szyfr Cezara z polskim alfabetem. Zmodyfikuj funkcję szyfrującą, 
aby obsługiwała polskie litery (ą, ć, ę, ł, ń, ó, ś, ź, ż) oprócz standardowych a–z.