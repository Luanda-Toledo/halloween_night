import pygame, sys
from constantes import *
from players.player import Player


# SUPERFICIE PRICIPAL (VENTANA)
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock() # Obtenemos el tiempo

img_fondo = pygame.image.load("halloween_nigth/recursos/fondo/1_game_background/1_game_background.png")
img_fondo = pygame.transform.scale(img_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

player_one = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    # player update - verificar como el player interactua con todo el nivel
    player_one.update()
    player_one.draw(ventana_principal)

    # enemigos update
    # dibujar player
    # dibujar todo el nivel

    pygame.display.flip()
    ventana_principal.blit(img_fondo, img_fondo.get_rect())


    delta_es = clock.tick(FPS) # Cantidad de tiempo en milisegundos que paso desde que entre a while hasta que salimos




