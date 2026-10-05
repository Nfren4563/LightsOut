
import comandos_consola as consola

COLOR_ENCENDIDO_LLAMA  = "f5a623"  
COLOR_ENCENDIDO_CUERPO = "e07b00"   
COLOR_APAGADO          = "4a4a4a"   
COLOR_CURSOR           = "00e5ff"   
COLOR_ESTRUCTURA       = "8b7355"   
COLOR_TITULO           = "f5a623"   
COLOR_HUD              = "aaaaaa"   
COLOR_MENU_SELECCION   = "f5a623"  
COLOR_MENU_NORMAL      = "666666" 
COLOR_BORDE            = "555555"  
COLOR_AYUDA            = "FF0000"
ANCHO_FAROL = 7
ALTO_FAROL = 7
SEPARACION = 2

FAROL_ENCENDIDO = [
"   ║   ",   
"  ═╬═  ", 
"  ╔═╗  ",   
" ╔═══╗ ",   
" ║ Δ ║ ",    
" ║ΔΔΔ║ ",    
" ╚═══╝ ",    
]

FAROL_APAGADO = [
"   ║   ",   
"  ═╬═  ",   
"  ╔═╗  ",    
" ╔═══╗ ",    
" ║ ░ ║ ",    
" ║░░░║ ",   
" ╚═══╝ ",   
]

FAROL_CURSOR = [
    "   ║   ",   
    "  ═╬═  ",    
    "  ╔═╗  ",    
    " ╔═══╗ ",    
    " ║ Δ ║ ",   
    " ║ΔΔΔ║ ",    
    " ╚═══╝ ",   
]

TITULO_ARTE = [
    r"        __       ___ .  __      __       ___ ",
    r"|    | / _` |__|  |  ' /__`    /  \ |  |  |  ",
    r"|___ | \__> |  |  |    .__/    \__/ \__/  |  ",
     "                                             ",
]

VICTORIA_ARTE = [
"  ╔═════════════════════════════════╗  ",
"  ║                                 ║  ",
"  ║    Δ  ¡TODAS LAS LUCES   Δ      ║  ",
"  ║   ΔΔΔ    APAGADAS!      ΔΔΔ     ║  ",
"  ║    Δ                     Δ      ║  ",
"  ║                                 ║  ",
"  ╠═════════════════════════════════╣  ",
]

MENU_MARCO = [
"  ╔══════════════════════════════════════════════════╗  ",
"  ║                                                  ║  ",
r"  ║          __       ___ .  __      __       ___    ║  ",
r"  ║  |    | / _` |__|  |  ' /__`    /  \ |  |  |     ║  ",
r"  ║  |___ | \__> |  |  |    .__/    \__/ \__/  |     ║  ",
"  ║                                                  ║  ",
"  ║                                                  ║  ",
"  ║                                                  ║  ",
"  ╠══════════════════════════════════════════════════╣  ",
"  ║       Selecciona una dificultad:                 ║  ",
"  ║                                                  ║  ",
"  ║                                                  ║  ",
"  ║                                                  ║  ",  
"  ║                                                  ║  ",   
"  ║                                                  ║  ",   
"  ║                                                  ║  ",
"  ╠══════════════════════════════════════════════════╣  ",
"  ║  Flechas: navegar                                ║  ",
"  ║  ENTER  : confirmar                              ║  ",
"  ║  Q      : salir                                  ║  ",
"  ║                                                  ║  ",
"  ╚══════════════════════════════════════════════════╝  ",
]


def dibujar_farol(x, y, estado, es_cursor,es_ayuda=False):
    if estado:
        sprite = FAROL_ENCENDIDO
    else:
        sprite = FAROL_APAGADO

    for i, linea in enumerate(sprite):
        consola.mover_cursor(x + i, y)

        if es_ayuda:
            consola.establecer_color_hex(COLOR_AYUDA)

        elif es_cursor:
            consola.establecer_color_hex(COLOR_CURSOR)
        elif estado:
            consola.establecer_color_hex(COLOR_ENCENDIDO_LLAMA)
        else:
            consola.establecer_color_hex(COLOR_APAGADO)

        consola.imprimir(linea)

    consola.restaurar_colores()

def redibujar_celda(tablero, f, c, cursor_f, cursor_c, fila_inicio, col_inicio, ayuda = None):
    if 0 <= f < len(tablero) and 0 <= c < len(tablero[0]):
        x, y = obtener_posicion(f, c, fila_inicio, col_inicio)

        estado = tablero[f][c]
        es_cursor = (f == cursor_f and c == cursor_c)
        es_ayuda = (f, c) == ayuda
        dibujar_farol(x, y, estado, es_cursor,es_ayuda)
    

