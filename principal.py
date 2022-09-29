""" TRABAJO PRÁCTICO N4:
        PAGANO, Luciana - ALLENDE, Maximo - ARRIETA, Benjamin - SUAREZ, Rodrigo - HEREDIA, Victoria
"""
from archivos import *

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
    matriz = []
    pro = cargar_datos("proyectos.csv")
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
            repp = int(input("Ingresar nombre/número del repositor: "))
            repp = buscar_rep(pro, repp)
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass


if __name__ == '__main__':
    principal()
