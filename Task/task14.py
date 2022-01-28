# 14. Найти третью цифру числа или сообщить, что её нет

import random
a=random.randint(1,999)
print(a)
def Find_third_number(a):
    if a//100==0:
        return False
    else:
        return a%10
print(Find_third_number(a))          
