# sito Eratostenesa

a = 2
b = 100
lista = [i for i in range(a, b)]

for i in range(len(lista)):
  if lista[i] != 0:
    for j in range(i+lista[i], b - a, lista[i]):
        lista[j] = 0
print(lista)

liczbypierwsze = [ i for i in lista if i > 0 ]
print(liczbypierwsze)


# Funkcja  - sito Eratostenesa
def sito(b):
    a = 2
    lista = [i for i in range(a, b)]
    for i in range(len(lista)):
      if lista[i] != 0:
        for j in range(i+lista[i], b - a, lista[i]):
            lista[j] = 0
    return [ i for i in lista if i > 0 ]


print(sito(100))

