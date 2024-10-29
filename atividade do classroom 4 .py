n=int(input("diga o seu codigo:"))
venda1=int(input("diga seu numero de vendas:"))
if(venda1<100):
    print("vish pae se lascou ta sem comissão, faz o L")
venda2=6/100*venda1
if(venda1>100)and(venda1<=350):
    print("sua comissão é de{}".format(venda2))
venda3=10/100*venda1
if(venda1>350):
    print("sua comissão é de {}".format(venda3))