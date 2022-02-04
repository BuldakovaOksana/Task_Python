# 25. Написать программу преобразования десятичного числа в двоичное

from audioop import reverse


def conver(a):
    list=[]
    while a>0:
        list.append(a%2)
        a//=2
    list.reverse()
    return list
print(conver(20))      

