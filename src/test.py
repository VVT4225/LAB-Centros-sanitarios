from coordenadas import *
from centros import *
from mapas import *

# print(calcular_distancia(Coordenadas(36.72460010332263, -5.931456684613025),Coordenadas(36.75005534052628, -5.809773177487557)))
centros = (leer_centros("C:/Users/Peke/Documents/GitHub/LAB-Centros-sanitarios/data/centrosSanitarios.csv"))
#print(calcular_total_camas_centros_accesibles(centros))
print(obtener_centros_con_uci_cercanos_a(centros,Coordenadas(36.72460010332263, -5.931456684613025),1))