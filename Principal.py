""" TRABAJO PRÁCTICO N4:
        PAGANO, Luciana - ALLENDE, Maximo - ARRIETA, Benjamin - SUAREZ, Rodrigo - HEREDIA, Victoria
"""
from Archivos import *
import time


def buscar_cod(vec, cod):
    n = len(vec)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if cod == vec[c].codigo:
            return c
        if cod < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1


def menu():
    print("\n========================================")
    print("\t\t\tMENU DE OPCIONES")
    print("========================================")
    print("1. Cargar")
    print("2. Filtrar por tag")
    print("3. Lenguajes")
    print("4. Popularidad")
    print("5. Buscar proyecto actualizado")
    print("6. Guardar populares")
    print("7. Mostrar archivo")
    print("8. Salir")
    print("========================================")
    print("========================================")


def principal():
    op = -1
    while op != 0:
        menu()
        op = int(input("Elija opción: "))
        op = validar_entre(op, 1, 8)
        if op == 1:
            cargar_datos()
            print("¡Se han cargado los datos!")
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass


if __name__ == '__main__':
    principal()
