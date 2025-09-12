# Algorytm zachłanny (ang. greedy algorithm)
Algorytm zachłanny to metoda rozwiązywania problemów optymalizacyjnych, która w każdym kroku wybiera opcję, która wygląda najbardziej obiecująco na danym etapie (tzw. lokalnie optymalny wybór) z nadzieją, że doprowadzi to do rozwiązania globalnie optymalnego.
## Główne cechy algorytmu zachłannego:
### Decyzje krokowe:
* Algorytm działa krok po kroku, podejmując kolejne decyzje w oparciu o lokalną optymalność.
### Nieodwracalność wyborów:
* Raz podjęte decyzje nie są zmieniane (brak cofania).
### Prostota:
* Zazwyczaj jest łatwiejszy do zaimplementowania i szybszy niż bardziej złożone podejścia, takie jak programowanie dynamiczne.
### Nie zawsze optymalne rozwiązanie:
* Algorytmy zachłanne działają poprawnie i znajdują rozwiązanie optymalne tylko dla pewnych klas problemów, w których występuje tzw. własność optymalnej struktury (np. problemy z własnością greedy-choice).

## Zadania

1. Napisz algorytm, ile zostało nominałów kasie po wydaniu n-kwoty reszty. 
    W kasie są następujące nominały: [100,50,20,10,5,2,1] oraz następująca ilość nominałów: [5,10,3,2,5,2,2].
2. Napisz algorytm, czy można wydać resztę zgodnie ze specyfiakcją zadania 1.
3. Napisz modyfikację algorytmu z zadania 1, sprawdzające jakich nominałów brakuje, aby wydać resztę. Wyświetl brakujące nominały.