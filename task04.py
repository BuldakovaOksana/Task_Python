# 4. Найти максимальное из трех чисел
def Find_max(a,b,c):
    max=a
    if b>a:
        max=b
    elif c>b:
        max=c 
    return max
print(Find_max(120,190,130))              