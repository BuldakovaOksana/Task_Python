# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

from calendar import weekday


list=[None, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('Введите число от 1 до 7')
a=int(input())
def Work_or_weekend_day(a):
    if a>0 and a<=5:
        print('Work day')
    elif a>=6 and a<=7:
        print('weekday')    

Work_or_weekend_day(a)        

print(list[a])