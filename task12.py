# 12. Удалить вторую цифру трёхзначного числа

import random
a=random.randint(100,999)
print(a)
def Delet_second_number(a):
    b=a%10
    c=a//100
    return c*10+b

print(Delet_second_number(a))