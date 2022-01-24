# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
a=random.randint(10,100)
print(a)
b=a%10
c=a//10
def Find_max(b,c):
    max=b
    if c>b: max=c
    return max
print(Find_max(b,c))    