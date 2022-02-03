# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

st1='dfhjkghfdjhrnv,jhnmkdhf'
st2='r'

def Occurrences(st1,st2):
    count=0
    while st2 in st1:
        count+=1
        st1=st1[st1.find(st2)+1:]
    return count

print(Occurrences(st1,st2))        

