# Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list=[1, 2, 3, 5, 1, 5, 3, 10]

def unique(li):
    uni_list=[]
    uni_list.append(set(li))
    return uni_list
    
print(unique(list))