soma=0
soma2=0
for i in range(1,3):
    nome=str(input("digite seu nome:"))
    end=str(input("digite seu endereço:"))
    valor=float(input("dgite seu valor de compra:"))
    if(valor<=50.000):
        bonus=valor*1.10
        print(bonus)
    if(valor>50.000):
        bonus=valor*1.15
        print(bonus)