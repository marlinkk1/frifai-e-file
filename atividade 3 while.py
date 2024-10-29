sc = 0
bh = 0 
rj=0
while True:
    cidade=str(input("digite a sua cidade: "))
    if cidade=='rj': 
        rj = rj + 1 
    if cidade=='bh': 
        bh = bh + 1 
    if cidade=='sc': 
        sc = sc + 1 
    if cidade=='fim':
        break
print("essas pessoas são do Rio de Janeiro", rj) 
print("essas pessoas são de Belo Horizonte", bh) 
print("essas pessoas são de Santa Cantarina", sc)