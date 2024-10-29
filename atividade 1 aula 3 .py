#Escreva um programa que receba trêsnotas, mostre a média aritmética delas e informe se o aluno foi aprovado oureprovado. Nota para ser aprovado deve ser igual ou maior que 7.
n1=float(input("fale sua nota:"))
n2=float(input("fale sua segunda nota:"))
n3=float(input("fala sua terceira nota:"))
soma=(n1+n2+n3)/3
print(soma)
if(soma>=7):
    print("nao fez mais que sua obrigação")
else:
    print("po cara voce não passou")