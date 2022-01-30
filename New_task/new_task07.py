# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x=1
y=1
z=0
print( not(x or y or z)== (not x and not y and not z))