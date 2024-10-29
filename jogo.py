import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Melhore sua Mira!")

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)

# Variáveis do jogo
score = 0
tempo_jogo = 30  
# Tempo em segundos
tempo_inicial = time.time()
target_radius = 30

# Função para desenhar um alvo
def desenhar_alvo(x, y):
    pygame.draw.circle(screen, verde, (x, y), target_radius)

# Loop principal do jogo
running = True
while running:
    screen.fill(branco)
    
    # Verifica o tempo de jogo
    if time.time() - tempo_inicial > tempo_jogo:
        print(f"Tempo esgotado! Você acertou {score} alvos.")
        running = False
        continue
    
    # Gera a posição do alvo
    target_x = random.randint(target_radius, largura - target_radius)
    target_y = random.randint(target_radius, altura - target_radius)

    desenhar_alvo(target_x, target_y)

    pygame.display.flip()
    pygame.time.delay(1000)  # Delay de 1 segundo entre alvos

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (target_x - target_radius < mouse_x < target_x + target_radius) and \
               (target_y - target_radius < mouse_y < target_y + target_radius):
                score += 1
                print(f"Acertou! Pontuação: {score}")

pygame.quit()