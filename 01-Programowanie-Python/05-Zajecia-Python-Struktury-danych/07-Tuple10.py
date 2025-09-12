# deklaracja tupli
zm = 1,
print(zm)

# iteacja tupli
for i in zm:
    print(i)


# tupla jako argument funkcji
def funkcja(a = (0,0), b = (0,0)):
    return (a[1] + b[1]) * (a[0] + b[0])


print(funkcja((1,2), (4,5)))


# iteracja tupli zagniezdzonych
t = ((1,2,3), (4,5,6,7,8), (9,10,11,(10,(100,200,300),20,30),12,13,14,15))
def view_tuple(t):
    if type(t) in [tuple, list]:
        for items in t:
            view_tuple(items)
    else:
        print(t)

view_tuple(t)