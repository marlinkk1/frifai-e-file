gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
alunos = []
while True:
    acertos = 0
    print("Responda as questões da prova:")    
    for i in range(10):
        while True:
            resposta = str(input("Questão {} (A/B/C/D/E): ".format(i + 1)))
            if (resposta in ['A', 'B', 'C', 'D', 'E']):
                break
            print("Resposta inválida. Tente novamente.") 
        if (resposta==gabarito[i]):
            acertos += 1
    alunos.append(acertos)
    print("Sua nota: {} pontos.".format(acertos))
    continuar = str(input("esse gabarito vai ser usado novamente? (s/n): "))
    if continuar != 's':    
        break
if alunos:
    maior = alunos[0]
    menor = alunos[0]
    totalalunos = 0
    soma_notas = 0
    for nota in alunos:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        soma_notas += nota
        totalalunos += 1
    media = soma_notas / totalalunos
    print("Resultados finais:")
    print("Maior acerto: {}".format(maior))
    print("Menor acerto: {}".format(menor))
    print("Total de alunos que utilizaram o sistema: {}".format(totalalunos))
    print("Média das notas da turma: {:.2f}".format(media))