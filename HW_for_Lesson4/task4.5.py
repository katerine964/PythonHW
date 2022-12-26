
f=open("polly.txt")
fd=f.readline()
pol=''
for i in range(len(fd)-3):
    pol+=f'{fd[i]}'
pol+='+ '
h=open("polly_2.txt")
hd=h.readline()
for i in range(len(hd)):
    pol+=f'{hd[i]}'
with open('Task4.5.txt', 'w') as finpoly:
            finpoly.write(pol)

