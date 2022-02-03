# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

from random import randint, random

list=[randint(1,10) for i in range(9)]
print(list)

def multiplication(list):
    list2=[]
    l=len(list)
    if l%2==0:
        r=l//2
    else: r=l//2+1    
    for i in range(r):
        res=list[i]*list[l-1-i]
        list2.append(res)
    return list2
print(multiplication(list))