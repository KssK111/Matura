## Znajdujemy lidera

Algorytm `WYSZUKIWANIA LIDERA` nazywamy taki element zbioru n-elementowego, który występuje w tym zbiorze więcej niż n/2 razy.

#### Przykład:

Zbiór `[1, 2, 3, 1, 1, 4]`. `Liderem` tego zbioru jest liczba 1, ponieważ występuje ona 3 razy, co stanowi więcej niż połowę elementów zbioru (6).

#### Specyfikacja problemu
`Dane: A[0...n-1]` - tablica n liczb całkowitych

### Algorytm:

1. Zainicjuj zmienną kandydat na pierwszy element zbioru.
2. Zainicjuj zmienną licznik na 1.
3. Przeiteruj przez pozostałe elementy zbioru:
4. Jeśli element jest równy kandydatowi, zwiększ licznik o 1.
5. W przeciwnym razie zmniejsz licznik o 1.
6. Jeśli licznik jest większy od 0, to kandydat jest liderem.
7. W przeciwnym razie nie ma lidera w zbiorze.

### Implementacja w Pythonie:

```commandline

def znajdz_lidera(zbior):
  """
  Znajduje lidera w zbiorze.
  Argumenty:
    zbior: Sekwencja elementów.
  Zwraca:
    Lidera zbioru lub None, jeśli nie ma lidera.
  """
  kandydat = zbior[0]
  licznik = 1

  for element in zbior[1:]:
    if element == kandydat:
      licznik += 1
    else:
      licznik -= 1

  if licznik > 0:
    return kandydat

  return None

# Przykład użycia
zbior = [1, 2, 3, 1, 1, 4]
lider = znajdz_lidera(zbior)

if lider is not None:
  print(f"Liderem zbioru jest {lider}")
else:
  print("Zbiór nie ma lidera")
```
### Złożoność obliczeniowa:

Algorytm ma złożoność czasową O(n), gdzie n jest liczbą elementów w zbiorze.
