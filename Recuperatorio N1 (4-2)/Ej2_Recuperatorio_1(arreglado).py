"""
Escribir un programa, compuesto por funciones, que permita:

a) Ingresar, en un diccionario, pares de datos con una clave que será el legajo de un alumno y un entero entre 4 y 10
que será la nota final de alguna materia aprobada. El ingreso estará en forma desordenada y un mismo legajo puede ingresarse
varias veces. 

b) Para cada alumno calcular su promedio, y luego listar los datos ordenados por promedio de mayor a menor.

c) Listar los datos ordenados de mayor a menor por cantidad de materias aprobadas.
"""

#-----------------------------------------------------------------------------------------------------------------------------#

def Ingresar_datos():
    
    NOTA_MIN = 4
    NOTA_MAX = 10
    
    NOTA = 0
    CANT_MATERIAS = 1
    
    dicc_alumnos = {}
    seguir = "si"
    
    while seguir == "si":
        legajo = input("Legajo: ")
        nota = int(input("Nota: "))
        
        while nota < NOTA_MIN or nota > NOTA_MAX:
            nota = int(input("Error.\n Nota: "))
        
        if legajo in dicc_alumnos:
            dicc_alumnos[legajo][NOTA] += nota
            dicc_alumnos[legajo][CANT_MATERIAS] += 1
            
        else:
            dicc_alumnos[legajo] = [nota, 1]
        
        seguir = input ("Seguir? (si/no): ")
        
    return dicc_alumnos

#-----------------------------------------------------------------------------------------------------------------------------#

def orden_promedios (dicc_alumnos):
    NOTA_TOTAL = 0
    CANT_MATERIAS = 1
    
    PROMEDIO = 1
      
    dicc_promedios = {}
    
    for alumno in dicc_alumnos:
        dicc_promedios[alumno] = dicc_alumnos[alumno][NOTA_TOTAL]/dicc_alumnos[alumno][CANT_MATERIAS]
    
    prom_ordenados = sorted(dicc_promedios.items(), key = lambda alumno:alumno[PROMEDIO], reverse = True)
    
    for alumno, promedio in prom_ordenados:
        print(f" Legajo: {alumno} - Promedio: {promedio} ")
        
    print("\n")    

#-----------------------------------------------------------------------------------------------------------------------------#

def orden_cantidad_mat (dicc_alumnos):
    CANT_MATERIAS = 1
 
    cant_mat_ordenadas = sorted(dicc_alumnos.items(), key = lambda alumno:alumno[CANT_MATERIAS], reverse = True)
    
    for alumno, datos in cant_mat_ordenadas:
        print(f" Legajo: {alumno} - Promedio: {datos[CANT_MATERIAS]} ")    

#-----------------------------------------------------------------------------------------------------------------------------#    

def main ():
    
    dicc_alumnos = Ingresar_datos()
    orden_promedios (dicc_alumnos)
    orden_cantidad_mat (dicc_alumnos)
    
main()