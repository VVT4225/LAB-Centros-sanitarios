from collections import namedtuple
import csv

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
    with open(fichero,encoding="utf-8"):
        lector = csv.reader(fichero,delimiter=";")
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalido, tiene_uci in lector:
            coords = Coordenadas(float(latitud),float(longitud))
            centro = CentroSanitario(nombre.strip(),localidad.strip(),coords,estado.strip(),int(num_camas),parsea_booleano(acceso_minusvalido),parsea_booleano(tiene_uci))
            res.append(centro)
    return res

leer_centros("C:/Users/Peke/Documents/GitHub/LAB-Centros-sanitarios/data/centrosSanitarios.csv")