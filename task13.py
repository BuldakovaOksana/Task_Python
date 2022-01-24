# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

import random
a=random.randint(10,99)
b=random.randint(1,9)
print(a,b)
if a%b==0:
    print(True)
else:
    print(a%b)    
