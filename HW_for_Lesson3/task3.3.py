#Напишите программу, которая будет преобразовывать десятичное число в двоичное.Без использования встроенной функции преобразования, без строк.
def del_na_2(num:int):
    num_list=[]
    while num>0:
        num_list.append(num%2)
        num=num//2
    return num_list
def razvorot(num_list:list):
    for i in range(len(num_list)//2):
        temp=num_list[i]
        num_list[i]=num_list[len(num_list)-i-1]
        num_list[len(num_list)-i-1]=temp
    return num_list
Num=int(input("Введите число:"))
print(*(razvorot(del_na_2(Num))))
            