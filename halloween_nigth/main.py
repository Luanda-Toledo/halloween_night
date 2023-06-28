import pygame, sys
from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
from constantes import *
from personajes.player import Player


# SUPERFICIE PRICIPAL (VENTANA)
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.init()

clock = pygame.time.Clock() # Obtenemos el tiempo

img_fondo = pygame.image.load("halloween_nigth/recursos/fondo/1_game_background/1_game_background.png")
img_fondo = pygame.transform.scale(img_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

player_one = Player(x = 0, y = 400, speed_walk = 4, speed_run = 8, gravity = 8, jump_power = 25, frame_rate_ms = 80, move_rate_ms = 40, jump_height = 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Cantidad de tiempo en milisegundos que paso desde que entre a while hasta que salimos
    delta_ms = clock.tick(FPS)
    ventana_principal.blit(img_fondo, img_fondo.get_rect())

    # player update - verificar como el player interactua con todo el nivel
    player_one.update(delta_ms)
    player_one.events(delta_ms,keys)
    player_one.draw(ventana_principal)

    # enemigos update
    # dibujar player
    # dibujar todo el nivel

    pygame.display.flip()
    ventana_principal.blit(img_fondo, img_fondo.get_rect())


 




