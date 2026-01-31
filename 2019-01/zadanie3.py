#3.2
ciag = [3,6,1,8,2,5,3,2,5,1,4,8,9,6]
n = len(ciag)
if 1 not in ciag:
    dlugosc = 0
    print(f"Długość najdłuższego podciągu = {dlugosc}")
else:
    obecna = 1
    for liczba in ciag[ciag.index(1) + 1:]:
        if liczba == obecna + 1:
            obecna += 1
    dlugosc = obecna
    print(f"Długość najdłuższego podciągu = {dlugosc}")

#3.1
ciagi = [[5,7,4,1,6,2,3,4,7,3,8,4,5,3,5], [6,7,3,7,4,9,1,6,4,2,6,4], [9,8,7,6,5,4,3,2,1]]
for ciag in ciagi:
    n = len(ciag)
    if 1 not in ciag:
        dlugosc = 0
        print(f"{ciag} - {dlugosc}")
    else:
        obecna = 1
        for liczba in ciag[ciag.index(1) + 1:]:
            if liczba == obecna + 1:
                obecna += 1
        dlugosc = obecna
        print(f"{ciag} - {dlugosc}")