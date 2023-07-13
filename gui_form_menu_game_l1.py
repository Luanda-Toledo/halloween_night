import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from player import Player
from enemigos import EnemyZombie, EnemyMurcielago
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Coins
import time
from pygame import rect
from auxiliar import Auxiliar

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        #self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=5,y=0,w=160,h=60,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_boton2,on_click_param="form_menu_levels",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_shoot,on_click_param="form_menu_settings",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=450,y=10,w=200,h=40,color_background=None,color_border=None,image_background="recursos/nada.png",image_progress="recursos/images/gui/set_gui_01/Data/Elements/heart.png",value = 5, value_max=5)
        self.widget_list = [self.boton2, self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.datos_extraidos = Auxiliar.leer_json("nivel_uno.json")

        background_data = self.datos_extraidos["nivel_1"]["background_level_uno"][0]
        x = background_data.get("x")
        y = background_data.get("y")
        path = background_data.get("path")
        w = w
        h = h

        self.static_background = Background(x, y, w, h, path)

        player_data = self.datos_extraidos["nivel_1"]["player_uno"][0]
        x = player_data.get("x")
        y = player_data.get("y")
        speed_walk = player_data.get("speed_walk")
        speed_run = player_data.get("speed_run")
        gravity = player_data.get("gravity")
        jump_power = player_data.get("jump_power")
        frame_rate_ms = player_data.get("frame_rate_ms")
        move_rate_ms = player_data.get("move_rate_ms")
        jump_height = player_data.get("jump_height")
        p_scale = player_data.get("p_scale")
        interval_time_jump = player_data.get("interval_time_jump")

        self.player_1 = Player(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale, interval_time_jump)

        self.enemy_list = []

        for zoombie in self.datos_extraidos["nivel_1"]["config_zoombie"]:
            x = zoombie["x"]
            y = zoombie["y"]
            speed_walk = zoombie["speed_walk"]
            speed_run = zoombie["speed_run"]
            gravity = zoombie["gravity"]
            jump_power = zoombie["jump_power"]
            frame_rate_ms = zoombie["frame_rate_ms"]
            move_rate_ms = zoombie["move_rate_ms"]
            jump_height = zoombie["jump_height"]
            p_scale = zoombie["p_scale"]
            interval_time_jump = zoombie["interval_time_jump"]

            enemy_zombie = EnemyZombie(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale, interval_time_jump)
            self.enemy_list.append(enemy_zombie)

        for murcielago in self.datos_extraidos["nivel_1"]["config_murcielago"]:
            x = murcielago["x"]
            y = murcielago["y"]
            speed_walk = murcielago["speed_walk"]
            speed_run = murcielago["speed_run"]
            gravity = murcielago["gravity"]
            jump_power = murcielago["jump_power"]
            frame_rate_ms = murcielago["frame_rate_ms"]
            move_rate_ms = murcielago["move_rate_ms"]
            jump_height = murcielago["jump_height"]
            p_scale = murcielago["p_scale"]
            interval_time_jump = murcielago["interval_time_jump"]

            enemy_murcielago = EnemyMurcielago(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale, interval_time_jump)
            self.enemy_list.append(enemy_murcielago)
            
        self.plataform_list = []
        for plataforma in self.datos_extraidos["nivel_1"]["config_plataformas"]:
            x = plataforma["x"]
            y = plataforma["y"]
            w = plataforma["w"]
            h = plataforma["h"]
            tipo = plataforma["tipo"]

            plataforma_obj = Plataform(x, y, w, h, tipo)
            self.plataform_list.append(plataforma_obj)

        self.bullet_list = []

        self.coin_list = []
        for coin in self.datos_extraidos["nivel_1"]["config_coins"]:
            x = coin["x"]
            y = coin["y"]
            w = coin["w"]
            h = coin["h"]
            tipo = coin["tipo"]

            coin_obj = Coins(x, y, w, h, tipo)
            self.coin_list.append(coin_obj)

        #PAUSA - TIMER
        self.is_paused = False
        self.start_time = 0
        self.elapsed_time = 0
        self.player_moved = False
        self.flag_segundos = False

        self.current_time = time.time()
        self.collision_timer = time.time()

        #IMG RELOJ
        self.clock_background = pygame.image.load("recursos/menu/button_two.png").convert_alpha()
        self.clock_background = pygame.transform.scale(self.clock_background, (120, 60))

        # IMG SCORE
        self.score_image = pygame.image.load("recursos/menu/button_two.png").convert_alpha()
        self.score_image = pygame.transform.scale(self.score_image, (260, 60))

        # IMG LIVE
        self.heart_image = pygame.image.load("recursos/images/gui/set_gui_01/Data/Elements/heart.png").convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40))

        # IMG GAME OVER
        self.game_over_image = pygame.image.load("recursos/images/gui/set_gui_01/Comic/Text/LOSER.png").convert_alpha()
        self.game_over_image_rect = self.game_over_image.get_rect(center=(self.master_surface.get_width() // 2, self.master_surface.get_height() // 2))

        # IMG WINNER
        self.winner_image = pygame.image.load("recursos/images/gui/set_gui_01/Comic/Text/VICTORY.png").convert_alpha()
        self.winner_image_rect = self.winner_image.get_rect(center=(self.master_surface.get_width() // 2, self.master_surface.get_height() // 2))


    def on_click_boton2(self, parametro):
        self.set_active(parametro)
        self.is_paused = not self.is_paused
        if self.is_paused:
            pygame.mixer.music.stop()
        else:
            if not self.player_moved:
                self.player_moved = True
                self.start_time = time.time()
                pygame.mixer.music.load("soundtracks/purgatory.mp3")
                pygame.mixer.music.play(-1)
            else:
                self.elapsed_time += time.time() - self.start_time
                self.start_time = time.time()


    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms, self.plataform_list, self.enemy_list, self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list)
    
            rect_enemy = enemy_element.rect
    
            # Obtener las coordenadas de los rectángulos adicionales
            rect_enemy_top = pygame.Rect(rect_enemy.left, rect_enemy.top - 10, rect_enemy.width, 10)
            rect_player_bottom = pygame.Rect(self.player_1.rect.left, self.player_1.rect.bottom, self.player_1.rect.width, 10)
    
            # Colisión entre el rectángulo superior del enemigo y el rectángulo inferior del jugador
            if rect_player_bottom.colliderect(rect_enemy_top):
                # El enemigo muere
                self.enemy_list.remove(enemy_element)
                self.player_1.score += 10
    
            # Colisión entre cualquier parte del jugador y el enemigo (excepto el rectángulo inferior)
            elif self.player_1.rect.colliderect(rect_enemy) and self.player_1.rect.bottom > rect_enemy.top:
                # El jugador pierde vida
                self.player_1.lives -= 1


        self.pb_lives.value = self.player_1.lives

        if not self.player_moved:
            if keys[K_LEFT] or keys[K_RIGHT]:
                self.player_moved = True
                self.start_time = time.time()
                pygame.mixer.music.load("soundtracks/purgatory.mp3")
                pygame.mixer.music.play(-1)

        self.player_1.events(delta_ms, keys)
        self.player_1.update(delta_ms, self.plataform_list, self.coin_list)


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for coin in self.coin_list:
            coin.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)

        if self.pb_lives.value <= 0:
            self.surface.blit(self.game_over_image, self.game_over_image_rect)
            self.is_paused = True

        if len(self.coin_list) == 0 and len(self.enemy_list) == 0:
            self.surface.blit(self.winner_image, self.winner_image_rect)
            self.is_paused = True

        #SCORE
        self.surface.blit(self.score_image, (170, 0))
        score_font = pygame.font.SysFont("Verdana", 30)  # Fuente para el texto del score
        score_text = score_font.render("SCORE: " + str(self.player_1.score * 100), True, (255, 255, 255))  # Renderiza el texto del score
        self.surface.blit(score_text, (200, 15))

        # Draw mini clock
        if not self.is_paused and self.player_moved:
            current_time = int(time.time() - self.start_time + self.elapsed_time)
            minutes = current_time // 60
            seconds = current_time % 60
            clock_rect = self.clock_background.get_rect(topright=(self.master_surface.get_width() - 20, 5))
            self.surface.blit(self.clock_background, clock_rect)
            clock_text = pygame.font.SysFont("Verdana", 30).render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
            clock_text_rect = clock_text.get_rect(center=clock_rect.center)
            self.surface.blit(clock_text, clock_text_rect)

    
