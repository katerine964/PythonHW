#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
a=int(input("Введите номер четверти: "))
if a==1:
    input ("x>0; y>0")
elif a==2:
    input ("x<0; y>0")
elif a==3:
    input ("x<0; y<0")
elif a==4:
    input ("x>0; y<0")
else:
    input ("Нет такой четверти")
    
    