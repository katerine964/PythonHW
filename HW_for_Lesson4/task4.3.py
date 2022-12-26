#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
import random
def input_list(num:int):
    if num<=0:
        print("Введите положительное число")
        return[]
    spisok=[random.randint(0,10) for i in range(num)]
    return spisok
def func(lst:list):
    newlst=[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                break
        else:
            newlst.append(lst[i])
    return newlst
mas=input_list(int(input("Введите количество элементов списка: ")))
print(mas)
new_list=func(mas)
print(new_list)
