from os import remove

slownik = {}

for i in range(1, 11):
    slownik[i] = i ** 2

print(slownik)

for i in slownik.values():
    print(i, end="\t")
print()
for i in slownik.keys():
    print(i, end="\t")
print()
for i in slownik.items():
    print(i, end="\t")
print()
for i, j in slownik.items():
    print(i, j, end="\t")
print()
print(len(slownik))

suma = 0
for i in slownik.values():
    suma += i
print(suma / len(slownik))

d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())

new_item = {'d': 4}
d.update(new_item)
print(d)

tab = [1, 2, 3, 4, 5]
odd = {}
ind = 0
for i in tab:
    if i % 2 == 0:
        odd[ind] = i
        ind += 1
print(odd.values())
d = {'c': 1}
del d['c']
print(d)
