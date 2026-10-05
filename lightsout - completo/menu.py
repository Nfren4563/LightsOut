import controlador_teclado as teclado
import visual
import comandos_consola as consola
def seleccionar_dificultad():
    opciones = [5, 7, 9]
    seleccion = 0

    consola.ocultar_cursor()
    visual.dibujar_menu_marco()
    visual.dibujar_opciones_menu(seleccion)

    while True:
        tecla = teclado.esperar_tecla()

        seleccion_anterior = seleccion

        if tecla in (teclado.ARRIBA, teclado.FLECHA_ARRIBA):
            seleccion = max(0, seleccion - 1)

        elif tecla in (teclado.ABAJO, teclado.FLECHA_ABAJO):
            seleccion = min(len(opciones) - 1, seleccion + 1)

        elif tecla == teclado.ENTRAR:
            return opciones[seleccion]

        elif tecla == teclado.SALIR:
            return None

        if seleccion != seleccion_anterior:
            visual.redibujar_opcion(seleccion_anterior, False)
            visual.redibujar_opcion(seleccion, True)