"""Escribir una función que, dado un texto que se pasa por parámetro, devuelva el valor booleano verdadero si todas las
palabras tienen 6 letras o menos, caso contrario devuelve falso. Las palabras están separadas solo por blancos. Optimizar."""
#-----------------------------------------------------------------------------------------------------------------------------#
NUM_MAX_LETRAS = 6
#-----------------------------------------------------------------------------------------------------------------------------#

def contar_letras (texto):
    contador = 0
    
    lista_texto = texto.split()
    
    for palabra in lista_texto:
        if len(palabra) > NUM_MAX_LETRAS:
            contador += 1
    
    return False if (contador > 0) else True

#-----------------------------------------------------------------------------------------------------------------------------#

def main ():
    texto = "Buenas tardes"
    print(contar_letras (texto))

#-----------------------------------------------------------------------------------------------------------------------------#

main()