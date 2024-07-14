"""
Escribir un programa, compuesto por funciones, que permita:

a) Ingresar en un diccionario, apellidos de jugadores (como clave) y dos datos: cantidad de minutos
jugados en cierto partido del mundial y puntaje otorgado por los periodistas deportivos para ese partido.
Como se ingresan datos de distintos partidos, un mismo jugador puede ingresarse varias veces, debiendo sumarse los valores. 

b) Listar cada uno de los jugadores con el total de tiempo jugado y el total del puntaje.


c) Imprimir un listado ordenado de mayor a menor de los 5 jugadores de mayor puntaje.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#dicc_jugadores = {"apellido_jug":["cant_minutos_jugados", "puntaje_partido"]}

def ingresar_valores ():
    
    MIN_JUGADOS = 0
    PUNTOS = 1
    
    dicc_jugadores = {}
    
    seguir = "si"
    
    while seguir == "si":
        
        jugador = input ("Apellido jugador: ")
        min_jugados = int (input ("Minutos jugados: "))
        puntos = int (input ("Puntaje dado por los periodistas: "))
        
        if jugador in dicc_jugadores:
            dicc_jugadores[jugador][MIN_JUGADOS] += min_jugados
            dicc_jugadores[jugador][PUNTOS] +=  puntos
        else:
            dicc_jugadores[jugador] = [min_jugados, puntos]
            
        seguir = input ("Seguir? (si/no): ")
    
    return dicc_jugadores

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def listar_jugadores(dicc_jugadores):
    
    MIN_JUGADOS = 0
    PUNTOS = 1
    
    print ("\n Listado de jugadores:")
    for jugador in dicc_jugadores:
        print (f"{jugador} jugó {dicc_jugadores[jugador][MIN_JUGADOS]} minutos y obtuvo {dicc_jugadores[jugador][PUNTOS]} puntos por parte de los periodistas")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def lista_puntos_ordenada(dicc_jugadores):
    
    DESEMPEÑO = 1
    PUNTOS = 1
    
    lista_ordenada = sorted(dicc_jugadores.items(), key = lambda jugador:jugador[DESEMPEÑO][PUNTOS], reverse = True)
    
    print("\n Mejores puntajes:")
    for nombre, desempeño in lista_ordenada[0:5]:
        print (f"{nombre}: {desempeño[PUNTOS]} puntos")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main ():
    
    dicc_jugadores = ingresar_valores ()
    
    listar_jugadores(dicc_jugadores)
    lista_puntos_ordenada (dicc_jugadores)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
main()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#