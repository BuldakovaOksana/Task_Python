# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
from datetime import datetime
list=[datetime.now().microsecond%10 for i in range(10)]
# def gen(list):
      
#     for i in list:
#         d=datetime.now().microsecond%100
#         list[i]=d
#     return list
print(list)