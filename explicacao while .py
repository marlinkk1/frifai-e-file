contador=0
i=0
while(i<3):
    idade=int(input("iforme sua idade:"))
    altura=float(input("informe sua altura:"))
    peso=float(input("informe seu peso:"))
    if(idade>50):
        contador+=1
print(contador)