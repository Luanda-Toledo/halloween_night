import pygame
import json

class Auxiliar:
    '''
    "Auxiliar" contiene varios métodos estáticos para tareas relacionadas con la manipulacióm
    de imágenes y el manejo de archivos JSON
    '''

    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip = False, step = 1, scale = 1): #para img en hoja sprite
        '''
        Este método toma la ruta de una hoja de sprites junto con el número de columnas y filas en la hoja.
        Opcionalmente, permite voltear las imágenes horizontalmente, establecer un tamaño de paso para 
        seleccionar fotogramas y escalar los fotogramas.
        Divide la hoja de sprites en fotogramas individuales y devuelve una lista de superficies pygame
        que representan cada fotograma.
        '''
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format, from_index, quantity, flip = False, step = 1, scale = 1, w = 0,
                                    h = 0, repeat_frame = 1): #para img individuales
        '''
        Este método toma una cadena de formato de ruta, un índice inicial, una cantidad y parámetros
        opcionales similares al método anterior.
        Genera rutas utilizando la cadena de formato y el índice proporcionados, carga los archivos
        de imagen individuales y realiza transformaciones opcionales.
        Devuelve una lista de superficies pygame que representan los fotogramas obtenidos de los archivos
        de imagen separados.
        '''

        lista = []
        for i in range(from_index, quantity + from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma, (w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma, 
                                                           (fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def leer_json(path):
        '''
        Este método toma la ruta de un archivo JSON y lee su contenido utilizando la función json.load().
        Devuelve los datos JSON analizados como un objeto de Python (diccionario, lista, etc.).
        '''
        with open(path, "r") as archivo:
            datos = json.load(archivo)
        return datos
    
