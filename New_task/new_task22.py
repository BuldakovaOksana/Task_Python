# Найти сумму чисел списка стоящих на нечетной позиции
from random import randint

list=[randint(1,10) for i in range(10)]
print(list)

def sum(list):
    sum=0
    count=0
    for i in list:
        if count%2==1:
            sum+=i
        count+=1
    return sum


print(sum(list))