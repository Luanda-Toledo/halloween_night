import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from plataforma import Plataform
from background import Background
from bullet import Bullet
from enemy_fantasmin import EnemyFantasmin
from enemy_murcielg import EnemyMurcielg

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_settings",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_settings",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/fondo/3_game_background/3_game_background.png")

        self.player_1 = Player(x=0,y=400,speed_walk=10,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)

        self.enemy_list = []
        self.enemy_list.append (EnemyFantasmin(x=1250,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=300))
        self.enemy_list.append (EnemyFantasmin(x=1100,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=300,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=500))
        self.enemy_list.append (EnemyFantasmin(x=700,y=200,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=200,y=400,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=600,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=50))
        self.enemy_list.append (EnemyFantasmin(x=450,y=400,speed_walk=1,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=1400,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=300,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=500))
        self.enemy_list.append (EnemyFantasmin(x=900,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=500,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=600,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=50))
        self.enemy_list.append (EnemyFantasmin(x=650,y=400,speed_walk=1,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=100,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=300,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=500))
        self.enemy_list.append (EnemyFantasmin(x=200,y=200,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=1400,y=500,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=600,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=50))
        self.enemy_list.append (EnemyFantasmin(x=1050,y=500,speed_walk=1,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=100,move_rate_ms=10,jump_height=140,p_scale=0.05,interval_time_jump=100))
        self.enemy_list.append (EnemyFantasmin(x=300,y=100,speed_walk=2,speed_run=2,gravity=10,jump_power=30,frame_rate_ms=300,move_rate_ms=50,jump_height=140,p_scale=0.05,interval_time_jump=500))
        #self.config_json = config_json

        self.plataform_list = []
        self.plataform_list.append(Plataform(x=800,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=850,y=400,width=100,height=50,type=0))

        self.plataform_list.append(Plataform(x=350,y=300,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=400,y=300,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=450,y=300,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=350,y=500,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=400,y=500,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=450,y=500,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=500,y=500,width=100,height=50,type=2))
        self.plataform_list.append(Plataform(x=550,y=500,width=100,height=50,type=2))

        self.plataform_list.append(Plataform(x=900,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=950,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1000,y=400,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=0,y=300,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=50,y=300,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=100,y=300,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1000,y=200,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1050,y=200,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1100,y=200,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1150,y=200,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=200,y=150,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=100,y=200,width=100,height=50,type=0))

        self.plataform_list.append(Plataform(x=600,y=100,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=700,y=200,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=800,y=300,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1150,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1200,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1250,y=400,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1300,y=400,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1000,y=600,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1050,y=600,width=100,height=50,type=0))
        self.plataform_list.append(Plataform(x=1100,y=600,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1350,y=150,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1400,y=150,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=150,y=400,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=200,y=400,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=300,y=600,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=750,y=550,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=800,y=550,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=600,y=360,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=650,y=360,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1200,y=550,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1400,y=550,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=100,y=550,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=0,y=490,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1300,y=300,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1350,y=300,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=350,y=100,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=400,y=100,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=850,y=100,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=900,y=100,width=100,height=50,type=1))

        self.plataform_list.append(Plataform(x=1200,y=80,width=100,height=50,type=1))
        self.plataform_list.append(Plataform(x=1250,y=80,width=100,height=50,type=1))

        self.bullet_list = []

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))

        

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)

        self.pb_lives.value = self.player_1.lives 


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)