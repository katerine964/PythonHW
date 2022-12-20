#Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
import random
from random import randint, randrange
mas=[2,5,7,9,11,23,37,41,55,63]
N=len(mas)
#a=[randrange(0,N) for i in range(N)]
#print(a)
index=[]
while len(index)<N:
    x=randint(0,(N-1))
    if x not in index:
        index.append(x)
newmas=[1]*len(mas)
for i in range(len(mas)):
    newmas[i]=mas[index[i]]
print("Изначальный список: ", mas)
print("Перемешанный список: ",newmas)


