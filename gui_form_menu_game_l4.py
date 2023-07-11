import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from player import Player
from enemigos import *
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Coins
import time

class FormGameLevel4(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        #self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=5,y=0,w=160,h=60,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_boton2,on_click_param="form_menu_levels",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="recursos/menu/button_two.png",on_click=self.on_click_shoot,on_click_param="form_menu_settings",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=450,y=10,w=200,h=40,color_background=None,color_border=None,image_background="recursos/nada.png",image_progress="recursos/images/gui/set_gui_01/Data/Elements/heart.png",value = 5, value_max=5)
        self.widget_list = [self.boton2, self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/fondo/1_game_background/1_game_background.png")

        self.player_1 = Player(x=0,y=400,speed_walk=10,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)

        self.enemy_list = []
        self.enemy_list.append (EnemyEsqueletin(x=1300,y=300,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.04,interval_time_jump=1000))
        self.enemy_list.append (EnemyEsqueletin(x=1100,y=500,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=300,move_rate_ms=50,jump_height=140,p_scale=0.04,interval_time_jump=500))
        self.enemy_list.append (EnemyEsqueletin(x=900,y=500,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=600,move_rate_ms=50,jump_height=140,p_scale=0.04,interval_time_jump=500))
        self.enemy_list.append (EnemyEsqueletin(x=200,y=400,speed_walk=1,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.04,interval_time_jump=1000))
        
        self.enemy_list.append (EnemyMurcielago(x=400,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=900,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=100,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=800))
        self.enemy_list.append (EnemyMurcielago(x=1000,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=1400,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=800))
        self.enemy_list.append (EnemyMurcielago(x=250,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=700,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=1200,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=800))
        self.enemy_list.append (EnemyMurcielago(x=1100,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=500))
        self.enemy_list.append (EnemyMurcielago(x=600,y=100,speed_walk=1,speed_run=2,gravity=1,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.02,interval_time_jump=800))

        self.enemy_list.append (EnemyEqueco(x=800,y=400,speed_walk=3,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=1000,move_rate_ms=10,jump_height=140,p_scale=0.04,interval_time_jump=500))
        #self.config_json = config_json

        self.plataform_list = []
        self.plataform_list.append(Plataform(x=200,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=250,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=450,y=500,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=500,y=500,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=200,y=200,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=350,y=280,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=300,y=580,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=350,y=580,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=900,y=580,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=950,y=580,width=100,height=50,type=0))

        self.plataform_list.append(Plataform(x=450,y=350,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=500,y=350,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=550,y=350,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=600,y=350,width=100,height=50,type=2))

        self.plataform_list.append(Plataform(x=0,y=350,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=50,y=350,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=100,y=350,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=150,y=350,width=100,height=50,type=2))

        self.plataform_list.append(Plataform(x=0,y=550,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=300,y=100,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=1400,y=100,width=100,height=50,type=2))    
        self.plataform_list.append(Plataform(x=600,y=430,width=100,height=50,type=12))
        self.plataform_list.append(Plataform(x=650,y=430,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=750,y=280,width=100,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=280,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=280,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=800,y=460,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=100,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=900,y=100,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=100,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=900,y=100,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=50,y=500,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=50,y=160,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=500,y=160,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=550,y=160,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1100,y=100,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1300,y=500,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1300,y=160,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=1350,y=160,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=1400,y=350,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1200,y=310,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1250,y=310,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1150,y=490,width=100,height=50,type=13))
        self.plataform_list.append(Plataform(x=1000,y=390,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=1050,y=390,width=100,height=50,type=14))
        self.plataform_list.append(Plataform(x=1000,y=200,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1050,y=200,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1100,y=200,width=100,height=50,type=0))
        

        self.bullet_list = []

        self.coin_list = []
        self.coin_list.append (Coins(x=1430,y=300,w=1,h=1,type=2))
        self.coin_list.append (Coins(x=100,y=480,w=1,h=1,type=3))
        self.coin_list.append (Coins(x=600,y=300,w=1,h=1,type=5))
        self.coin_list.append (Coins(x=500,y=300,w=1,h=1,type=1))
        self.coin_list.append (Coins(x=800,y=250,w=1,h=1,type=1))
        self.coin_list.append (Coins(x=930,y=80,w=1,h=1,type=2))
        self.coin_list.append (Coins(x=1220,y=280,w=1,h=1,type=3))
        self.coin_list.append (Coins(x=1050,y=350,w=1,h=1,type=4))
        self.coin_list.append (Coins(x=350,y=550,w=1,h=1,type=5))
        self.coin_list.append (Coins(x=830,y=430,w=1,h=1,type=1))
        self.coin_list.append (Coins(x=100,y=130,w=1,h=1,type=2))
        self.coin_list.append (Coins(x=350,y=80,w=1,h=1,type=3))
        self.coin_list.append (Coins(x=1430,y=70,w=1,h=1,type=5)) 
        self.coin_list.append (Coins(x=400,y=670,w=1,h=1,type=3))
        self.coin_list.append (Coins(x=800,y=670,w=1,h=1,type=4))
        self.coin_list.append (Coins(x=1200,y=670,w=1,h=1,type=5))
        self.coin_list.append (Coins(x=1130,y=60,w=1,h=1,type=1))
        self.coin_list.append (Coins(x=550,y=120,w=1,h=1,type=3))
        self.coin_list.append (Coins(x=1350,y=470,w=1,h=1,type=4))
        self.coin_list.append (Coins(x=100,y=320,w=1,h=1,type=5))

        #PAUSA - TIMER
        self.is_paused = False
        self.start_time = 0
        self.elapsed_time = 0
        self.player_moved = False

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

    #def on_click_shoot(self, parametro):
    #    for enemy_element in self.enemy_list:
    #        self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="recursos/images/gui/jungle/upgrade/a.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
 
    def update(self, lista_eventos, keys, delta_ms):
            
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms, self.plataform_list, self.enemy_list, self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list)

            rect_enemy = enemy_element.rect
            if self.player_1.rect.colliderect(rect_enemy) and self.player_1.rect.top < rect_enemy.bottom:
                self.enemy_list.remove(enemy_element)
                self.player_1.score += 10
        
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

        if self.player_1.lives <= 0:
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