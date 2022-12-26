#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
def prost_mnoj(num:int):
    if num<=0:
        print("Введите натуральное число: ")
        return[]
    i=2
    mnoj=[]
    while i*i<=num:
        while num%i==0:
            mnoj.append(i)
            num=num//i
        i=i+1
    if num>=2:
        mnoj.append(num)
    return mnoj
       
N = int(input("Введите число: "))
print(prost_mnoj(N))
