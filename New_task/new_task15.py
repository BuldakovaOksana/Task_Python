# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

from unittest import result


def products_of_numbers(n):
    list=[]
    result=1
    for i in range(1,n+1):
        result*=i
        list.append(result)
    return list

print(products_of_numbers(4))        