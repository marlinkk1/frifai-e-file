votoembranco=0
votonulo=0
meunego=0
maria=0
joao=0
jose=0
i=0
while(i<6):
    candidato=int(input("digite o numero do seu candidato"))
    if(candidato==1):
        jose=jose+1
    if(candidato==2):
        joao=joao+1
    if(candidato==3):
        maria=maria+1
    if(candidato==4):
        meunego=meunego+1
    if(candidato==5):
        votonulo=votonulo+1
    if(candidato==6):
        votoembranco=votoembranco+1
    if(candidato>7):
        i=7
        print("invalido")
        break
soma1=votonulo/(jose+joao+maria+meunego)*100
soma2=votoembranco/(jose+joao+maria+meunego)*100

