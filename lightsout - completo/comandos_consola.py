

import sys
import os  


def imprimir(texto):
    sys.stdout.write(texto)
    sys.stdout.flush()



def mover_cursor(fila, columna):
    imprimir(f"\033[{fila};{columna}H")

def ocultar_cursor():
    imprimir("\033[?25l")

def mostrar_cursor():
    imprimir("\033[?25h")


def limpiar_pantalla():
    imprimir("\033[2J\033[H")

def borrar_linea():
    imprimir("\033[2K\r")

def restaurar_colores():
    imprimir("\033[0m")

def establecer_color_hex(hex_color):
 
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    imprimir(f"\033[38;2;{r};{g};{b}m")


def obtener_ancho_terminal():

    try:
        return os.get_terminal_size().columns
    except:

        return 80

def obtener_alto_terminal():

    try:
        return os.get_terminal_size().lines
    except:
        return 24

def calcular_columna_inicio(ancho_juego):
    
    ancho_terminal = obtener_ancho_terminal()

    margen = (ancho_terminal - ancho_juego) // 2

    return max(1, margen)