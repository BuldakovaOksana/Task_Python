# 5. Написать программу вычисления значения функции y = f(a)


x = input()
x = int(x)
if x > 0:
    y = 2*x - 10
elif x == 0:
    y = 0
else:
    y = 2*abs(x) - 1
print(y)