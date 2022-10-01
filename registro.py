#import os
import datetime
import pickle
import random
#from archivos import *


def stringtoproject(renglon):
    x = renglon.split("|")
    x_cod = x[0]
    x_rep = x[1]
    x_desc = x[2]
    x_date = x[3]
    x_leng = x[4]
    x_tags = x[5]
    x_likes = x[6]
    x_url = x[7]
    return Projecto(x_cod, x_rep, x_desc, x_date, x_leng, x_tags, x_likes, x_url)


def cargar_datos(archivo):
    trgh = []
    m = open(archivo, mode="rt", encoding="utf8")
    primerrenglon = True
    for renglon in m:
        if renglon is not None:
            tarea = stringtoproject(renglon)
            x_rep = tarea.repositorio
            if primerrenglon:
                primerrenglon = False
            else:
                if not tarea.lenguaje is None:
                    pos = buscar_rep(trgh, x_rep)
                    if pos == -1:
                        add_in_order(trgh, tarea)
    m.close()
    print(len(trgh))
    for i in range(len(trgh)):
        print(
            f"{trgh[i].nombre_usuario:20} | {trgh[i].repositorio:20} | {trgh[i].fecha_actualizacion:20} | {trgh[i].lenguaje:20} |"
            f" {trgh[i].tags:20} | {trgh[i].like:20} | {trgh[i].url:20}")
    return trgh


def add_in_order(trgh, registro):
    n = len(trgh)
    izq = 0
    der = n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if trgh[c].repositorio == registro.repositorio:
            pos = c
            break

        if registro.repositorio < trgh[c].repositorio:
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
