# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19



ls=[1.1, 1.2, 3.1, 5, 10.01]
li=[i for i in ls if type(i)==float]
li=list(map(lambda i: round(i%1,2), li))
print(li)

def res(list):
    for i in list:
        if type(i)==float:
           return max(list)-min(list)
            

print(res(li))
