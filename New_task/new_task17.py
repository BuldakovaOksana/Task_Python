# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

# numb=['2','5','3','4']
# with open('filetask17.txt','w') as data:
#     data.writelines(numb)
# data.close()

with open('filetask17.txt', 'r') as f:
    nums = f.read().splitlines()
    nums=list(map(int,nums))
print(nums)
n=8
list=[i for i in range(1,n) ]
    
print(list)   

def sum(list1,list2):
    res=1
    for i in list1:
         res*=list2[list1[i]]
         print(res)
    return res

print(sum(nums,list))         