import pygame
import sys

pygame.init()

tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
largura, altura = tela.get_size()

fonte = pygame.font.SysFont("Arial", 40)

progresso = 0

clock = pygame.time.Clock()

while True:
    tela.fill((10,10,10))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # texto
    txt = fonte.render(f"Atualizando sistema... {int(progresso)}%", True, (255,255,255))
    tela.blit(txt, (largura//2 - txt.get_width()//2, altura//2 - 50))

    # barra
    pygame.draw.rect(tela, (50,50,50), (largura//2-200, altura//2+20, 400, 20))
    pygame.draw.rect(tela, (0,200,255), (largura//2-200, altura//2+20, 4*progresso, 20))

    # lógica fake
    if progresso < 100:
        if progresso < 20:
            progresso += 0.5
        elif progresso < 80:
            progresso += 0.2
        else:
            progresso += 0.05

    pygame.display.flip()
    clock.tick(60)