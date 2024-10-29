soma=0
s=0
n=0
n2=0
i=0
while(i<3):
    d=int(input("informe um numero:"))
    if (d>0) and (d<25):
        soma=soma+1
    if(d>26) and (d<50):
        s=s+1
    if(d>51) and (d<75):
        n=n+1
    if(d>76) and (d<100):
        n2=n2+1 
    if(d<0):
        i=4
print("os valores estão entre 0 e 25",soma)
print("os valores estão entre 26 e 50",s)
print("os valores estão entre 51 e 75",n)
print("os valores estão entre 76 e 100",n2)