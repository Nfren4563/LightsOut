
import keyboard


ARRIBA    = "up"
ABAJO     = "down"
DERECHA   = "right"
IZQUIERDA = "left"
FLECHA_ARRIBA    = "flecha arriba"
FLECHA_ABAJO     = "flecha abajo"
FLECHA_DERECHA   = "flecha derecha"
FLECHA_IZQUIERDA = "flecha izquierda"
ENTRAR    = "enter"
SALIR     = "q"
T    = "t"


_TECLAS_JUEGO = [ARRIBA, ABAJO, DERECHA, IZQUIERDA, FLECHA_ARRIBA, FLECHA_ABAJO, FLECHA_DERECHA, FLECHA_IZQUIERDA, ENTRAR, SALIR, "esc", T]


def esperar_tecla():

    evento = keyboard.read_event(suppress=False)

    if evento.event_type != keyboard.KEY_DOWN:
        return None

    nombre = evento.name.lower()

    if nombre in ("q", "esc"):
        return SALIR

    if nombre in _TECLAS_JUEGO:
        return nombre

    return None


def limpiar():
    keyboard.unhook_all()
