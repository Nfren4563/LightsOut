import comandos_consola as consola
import controlador_teclado as teclado
from juego import Juego
import visual 
from menu import seleccionar_dificultad

def main():
    juego = Juego()

    consola.limpiar_pantalla()

    consola.ocultar_cursor()

    tam = seleccionar_dificultad()
    if tam is None:
        return

    juego.iniciar(tam)

    consola.ocultar_cursor()

    consola.limpiar_pantalla()

    juego.dibujar()

    try:
        while True:

            tecla = teclado.esperar_tecla()

            if tecla == teclado.SALIR:
                consola.limpiar_pantalla()
                tam = seleccionar_dificultad()
                if tam is None:
                    return
                juego.iniciar(tam)

                consola.limpiar_pantalla()
                juego.dibujar()
                continue

            juego.manejar_input(tecla)   

            if juego.es_victoria():
                visual.dibujar_victoria(juego.movimientos)

                while True:
                    tecla = teclado.esperar_tecla()

                    if tecla == teclado.ENTRAR:
                        tam = seleccionar_dificultad()
                        if tam is None:
                            return
                        juego.iniciar(tam)
                        break

                    elif tecla == teclado.SALIR:
                        return

    finally:
        consola.mostrar_cursor()
        teclado.limpiar()

if __name__ == "__main__":
    main()