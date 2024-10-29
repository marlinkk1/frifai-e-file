#Escreva um algoritmo que receba 100 números, e conte quantos deles estão no intervalo 
#[10, 20] e quantos deles estão fora do intervalo, escrevendo estas informações.
soma=0
nota=0
for i in range(1,5):
    n=int(input("diga um numero:"))
    if 10>= n<=20:
        soma +=1
    else:
        nota+=1
print("numero entre 10,20",soma)
print("{} numeros fora do intervalo".format(nota))