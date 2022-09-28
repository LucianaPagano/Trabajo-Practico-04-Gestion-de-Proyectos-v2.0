import os
import pickle
from Registro import *

def cargar_datos():
    trgh = []
    m = open("proyectos.csv", mode="rt", encoding="utf8")
    primerrenglon = False
    for renglon in m:
        x = renglon.split("|")
        name_name = x[0]
        name_rep = x[1]
        desc_rep = x[2]
        name_date = x[3]
        leng_rep = x[4]
        name_rep = x[5]
        if not primerrenglon:
            primerrenglon = True
        else:
            if not leng_rep == None:
                trgh.append(x)
    m.close()
    #for i in range(len(trgh)):
     #   print(trgh[i])



def tags():
    pass

def leer_texto():
    fd = "proyectos.csv"
    if not os.path.exists(fd):
        print("Error, el archivo no existe: ")
        return
    m = open(fd, "r")
    for line in m:
        print(line, end='')


