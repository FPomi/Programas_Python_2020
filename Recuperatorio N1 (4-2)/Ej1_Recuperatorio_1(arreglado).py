"""Escribir una función que, dado un texto que se pasa por parámetro, devuelva el valor booleano verdadero si todas las
palabras tienen 6 letras o menos, caso contrario devuelve falso. Las palabras están separadas solo por blancos. Optimizar."""
#-----------------------------------------------------------------------------------------------------------------------------#
NUM_MAX_LETRAS = 6
texto = "Buenas tardes"
#-----------------------------------------------------------------------------------------------------------------------------#

def contar_letras (texto):
    
    for palabra in texto.split():
        if len(palabra) > NUM_MAX_LETRAS:
            break
        
    return False if (palabra != texto.split()[-1]) else True

#-----------------------------------------------------------------------------------------------------------------------------#

def main ():
    print(contar_letras (texto))

#-----------------------------------------------------------------------------------------------------------------------------#

main()