def dibujar_tablero(tablero, cursor_f, cursor_c, ayuda=None):
    filas = len(tablero)
    columnas = len(tablero[0])

    ancho = columnas * ANCHO_FAROL + (columnas - 1) * SEPARACION
    col_inicio = consola.calcular_columna_inicio(ancho)

    fila_inicio = 8  

    for f in range(filas):
        for c in range(columnas):
            x, y = obtener_posicion(f, c, fila_inicio, col_inicio)

            estado = tablero[f][c]
            es_cursor = (f == cursor_f and c == cursor_c)
            es_ayuda = (f,c) == ayuda

            dibujar_farol(x, y, estado, es_cursor,es_ayuda)

    return fila_inicio, col_inicio


def dibujar_hud(movimientos, tamaño, fila_inicio, filas_tablero,col_inicio,columnas,ayuda_activa):
    ancho_tablero = columnas * ANCHO_FAROL + (columnas - 1) * SEPARACION
    fila = fila_inicio + filas_tablero * (ALTO_FAROL + 1) + 1

    consola.mover_cursor(fila+2, col_inicio)
    consola.imprimir(f"Movimientos: {movimientos} | Tamaño: {tamaño}x{tamaño} | Ayuda: {'Activo' if ayuda_activa else 'Apagado'}")

    consola.mover_cursor(fila + 3, col_inicio)
    consola.imprimir("Flechas: mover | ENTER: activar | Q: salir  |  T: Ayuda")


def dibujar_victoria(movimientos):
    consola.limpiar_pantalla()

    ancho = len(VICTORIA_ARTE[0])
    col_inicio = consola.calcular_columna_inicio(ancho)

    for i, linea in enumerate(VICTORIA_ARTE):
        consola.mover_cursor(2 + i, col_inicio)
        consola.imprimir(linea)
 

def dibujar_menu_marco():

    ancho = len(MENU_MARCO[0])
    col_inicio = consola.calcular_columna_inicio(ancho)

    for i, linea in enumerate(MENU_MARCO):
        consola.mover_cursor(2 + i, col_inicio)
        consola.imprimir(linea)

def dibujar_opciones_menu(seleccion):
    opciones = ["Facil (5x5)", "Medio (7x7)", "Dificil (9x9)"]

    col_inicio = consola.calcular_columna_inicio(len(MENU_MARCO[0]))

    fila_base = 12  

    for i, texto in enumerate(opciones):
        consola.mover_cursor(fila_base + i, col_inicio + 10)

        if i == seleccion:
            consola.establecer_color_hex(COLOR_MENU_SELECCION)
            consola.imprimir(f"> {texto}")
        else:
            consola.establecer_color_hex(COLOR_MENU_NORMAL)
            consola.imprimir(f"  {texto}")

    consola.restaurar_colores()

def obtener_posicion(f, c, fila_inicio, col_inicio):
    x = fila_inicio + f * (ALTO_FAROL + 1)
    y = col_inicio + c * (ANCHO_FAROL + SEPARACION)
    return x, y

def dibujar_titulo(col_inicio, columnas):
    
    ancho_tablero = columnas * ANCHO_FAROL + (columnas - 1) * SEPARACION

    for i, linea in enumerate(TITULO_ARTE):
        col = col_inicio + (ancho_tablero - len(linea)) // 2
        consola.mover_cursor(1 + i, col)
        consola.imprimir(linea)

def dibujar_candelabro(fila_inicio, col_inicio, filas, columnas):
    
    ancho_tablero = columnas * ANCHO_FAROL + (columnas - 1) * SEPARACION

    barra_sup = "═" * ancho_tablero

    consola.mover_cursor(fila_inicio - 2, col_inicio)
    consola.imprimir(barra_sup)

    for c in range(columnas):
        x, y = obtener_posicion(0, c, fila_inicio, col_inicio)

        consola.mover_cursor(x - 1, y + ANCHO_FAROL//2)
        consola.imprimir("║")

    barra_inf = "═" * ancho_tablero

    alto_tablero = filas * (ALTO_FAROL + 1)

    consola.mover_cursor(fila_inicio + alto_tablero, col_inicio)
    consola.imprimir(barra_inf)

def redibujar_opcion(index, seleccionada):
    opciones = ["Facil (5x5)", "Medio (7x7)", "Dificil (9x9)"]

    col_inicio = consola.calcular_columna_inicio(len(MENU_MARCO[0]))
    fila_base = 12

    consola.mover_cursor(fila_base + index, col_inicio + 10)

    if seleccionada:
        consola.establecer_color_hex(COLOR_MENU_SELECCION)
        consola.imprimir(f"> {opciones[index]}  ")
    else:
        consola.establecer_color_hex(COLOR_MENU_NORMAL)
        consola.imprimir(f"  {opciones[index]}  ")

    consola.restaurar_colores()

