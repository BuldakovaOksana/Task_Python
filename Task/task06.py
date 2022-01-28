# Выяснить является ли число чётным
def Is_number_even(a):
    return a%2==0
from random import randint

a=randint(1,10)
print(a)
result=Is_number_even(a)
print(result)    