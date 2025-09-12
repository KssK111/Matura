# Zadanie.
# Przechowywanie współrzędnych punktów. Utwórz tuple,
# w którym każdy element to para współrzędnych (x, y)
# reprezentująca punkty na płaszczyźnie tworzące trójkąt.
# Oblicz pole tego trójkąta.

from math import fabs
pkt = ((1, 2), (2, 1), (3, 1))
# Pole= 1/2 * fabs(x1*(y2-y3)+x2*(y3−y1)+x3*(y1−y2))
pole_trojkata = 0.5 * fabs(pkt[0][0]*(pkt[1][1]-pkt[2][1])+pkt[1][0]*(pkt[2][1]-pkt[0][1])+pkt[2][0]*(pkt[0][1]-pkt[2][1]))
print("Pole trójkąta o współrzędnych ", pkt, " wynosi :", pole_trojkata)