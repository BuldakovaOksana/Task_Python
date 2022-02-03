# 14. Подсчитать сумму цифр в вещественном числе.


def sum(n):
    result=0
    st_n=str(n)
    for i in st_n:
        if i!='.':
            result += int(i)
    return result 

print(sum(1552.354))    
