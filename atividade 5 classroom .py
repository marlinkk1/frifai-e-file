#Faça um algoritmo que receba o peso, a idade e a altura de cem pessoas, 
#calcule e informe os valores de: maior peso, menor peso, maior
#altura, menor altura, maior idade e menor idade deste grupo de pessoas.
posi=0
nega=0
for i in range(5):
    v=int(input("diga um numero:"))
    if v>nega:
        posi+=1
    else:
        nega+=1
print("a quatidade de negativos{}".format(nega))