nome=str(input("informe seu nome: "))
len=len(nome)
if (len>3):
 idade=int(input("informe sua idade: "))
if (idade>0) and (idade<150):
 salario=float(input("informe o valor que vc ganha: "))
if (salario>0):
 sexo=str(input("qual e seu sexo F ou M: "))
if (sexo=="f") or (sexo=="m"):
 civil=str(input("digite seu estado civil com, solteiro,casado,viuvo e deixado: "))
if (civil=='solteiro') or ('casado') or ("viuvo") or ("deixado"):
    print("valido")
else:
    print("invalido")