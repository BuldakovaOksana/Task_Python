# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def fibonachi(k):
    a,b=1,1
    list=[]
    for i in range(k):
        list.append(a)
        a,b=b,a+b
    
    a,b=0,1    
    for i in range(k+1):
        list.insert(0,a)
        a,b=b,a-b    
    return list
print(fibonachi(8))        