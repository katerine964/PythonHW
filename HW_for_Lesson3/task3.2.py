#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д
import random
def input_list(num:int):
    if num<=0:
        print("Введите положительное число")
        return[]
    spisok=random.sample(range(1,100),num)
    return spisok
def list_of_couple(spisok:list):
    new_list=[]
    if len(spisok)%2==0:
        for i in range(len(spisok)//2):
            new_list.append(spisok[i]+spisok[len(spisok)-i-1])
    #return new_list
    else:
        for i in range(len(spisok)//2):
            new_list.append(spisok[i]+spisok[len(spisok)-i-1])
        new_list.append(spisok[len(spisok)//2])
    return new_list    
mas=input_list(int(input("Введите количество элементов списка: ")))
print(mas)
new_list=list_of_couple(mas)
print(new_list)
            
        