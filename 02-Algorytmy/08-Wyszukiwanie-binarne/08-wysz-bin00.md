# Wyszukiwanie binarne

## Opis algorytmu

Wyszukiwanie binarne to wydajny algorytm do znajdowania elementu w posortowanej liście. Działa na zasadzie dzielenia
listy na pół w każdym kroku, aż do znalezienia poszukiwanego elementu lub stwierdzenia, że elementu nie ma w liście.

Jednym z najczęstszych sposobów wykorzystania **wyszukiwania binarnego** jest znalezienie elementu w tablicy. Przykładowo,
katalog gwiazd Tycho-2 zawiera informacje na temat jasności 2 539 913 gwiazd w naszej galaktyce. Załóżmy, że chcesz
przeszukać ten katalog w poszukiwaniu konkretnej gwiazdy, na podstawie nazwy gwiazdy. Jeżeli program ten miałby zbadać
każdą gwiazdę w katalogu począwszy od pierwszej, korzystając z algorytmu o nazwie **wyszukiwanie liniowe**, komputer w
najgorszym wypadku musiałby zbadać wszystkie 2 539 913 gwiazd, aby znaleźć gwiazdę, której szukasz. Jeżeli katalog ten
byłby posortowany alfabetycznie po nazwie gwiazdy, algorytm wyszukiwania binarnego nie musiałby zbadać więcej niż 22
gwiazdy, nawet w najgorszym wypadku.

### Dzięki tej metodzie ilość czas działania algorytmu wynosi:

`O(log n )`

## Działanie algorytmu

### Uwagi:
Lista musi być posortowana, w przeciwnym razie algorytm nie zadziała poprawnie. 


1. Ustalamy początek i koniec przedziału poszukiwań.
2. Znajdujemy środek przedziału instrukcją:
    `pivot = (poczatek + koniec) // 2`
3. Porównujemy wartość w środku z szukaną wartością:
   * Jeśli wartość w środku jest równa szukanej, zwracamy jej indeks. 
   * Jeśli wartość w środku jest większa od szukanej, kontynuujemy poszukiwanie w lewej części przedziału.
   * Jeśli wartość w środku jest mniejsza, przeszukujemy prawą część przedziału.
4. Proces powtarzamy aż do znalezienia elementu lub wyczerpania przedziału.
5. Jeśli element nie zostanie znaleziony algorytm zwraca `-1`.

## Rekurencyjna wersja

```commandline
def wyszukiwanie_binarne(lista, element, pocz=0, kon=None):
    if kon is None:
        kon = len(lista) - 1
    
    if pocz > kon:
        return -1  # Element nie został znaleziony
    
    srodek = (pocz + kon) // 2
    if lista[srodek] == element:
        return srodek
    elif lista[srodek] > element:
        return wyszukiwanie_binarne(lista, element, pocz, srodek - 1)
    else:
        return wyszukiwanie_binarne(lista, element, srodek + 1, kon)
```

## Iteracyjna wersja

```commandline
def wyszukiwanie_binarne_iter(lista, element):
    pocz = 0
    kon = len(lista) - 1
    
    while pocz <= kon:
        srodek = (pocz + kon) // 2
        if lista[srodek] == element:
            return srodek
        elif lista[srodek] > element:
            kon = srodek - 1
        else:
            pocz = srodek + 1
    
    return -1  # Element nie został znaleziony
```


## Zadania

1. Znajdź element w posortowanej liście przy użyciu wyszukiwania binarnego `08-wysz-bin01.py`. 
2. Zwróć indeks szukanego elementu w liście, jeśli istnieje.
3. Zwróć True/False, czy dany element istnieje w liście.
4. Zaimplementuj wyszukiwanie binarne rekurencyjnie.
5. Zaimplementuj wyszukiwanie binarne iteracyjnie.
    

6. Zdefiniuj listę z duplikatami oraz zwróć pierwszy i ostatni indeks szukanego elementu w liście z duplikatami `08-wysz-bin04.py`.
7. Znajdź pierwszy element większy od danego X.
8. Znajdź ostatni element mniejszy od danego X. 
9. Znajdź najmniejszy element większy lub równy X.
10. Znajdź największy element mniejszy lub równy X.


11. W liście posortowanej znajdź indeks elementu większego niż 100.
12. W tablicy z 0 i 1 znajdź pierwszy indeks, gdzie pojawia się 1.
13. W posortowanej tablicy znajdź liczbę wystąpień danego elementu.
14. Dla dużego pliku danych znajdź, czy element X się w nim znajduje (symulacja).
15. Wygeneruj losową posortowaną listę i sprawdź, czy liczba Y w niej jest.
