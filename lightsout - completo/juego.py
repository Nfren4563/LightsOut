import tablero
import visual
import controlador_teclado as teclado


class Juego:
    def __init__(self):
        self.tablero     = None
        self.cursor_f    = 0
        self.cursor_c    = 0
        self.movimientos = 0
        self.fila_inicio = 0
        self.col_inicio  = 0
        self.modo_ayuda  = False
        self.solucion    = []  


    def iniciar(self, tamaño):
        if tamaño == 5:
            movimientos = 5
        elif tamaño == 7:
            movimientos = 10
        else:
            movimientos = 15

        self.tablero, self.solucion = tablero.generar_puzzle(
            tamaño, tamaño, movimientos
        )

        self.cursor_f    = 0
        self.cursor_c    = 0
        self.movimientos = 0
        self.modo_ayuda  = False


    def obtener_ayuda(self):
        if self.modo_ayuda and self.solucion:
            return self.solucion[0]
        return None


    def manejar_input(self, tecla):

        if tecla in (teclado.ARRIBA, teclado.FLECHA_ARRIBA):
            if self.cursor_f > 0:
                self.mover_cursor(self.cursor_f - 1, self.cursor_c)

        elif tecla in (teclado.ABAJO, teclado.FLECHA_ABAJO):
            if self.cursor_f < len(self.tablero) - 1:
                self.mover_cursor(self.cursor_f + 1, self.cursor_c)

        elif tecla in (teclado.IZQUIERDA, teclado.FLECHA_IZQUIERDA):
            if self.cursor_c > 0:
                self.mover_cursor(self.cursor_f, self.cursor_c - 1)

        elif tecla in (teclado.DERECHA, teclado.FLECHA_DERECHA):
            if self.cursor_c < len(self.tablero[0]) - 1:
                self.mover_cursor(self.cursor_f, self.cursor_c + 1)

        elif tecla == "t":
            self.modo_ayuda = not self.modo_ayuda
            self.dibujar()  

        elif tecla == teclado.ENTRAR:
            self.activar()


    def dibujar(self):
        ayuda = self.obtener_ayuda()

        self.fila_inicio, self.col_inicio = visual.dibujar_tablero(
            self.tablero, self.cursor_f, self.cursor_c, ayuda
        )
        visual.dibujar_titulo(self.col_inicio, len(self.tablero[0]))
        visual.dibujar_candelabro(
            self.fila_inicio, self.col_inicio,
            len(self.tablero), len(self.tablero[0])
        )
        visual.dibujar_hud(
            self.movimientos, len(self.tablero),
            self.fila_inicio, len(self.tablero),
            self.col_inicio, len(self.tablero[0]),
            self.modo_ayuda
        )

    def es_victoria(self):
        return tablero.verificar_victoria(self.tablero)

    def mover_cursor(self, nueva_f, nueva_c):
        vieja_f, vieja_c = self.cursor_f, self.cursor_c
        self.cursor_f = nueva_f
        self.cursor_c = nueva_c

        ayuda = self.obtener_ayuda()

        visual.redibujar_celda(
            self.tablero, vieja_f, vieja_c,
            self.cursor_f, self.cursor_c,
            self.fila_inicio, self.col_inicio, ayuda
        )
        visual.redibujar_celda(
            self.tablero, self.cursor_f, self.cursor_c,
            self.cursor_f, self.cursor_c,
            self.fila_inicio, self.col_inicio, ayuda
        )


    def activar(self):
        f, c = self.cursor_f, self.cursor_c

        tablero.activar_celda(self.tablero, f, c)
        self.movimientos += 1

        ayuda_anterior = self.obtener_ayuda()

        if self.solucion and (f, c) == self.solucion[0]:
            self.solucion.pop(0)
        else:
            self.solucion.insert(0, (f, c))

        ayuda = self.obtener_ayuda()

        celdas = set([(f, c), (f-1, c), (f+1, c), (f, c-1), (f, c+1)])
        if ayuda_anterior:
            celdas.add(ayuda_anterior)
        if ayuda:
            celdas.add(ayuda)

        for cf, cc in celdas:
            visual.redibujar_celda(
                self.tablero, cf, cc,
                self.cursor_f, self.cursor_c,
                self.fila_inicio, self.col_inicio, ayuda
            )

        visual.dibujar_hud(
            self.movimientos, len(self.tablero),
            self.fila_inicio, len(self.tablero),
            self.col_inicio, len(self.tablero[0]),
            self.modo_ayuda
        )