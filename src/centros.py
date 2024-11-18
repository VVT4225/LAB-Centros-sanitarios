from collections import namedtuple
import csv

from coordenadas import *

Coordenadas = namedtuple("Coordenadas",[("latitud"),("longitud")])
CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def parsea_booleano(cadena):
    cadena = cadena.strip().lower()
    res = None
    if cadena == "true":
        res = True
    elif cadena == "false":
        res = False
    return res


def leer_centros(fichero):
    res = []
    with open(fichero,encoding="utf-8") as f:
        lector = csv.reader(f,delimiter=";")
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalido, tiene_uci in lector:
            coords = Coordenadas(float(latitud),float(longitud))
            centro = CentroSanitario(nombre.strip(),localidad.strip(),coords,estado.strip(),int(num_camas),parsea_booleano(acceso_minusvalido),parsea_booleano(tiene_uci))
            res.append(centro)
    return res

def calcular_total_camas_centros_accesibles(centros):
    res = 0
    for i in centros:
        if i.acceso_minusvalidos == True:
            res += i.num_camas
    return res

def obtener_centros_con_uci_cercanos_a(centros,coords,umbral):
    uci = []
    res = []
    for i in centros:
        if i.tiene_uci == True:
            uci.append(i)
    for i in uci:
        if calcular_distancia(i.coordenadas,coords) <= umbral:
            res.append((i.nombre,i.localidad,i.coordenadas))
    return res