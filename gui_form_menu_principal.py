import pygame
import pygame.mixer
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button

class FormMenuA(Form):
    '''
    "FormMenuA" es una subclase de "Form" y representa el formulario del menú principal
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        '''
        El método de inicialización de la clase recibe varios parámetros que definen las propiedades del formulario:
        name: El nombre del formulario.
        master_surface: La superficie principal del formulario.
        x, y: Las coordenadas de la posición inicial del formulario.
        w, h: El ancho y alto del formulario.
        color_background: El color de fondo del formulario.
        color_border: El color del borde del formulario.
        active: Indica si el formulario está activo o no.

        Carga y muestra una imagen de presentación del juego durante 5 segundos.
        Carga y muestra una imagen de fondo para el menú principal.
        Carga y muestra una imagen de fondo para los botones del menú.
        Inicializa los botones correspondientes a cada opción del menú: START, SCORES, SETTINGS y EXIT.
        Crea una lista llamada lista_widget que contiene todos los botones.
        '''
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        #Imagen de inicio del juego de 5 segundos 
        ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("HALLOWEEN NIGHT")

        imagen = pygame.image.load("recursos/menu/presentacion_juego.png")
        imagen = pygame.transform.scale(imagen, tamaño_presentacion_inicial)
        imagen_rect = imagen.get_rect()
        imagen_rect.center = (ventana.get_width() // 2, ventana.get_height() // 2)

        fuente = pygame.font.Font(None, 50)
        texto = fuente.render("C a r g a n d o . . .", True, C_RED)
        texto_rect = texto.get_rect()
        texto_rect.center = posicion_text_cargando_menu_principal

        tiempo_inicial = pygame.time.get_ticks()

        while pygame.time.get_ticks() - tiempo_inicial < 5000:
            ventana.fill(C_BLACK)
            ventana.blit(imagen, imagen_rect)
            ventana.blit(texto, texto_rect)
            pygame.display.flip()

        # Imagen del fondo del menu principal
        screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
        imagen_fondo = pygame.image.load("recursos/menu/menu_fondo_dos.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA,ALTO_VENTANA))
        pygame.display.set_caption("HALLOWEEN NIGTH")
        screen.blit(imagen_fondo,imagen_fondo.get_rect())

        # Imagen fondo de los botones
        imagen_fondo_botones = pygame.image.load("recursos/menu/fondo_menu_uno.png")
        imagen_fondo_botones = pygame.transform.scale(imagen_fondo_botones, tamaño_img_fondo_botones)
        imagen_fondo_botones_rect = imagen_fondo_botones.get_rect()
        imagen_fondo_botones_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

        # LEVELS
        self.boton1 = Button(master = self, x = 100, y = 20, w = 180, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_menu_levels", text = "START", font = "Times", font_size = 30, font_color = C_BLACK)
        # SCORES
        self.boton2 = Button(master = self, x = 80, y = 80, w = 220, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_menu_C", text = "SCORES", font = "Times", font_size = 30, font_color = C_BLACK)
        # SETTING
        self.boton3 = Button(master = self, x = 80, y = 140, w = 220, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "form_menu_settings", text = "SETTING", font = "Times", font_size = 30, font_color = C_BLACK)
        # EXIT
        self.boton4 = Button(master = self, x = 110, y = 200, w = 160, h = 80, color_background = None, color_border = None, image_background = "recursos/menu/button.png", on_click = self.on_click_boton2, on_click_param = "", text = "EXIT", font = "Times", font_size = 30, font_color = C_BLACK)

        #Lista de botones que van a aparecer en nuestro menu principal
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.boton4]
    
    def on_click_boton2(self, parametro):
        '''
        Maneja el evento de clic de los botones del menú. Cambia al formulario correspondiente 
        a la opción seleccionada estableciéndolo como formulario activo.
        '''
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        '''
        Actualiza el estado del formulario y sus elementos en función de los eventos recibidos, las teclas presionadas 
        y el tiempo transcurrido desde la última actualización. Actualiza los botones en la lista lista_widget.
        '''
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        '''
        Dibuja el contenido del formulario en la superficie principal. Llama al método draw()
        de la clase padre "Form" para dibujar el fondo y el borde. Dibuja los botones en la lista lista_widget.
        ''' 
        super().draw()

        for aux_widget in self.lista_widget:    
            aux_widget.draw()