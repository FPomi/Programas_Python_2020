"""
Escribir una funcion en Python, para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave candidata, previamente ingresada por el usuario.
Devolvera true o false, dependiendo de si cumple o no, con las siguientes condiciones:

- La clave debe estar formada unicamente por, entre 4 y 8 caracteres numericos
- Tener al menos un caracter numerico impar y uno par

Ejemplos a validar:

validar("j2021") devuevle False
validar("2021a") devuevle False
validar("20X21") devuevle False
validar("2020") devuelve False
validar("23445776") devuelve True
validar("089") devuelve False
validar("027845321") devuelve False
validar("02784532") devuelve True

Para validar, escribí un programa que cree una lista, con las cadenas a validar, y
luego invoque a la función por cada una de las cadenas, mostrando el resultado correspondiente para cada una de ellas.
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def validar_clave (clave):
    
    LARGO_MIN = 4
    LARGO_MAX = 8
    
    es_par = 0
    es_impar = 0
    
    if (clave.isnumeric() == True) and (len(clave) >= LARGO_MIN) and (len(clave) <= LARGO_MAX):
        for numero in clave:
            if int(numero) % 2 == 0:
                es_par += 1
            else:
                es_impar += 1
    
    return False if (len(clave) < LARGO_MIN) or (len(clave) > LARGO_MAX) or (clave.isnumeric() == False) or (es_par == 0) or (es_impar == 0)  else True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def crear_claves():
    lista_claves = []
    seguir = "si"
    
    while seguir == "si":
        clave = input ("Cadena a validar: ")
        lista_claves += [clave]
        seguir = input ("Seguir? (si/no): ")
        
    for clave_ in lista_claves:
        print (f"La cadena {clave_} devuelve {validar_clave (clave_)}")
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

crear_claves()
