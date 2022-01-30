# 10. Найти расстояние между двумя точками пространства 

from math import *
def distance(x1, y1, x2, y2):
    c = sqrt((x2-x1)**2 + (y2-y1)**2)
    return c

print( distance(-1,3,6,2))