# Составить список простых множителей натурального числа N

n = 100

def task31 (n):
    i = 2
    array = []
    while n != 1: 
        if n % i == 0:
            array.append(i) #3
            n = n / i
            i = 2
        else: 
            i += 1
    return (array)

print (task31 (100))