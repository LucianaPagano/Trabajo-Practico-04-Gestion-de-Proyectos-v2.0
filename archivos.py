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

