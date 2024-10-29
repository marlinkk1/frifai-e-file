#Construir um algoritmo que receba cem números e informe a média e a soma entre os números positivos.
soma=0
n=0
for i in range(1,7):
    n1=int(input("insira um valor"))
    if(n1>0):        
        soma+=1
        n+=1
    if n>0:
        media=soma/i
        print("soma e positiva",soma)
        print("media e positiva",media)