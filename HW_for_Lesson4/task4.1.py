#Вычислить число c заданной точностью d
from decimal import Decimal
from decimal import getcontext
N=float(input("введите число: "))
a=float(input("введите точность: "))
getcontext().prec = len(str(a))-1-len(str(int(a)))+len(str(int(N)))
print(Decimal(N)*Decimal(1))
     