horas=int(input("me diga um horario:"))
def slowfordcria(horas):
    horas=horas%12
if(horas>12):
    print("P.M",horas,)
if(horas<12):
    print("A.M",horas,)