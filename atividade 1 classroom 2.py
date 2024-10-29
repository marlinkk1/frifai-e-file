#Construa um algoritmo que receba cinquenta números e mostre a média dos números que foram digitados.
soma=0
for i in range(1,51):
    valor=int(input("digite um valor"))
    soma=soma+valor
    print(soma)
media=soma/i
print(media)
