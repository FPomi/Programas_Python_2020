"""
Escribir un programa, compuesto por funciones, que permita:

a) Ingresar, en un diccionario, pares de datos con una clave que será el legajo de un alumno y un entero entre 4 y 10
que será la nota final de alguna materia aprobada. El ingreso estará en forma desordenada y un mismo legajo puede ingresarse
varias veces. 

b) Para cada alumno calcular su promedio, y luego listar los datos ordenados por promedio de mayor a menor.

c) Listar los datos ordenados de mayor a menor por cantidad de materias aprobadas.
"""

NO = 0
SI = 1

def ingreso_datos ():
    lista_alumnos = []
    seguir = "SI"
    
    while (seguir == "SI"):
        legajo = input ("\nIngresar legajo: ")
        nota = input ("Ingresar nota:")

        lista_alumnos.append ([legajo, nota])
        
        #print (lista_alumnos)
        
        seguir = input ("Quiere seguir (SI/NO): ")

    crear_diccionario (lista_alumnos)
    
    
def crear_diccionario (lista_alumnos):
    dic_alumnos = {}
    
    for alumno in lista_alumnos:
        
        if alumno[0] not in dic_alumnos:
            dic_alumnos[alumno[0]] = alumno[1]
        else:
            dic_alumnos[alumno[0]].append(alumno[1])
            
    print(dic_alumnos)
    
        
ingreso_datos()