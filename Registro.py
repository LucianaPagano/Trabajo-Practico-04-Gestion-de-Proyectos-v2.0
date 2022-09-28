import random

class Projecto:
    def __init__(self, cod, rep, datee, leng, tags, like, url):
        self.nombre_usuario = cod
        self.repositorio = rep
        self.fecha_actualizacion = datee
        self.lenguaje = leng
        self.tags = tags
        self.like = like
        self.url = url

def validar_mayor_que(num, lim):
    while num < lim:
        print("Error. Debe ser mayor a, ", lim)
        num = int(input("Ingrese nuevamente: "))
    return num

def validar_menor_que(num, lim):
    while num > lim:
        print("Error. Debe ser menor a, ", lim)
        num = int(input("Ingrese nuevamente: "))
    return num

def validar_entre(num, inf, sup):
    while num < inf or num > sup:
        print("Error, opcion no valida")
        num = int(input("Ingrese nuevamente: "))
    return num

def crearArreglo():
    n = int(input("Ingrese la cantidad de componentes del arreglo(mayor que 0): "))
    n = validar_mayor_que(n, 0)
    vec = n * [None]
    return vec

