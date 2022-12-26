#Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
import random
def input_list(num:int):
    if num<=0:
        print("Введите положительное число")
        return[]
    spisok=random.sample(range(1,100),num)
    return spisok
def sum_nechet(spisok:list):
    sum=0
    for i in range(len(spisok)):
        if i%2==0:
            sum=sum+spisok[i]
    return sum
            
mas=input_list(int(input("Введите количество элементов списка: ")))
print(mas)
summa=sum_nechet(mas)
print(summa)