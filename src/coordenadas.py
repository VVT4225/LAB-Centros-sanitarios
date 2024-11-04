from collections import namedtuple
import math

Coordenadas = namedtuple("Coordenadas",[("latitud"),("longitud")])

def calcular_distancia(c1,c2):
    dist = math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    return dist

def calcular_media_coordenadas(lista):
    lat = 0
    long = 0
    num = 0
    for c in lista:
        num += 1
        lat += c[0]
        long += c[1]
    res = Coordenadas((lat/num),(long/num))
    return res