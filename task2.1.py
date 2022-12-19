n=float(input("введите вещественное число: "))
m=len(str (n))
sum=0
k=round(n*10**(m-2))
while k>0:
    sum=sum+k%10
    k=k//10
print("Сумма цифр числа ",n,"равна ",sum)