import os
from datetime import datetime
import random
import pickle

import cad as cad


class Projecto:
    def __init__(self, cod, rep, desc, datee, leng, tags, like, url):
        self.nombre_usuario = cod
        self.repositorio = rep
        self.descripcion = desc
        self.fecha_actualizacion = datee
        self.lenguaje = leng
        self.tags = tags
        self.like = like
        self.url = url


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


def tostring(trgh):
    print(f"{trgh.nombre_usuario:20} | {trgh.repositorio:20} | {trgh.fecha_actualizacion:20} | {trgh.lenguaje:20} |"
          f" {trgh.tags:20} | {trgh.like:20} | {trgh.url:20}")


def mostrar(trgh):
    for i in range(len(trgh)):
        print(
            f"{trgh[i].nombre_usuario:20} | {trgh[i].repositorio:20} | {trgh[i].fecha_actualizacion:20} | {trgh[i].lenguaje:20} |"
            f" {trgh[i].tags:20} | {trgh[i].like:20} | {trgh[i].url:20}")


def cargar_datos(archivo):
    trgh = []
    contE = 0
    contI = 0
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
                        contE += 1
                    elif tarea.lenguaje is None:
                        contI += 1

    m.close()
    print("Se han cargado {} datos, se han omitido {}".format(contE, contI))

    return trgh


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


def actualizar(trgh):
    now = datetime.now()
    now = str(now)
    repo = input("Ingrese repo: ")
    pos = buscar_rep(trgh, repo)
    if pos != -1:
        print("Encontró")
        tostring(trgh[pos])
        trgh[pos].url = input("Ingrese nuevo URL: ")
        now = now[:10]
        trgh[pos].fecha_actualizacion = now
        tostring(trgh[pos])
    else:
        print("Recatate")
