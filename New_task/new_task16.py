# Задать список из n чисел последовательности (1+1/n)n и вывести на экран их сумму
from fractions import Fraction
def sequence(n):
    list=[]
    r=0
    for i in range(1,n+1):
        r=(1+Fraction(1,i))**i
        list.append(r)
    return list

def sum(list):
    r=0
    for i in range(len(list)):
        r+=list[i]       
    return r
ls=sequence(5)
print(ls)
print(sum(ls))