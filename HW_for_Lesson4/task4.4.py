#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
import random 
 
k= int(input("Введите натуральную степень k:"))
n=int(input("Сколько раз нужно сформировать многочлен многочлен (не менее 3х): "))
 
def koeffs (k,n:int):
    if k<=0:
        print("степень должна быть натуральной")
    elif n<3:
        print("количество многочленов должно быть не меньше 3х")
    list=[[random.randint(1, 10) for j in range(k+1)] for i in range(n)]
    return list
def polinom(ls:list):
    wr = ''
    for i in range(len(ls)):
        if i != len(ls) - 1 and ls[i] != 0 and i != len(ls) - 2:
            wr += f'{ls[i]}x^{len(ls) - i - 1}'
            if ls [i + 1] != 0:
                wr += ' + '
        elif i == len(ls) - 2 and ls[i] != 0:
            wr += f'{ls[i]}x'
            if ls[i + 1] != 0:
                wr += ' + '
        elif i == len(ls) - 1 and ls[i] != 0:
            wr += f'{ls[i]} = 0   \n'
        elif i == len(ls) - 1 and ls[i] == 0:
                wr += ' = 0   \n'
    return wr
def output_polinoms(lst:list):
    with open('Task4.4.txt', 'w') as pr:
        pr.write("")
    for i in range(len(lst)):
        with open('Task4.4.txt', 'a') as poly:
            poly.write(polinom(lst[i]))
mylist=koeffs(k,n)
output_polinoms(mylist)


