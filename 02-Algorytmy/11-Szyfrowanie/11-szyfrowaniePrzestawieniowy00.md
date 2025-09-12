# Szyfr przestawieniowy

Szyfr przestawieniowy (ang. transposition cipher) to metoda szyfrowania, 
w której znaki wiadomości są przemieszczane według określonego schematu, 
bez zmiany ich tożsamości. W przeciwieństwie do szyfrów podstawieniowych 
(gdzie litery są zastępowane innymi literami), tutaj litery pozostają te same, 
ale ich kolejność zostaje zmieniona.

Przykład szyfru przestawieniowego – **Szyfr Kolumnowy** 

Za pomocą klucza tekstowego lub liczby ustalonej szyfrujemy wiadomość jawną: `TAJNEHASLO`

Za pomocą liczby, która ustala nam ilość kolumn. 
Dopisujemy ewentualnie dowolne znaki, jeśli długość 
wiadomości nie dzieli się przez długość klucza, 
np.: # lub spacje.
```
liczba = 3
Kolumny: 1 2 3
Znaki:   T A J
Znaki:   N E H
Znaki:   A S L
Znaki:   O # #
```
Odczytujemy znaki kolumnami 1-3, szyfrogram: TNAOAES#JHL#

Numerujemy litery klucza alfabetycznie:
```markdown
K = 1
O = 2
T = 3
```
Czyli kolejność kolumn to: T (1), K (2), O (3)

Układamy wiadomość w wiersze pod kluczem:
```markdown
 K  O  T
---------
 T  A  J
 N  E  H
 A  S  L
 O
```
(Dopisujemy ewentualne puste znaki, jeśli długość wiadomości nie dzieli się przez długość klucza)

Odczytujemy kolumny w kolejności alfabetycznej liter klucza (1->2->3 -> K->O->T):
```markdown
K: T N A O  
O: A E S  
T: J H L  
```
Szyfrogram: TNAO AES JHL