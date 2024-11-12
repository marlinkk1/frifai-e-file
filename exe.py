import pygame
import random

# Inicializando o pygame
pygame.init()

# Configuração da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Tigrin")

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Definindo o jogador e o tigrin
tamanho_jogador = 50
tamanho_tigrin = 50

# Jogador
jogador_x = LARGURA // 2
jogador_y = ALTURA // 2
velocidade_jogador = 5

# Tigrin
tigrin_x = random.randint(0, LARGURA - tamanho_tigrin)
tigrin_y = random.randint(0, ALTURA - tamanho_tigrin)
velocidade_tigrin = 3

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, AZUL, (x, y, tamanho_jogador, tamanho_jogador))

# Função para desenhar o tigrin
def desenhar_tigrin(x, y):
    pygame.draw.rect(tela, VERMELHO, (x, y, tamanho_tigrin, tamanho_tigrin))

# Função para checar colisão
def checar_colisao(jogador_x, jogador_y, tigrin_x, tigrin_y):
    if (jogador_x < tigrin_x + tamanho_tigrin and
        jogador_x + tamanho_jogador > tigrin_x and
        jogador_y < tigrin_y + tamanho_tigrin and
        jogador_y + tamanho_jogador > tigrin_y):
        return True
    return False

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(BRANCO)

    # Captura de eventos (teclas pressionadas, fechamento da janela, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade_jogador
    if teclas[pygame.K_UP]:
        jogador_y -= velocidade_jogador
    if teclas[pygame.K_DOWN]:
        jogador_y += velocidade_jogador

    # Impedindo que o jogador saia da tela
    if jogador_x < 0:
        jogador_x = 0
    if jogador_x > LARGURA - tamanho_jogador:
        jogador_x = LARGURA - tamanho_jogador
    if jogador_y < 0:
        jogador_y = 0
    if jogador_y > ALTURA - tamanho_jogador:
        jogador_y = ALTURA - tamanho_jogador

    # Movimento do tigrin
    if tigrin_x < jogador_x:
        tigrin_x += velocidade_tigrin
    elif tigrin_x > jogador_x:
        tigrin_x -= velocidade_tigrin
    if tigrin_y < jogador_y:
        tigrin_y += velocidade_tigrin
    elif tigrin_y > jogador_y:
        tigrin_y -= velocidade_tigrin

    # Verificar se o tigrin capturou o jogador
    if checar_colisao(jogador_x, jogador_y, tigrin_x, tigrin_y):
        print("Você foi pego pelo Tigrin!")
        rodando = False

    # Desenhar o jogador e o tigrin
    desenhar_jogador(jogador_x, jogador_y)
    desenhar_tigrin(tigrin_x, tigrin_y)

    # Atualizar a tela
    pygame.display.update()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(30)

# Fechar o pygame
pygame.quit()