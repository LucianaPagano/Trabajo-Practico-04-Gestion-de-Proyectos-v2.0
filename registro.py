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


def stringtoproject(renglon):
    x = renglon.split("|")
    x_cod = x[0]
    x_rep = x[1]
    x_date = x[2]
    x_leng = x[3]
    x_tags = x[4]
    x_likes = x[5]
    x_url = x[6]
    return Projecto(x_cod, x_rep, x_date, x_leng, x_tags, x_likes, x_url)


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
