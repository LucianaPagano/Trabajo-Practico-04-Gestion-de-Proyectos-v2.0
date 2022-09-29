import os
import datetime
from registro import *


def cargar_datos(archivo):
    trgh = []
    m = open(archivo, mode="rt", encoding="utf8")
    primerrenglon = False
    for renglon in m:
        if renglon is not None:
            x = renglon.split("|")
            x_rep = x[1]
            tarea = stringtoproject(renglon[:-1])
            if not primerrenglon:
                primerrenglon = True
            else:
                if not x_rep is None:
                    a = trgh.append(x)
                    add_in_order(trgh, tarea)
    m.close()
    for i in range(len(trgh)):
        print(trgh[i])

    return trgh


def add_in_order(trgh, registro):
    n = len(trgh)
    izq = 0
    der = n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if trgh[c].repositorio == registro.a:
            pos = c
            break

        if registro.repositorio < trgh[c].x_rep:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    trgh[pos:pos] = [registro]


def buscar_rep(trgh, repp):
    n = len(trgh)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if repp == trgh[c].repositorio:
            return c
        if repp < trgh[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    return -1


def leer_texto():
    fd = "proyectos.csv"
    if not os.path.exists(fd):
        print("Error, el archivo no existe: ")
        return
    m = open(fd, "r")
    for line in m:
        print(line, end='')
