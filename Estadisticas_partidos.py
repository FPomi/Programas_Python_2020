"""
El siguiente ejercicio nos pide extraer estadísticas para un campeonato de fútbol finalizado
a partir de ciertos datos que se encuentran cargados en un diccionario importado desde un archivo secundario.

El diccionario tiene como clave el nombre del equipo de fútbol y como valor asociado una tupla de largo 5,
que contiene información sobre el desempeño de los equipos en el campeonato. En la primera posición tiene la
cantidad de partidos ganados (vale por 3 puntos); en la segunda posición la cantidad de partidos empatados
(vale por 1 punto); en la tercera posición la cantidad de partidos perdidos (vale por 0 puntos);
en la cuarta posición la cantidad de goles realizados; y en la quinta posición la cantidad de goles recibidos.

A partir de importar este diccionario, se pide construir un programa que calcule las siguientes estadísticas:

El equipo que salió campeón, con su respectiva cantidad de puntos.
El equipo que desciende (último), con su respectiva cantidad de puntos.
El partido que más partidos empatados tuvo, con su respectiva cantidad.
El equipo que tiene el ratio goles realizados sobre goles recibidos más alto de todos (goles realizados / goles recibidos).
"""

def estadisticas_torneo(dicc_estadisticas):
    mayor_puntaje = 0
    menor_puntaje = 1000
    mayor_empates = 0
    ratio_goles = 0
    
    for equipo in dicc_estadisticas:
        ganados, empatados, perdidos, goles_metidos, goles_recibidos = dicc_estadisticas [equipo]
        
        puntos = (ganados * 3) + empatados
        
        if mayor_puntaje < puntos:
            mayor_puntaje = puntos
            equipo_campeon = equipo
            
        if  menor_puntaje > puntos:
            menor_puntaje = puntos
            equipo_descendiente = equipo
            
        if mayor_empates < empatados:
            mayor_empates = empatados
            equipo_mayor_empates = equipo
            
        if  goles_recibidos == 0 or ratio_goles < (goles_metidos/goles_recibidos):
            ratio_goles = goles_metidos/goles_recibidos
            equipo_mejor_ratio = equipo
        
    print (f"El equipo campeon es {equipo_campeon} con {mayor_puntaje} puntos.")
    print(f"El equipo que desciende es {equipo_descendiente} con {menor_puntaje} puntos.")
    print(f"El equipo que mas partidos empato es {equipo_mayor_empates} con {mayor_empates} partidos.")
    print(f"El equipo con mejor proporcion goleadora es {equipo_mejor_ratio} con {ratio_goles}.")
    
    
    
#estadisticas_torneo({"boca":(9,1,0,15,3), "river":(3,3,4,6,15)})