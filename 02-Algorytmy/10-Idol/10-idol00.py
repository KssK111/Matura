from random import randint

def lista(x):
    l = []
    for i in range(x):
        tmp = []
        for j in range(x):
            if i == j:
                tmp.append('x')
            else:
                tmp.append(randint(0, 1))
        l.append(tmp)
    return l


A = lista(2)
for i in A:
    print(i)
    print(i.count(1))


