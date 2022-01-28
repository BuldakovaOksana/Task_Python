# Найти максимальное из пяти чисел

from random import randint
lst = [randint(1, 10) for i in range(5)]
print(lst)
def Max_number(lst):
    max=lst[0]
    for i in range(len(lst)):
        if lst[i]>max:
            max=lst[i]
    return max

print(Max_number(lst))