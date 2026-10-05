import random
from menu import *

def crear_tablero(filas, columnas):
    return [[False for _ in range(columnas)] for _ in range(filas)]


def activar_celda(tablero, fila, columna):
    celdas = [
        (fila, columna),
        (fila - 1, columna),
        (fila + 1, columna),
        (fila, columna - 1),
        (fila, columna + 1),
    ]

    for f, c in celdas:
        if 0 <= f < len(tablero) and 0 <= c < len(tablero[0]):
            tablero[f][c] = not tablero[f][c]


def generar_puzzle(filas, columnas, movimientos_objetivo):
    t = [[0 for _ in range(columnas)] for _ in range(filas)]

    historial = []

    for _ in range(movimientos_objetivo):
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)

        activar_celda(t, f, c)
        historial.append((f, c))

        if verificar_victoria(t):
            activar_celda(t, 0, 0)
            historial.append((0, 0))

    solucion = list(reversed(historial))
    return t, solucion


def verificar_victoria(tablero):
    return all(not celda for fila in tablero for celda in fila)