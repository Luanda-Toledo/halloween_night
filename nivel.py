import json

def data_json(nombre_archivo:str):
    '''
    Carga datos de un archivo JSON y los devuelve como una lista de Python.
    Parámetros: nombre_archivo (str): Ruta o nombre del archivo JSON a cargar.
    Retorna: lista (list): Lista de Python con los datos del archivo JSON.
    '''
    lista= []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict
    return lista