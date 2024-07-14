"""
La fábrica de yogur en potes de vidrio Dahi se encuentra procesando los yogures recibidos de sus distintos
centros de producción y para eso tiene los siguientes archivos:


CORDOBA.CSV, SANTA_FE.CSV, ENTRE_RIOS.CSV, ordenados por lote

    lote: código alfanumérico, por ejemplo DXCO20210304

    gusto: string con posibles valores frutilla, vainilla, sin sabor

    calorías: string con posibles valores entero, light

    adicionales: string con posibles valores con frutas, con cereales o vacío.

    peso: valor numérico con decimales expresado en gramos, por ejemplo 125.22


Se pide escribir un programa en Python que procese los archivos y:


1. Genere un archivo único de salida STOCK.CSV unificando los datos de los 3 archivos y ordenado por lote,
descartando aquellos yogures con un peso menor a 90 gramos.

2. Imprimir la cantidad de kilos de yogur producido por cada uno de los 3 centros de producción

3. Guardar en un archivo PRODUCCION.TXT la descripción y el total de unidades de cada variedad de yogur en stock,
ordenado de mayor a menor por total de unidades. La variedad está determinada por el gusto, las calorías y los adicionales.
Por ejemplo “vainilla light con frutas”, “frutilla entero”, “sin sabor light con cereales”, etc.
"""

def leer_archivo(archivo, vacio):
    linea = archivo.readline()
    return linea.split(",") if linea else vacio

def analizar_stock(provincia):
    vacio = ("","","","","")
    lote, gusto, calorias, adicionales, peso = leer_archivo(provincia, vacio)
    
    while lote:
        if peso  90:
        
    
    return lista_provincia


def generar_stock(cordoba, santa_fe, entre_rios, stock):
    lista_cordoba = []
    lista_santa_fe = []
    lista_entre_rios = []


def main():
    cordoba = open ("CORDOBA.CSV", "r")
    santa_fe = open ("SANTA_FE.CSV", "r")
    entre_rios = open ("ENTRE_RIOS", "r")
    
    stock = open ("STOCK.CSV", "w")
    
    
    

main()