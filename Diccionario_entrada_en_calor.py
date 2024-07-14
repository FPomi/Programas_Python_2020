"""
numeros_al_cuadrado: Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden el rango de números
positivos tomando como límite superior el número que se recibió como parámetro, y donde para cada clave su valor asociado
será el número de la clave al cuadrado.
"""
def numeros_al_cuadrado(numero):
    dicc_al_cuadrado = {}
    
    for num_actual in range (1, numero+1):
        dicc_al_cuadrado[num_actual] = num_actual**2
    
    #print(diccionario_al_cuadrado)
    
    return dicc_al_cuadrado
    



"""
mezclar_diccionarios: Recibe dos diccionarios. Retorna un único diccionario, que resultad de realizar la mezcla entre
los dos. Las claves del nuevo diccionario deben ser las claves de ambos (asumir que no tienen claves iguales),
con sus respectivos valores.
"""

def mezclar_diccionarios(dicc_uno, dicc_dos):
    
    dicc_combinados = {}
    
    for posicion in dicc_uno:
        dicc_combinados [posicion] = dicc_uno[posicion]
        
    for posicion in dicc_dos:
        dicc_combinados [posicion] = dicc_dos[posicion]
    
    #print (dicc_combinados)
    
    return dicc_combinados
    
    
"""
filtrar_por_sumar_diez: Recibe un diccionario cuyas claves son enteros, y también su valor asociado.
Retorna un diccionario que contiene únicamente los pares clave-valor del diccionario que se recibió por
parámetro que al sumarlos sean mayores o iguales a 10.
"""
def filtrar_por_sumar_diez(diccionario):
    
    dicc_filtrado = {}
    
    for posicion in diccionario:
        if (posicion + diccionario[posicion]) >= 10:
            dicc_filtrado[posicion] = diccionario [posicion] 
    
    #print (dicc_filtrado)
    
    return dicc_filtrado
 
 
"""
ordenar_valores_por_longitud: Recibe un diccionario con claves de tipo string y valores asociados de tipo string.
Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada
descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.
"""
def ordenar_valores_por_longitud(diccionario):
    
    lista_ordenada = []
    
    lista_ordenada = sorted(diccionario.values(), key = lambda palabra : len(palabra), reverse = True)
    
    return lista_ordenada
