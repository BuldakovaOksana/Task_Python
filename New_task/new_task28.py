# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
from cmath import sqrt
import math

def find_square(a,b,c):
    D=b**2-4*a*c
    res=[]
    if D<0:
        res.append('нет корней')
    if D==0:
        x1=-b/(2*a)    
        res.append(x1)
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        res.append(int(x1))
        x2=(-b-math.sqrt(D))/(2*a)
        res.append(int(x2))
    return res 
print(find_square(1,-4,3))    