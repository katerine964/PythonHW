# Задайте список из произвольных вещественных чисел, количество задаёт пользователь. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
def input_list(num:int):
    if num<=0:
        print("Введите положительное число")
        return[]
    spisok=[]
    for i in range(num):
        spisok.append(round(random.uniform(1,100),2))
    return spisok
def list_drob_chast(spisok:list):
    new_spisok=[]
    for i in range(len(spisok)):
        new_spisok.append(round(spisok[i]%1,2))
    return new_spisok
spisok=input_list(5)
print(spisok)
new_spisok=list_drob_chast(spisok)
print(new_spisok)
max= max(new_spisok)
min= min(new_spisok)
razn=(max-min)
print(razn) 

#new_spisok=input_list(int(input("Введите количество элементов сприска: ")))  
#print(new_spisok)
#drob_spisok=list_drob_chast(new_spisok)
#print(drob_spisok)
#max= max(drob_spisok)
#print(list_drob_chast(new_spisok))
