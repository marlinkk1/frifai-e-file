import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    # Escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    
    if escolha_usuario not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return jogar()  # Recomeça o jogo se a escolha for inválida
    
    # Escolha do computador
    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")
    
    # Lógica do jogo
    if escolha_usuario == escolha_computador:
        resultado = "Empate!"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"
    
    print(resultado)

# Iniciar o jogo
if __name__ == "__main__":
    jogar()