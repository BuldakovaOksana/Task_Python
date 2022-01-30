# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

def Quarter_of_coordinate(x,y):
    if x>0 and y>0:
        print('First quarter')
    elif x<0 and y>0:
        print('Second quarter')    
    elif x<0 and y<0:
        print('Third quarter')   
    elif x>0 and y<0:
        print('Fourth quarter')    

Quarter_of_coordinate(-5,-8)         
