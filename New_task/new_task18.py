
# Реализовать алгоритм перемешивания списка. 
from random import randint
list=[i for i in range(10)]
print(list)

def mix(list):
    a=0
    for i in list:
        j=randint(0,len(list)-1)
        a=list[i]
        list[i]=list[j]
        list[j]=a
    return list
print(mix(list))        