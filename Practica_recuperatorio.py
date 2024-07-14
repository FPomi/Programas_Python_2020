"""
Parcial algo
4)
def zanahoria(precios):
    
    lista_precios = precios.split()
    
    Precio_ZANAHORÍN = int(lista_precios[0])
    Precio_ZANAHORÓN = int(lista_precios[1])
    
    if Precio_ZANAHORÍN < Precio_ZANAHORÓN:
        print ("ZANAHORÍN")
    elif Precio_ZANAHORÍN > Precio_ZANAHORÓN:
        print("ZANAHORÓN")
    else:
        print("DA IGUAL")
    
    
def main():
    precios = "3 1"
    zanahoria(precios)
    
main()

"""
#----------------------------------------------------------------------------------------------------------------------------#

"""
Recuperatorio 1
4)

#----------------------------------------------------------------------------------------------------------------------------#
#dic_procto = {cod.producto : [nombre producto, cantidad producto en cm3, cantidad producida en cm3]}
dic_productos = {"100": ["Humectante clásica", 0, 0], "200": ["Antiage colageno", 0, 0], "300": ["Facial con UV", 0, 0], "400": ["Desmaquillante", 0, 0], "10": ["Vitamina A", 0, 0]}
#----------------------------------------------------------------------------------------------------------------------------#

def ingreso_cm3 (dic_productos):
    for cod_producto in dic_productos:
        print("\n", dic_productos[cod_producto][0])
        dic_productos[cod_producto][1] = int(input("Ingrese la cantidad (en cm3) disponible: "))
    
    envases_200cm3 = 0
    envases_500cm3 = 0
    envases_1000cm3 = 0
    
    produccion (dic_productos, envases_200cm3, envases_500cm3, envases_1000cm3)

#----------------------------------------------------------------------------------------------------------------------------#

def produccion (dic_productos, envases_200cm3, envases_500cm3, envases_1000cm3):
     
    seguir = "si"
    
    while (seguir == "si"): 
        crema_utilizada = input("\n Codigo de crema a usar: ")
        cant_a_utilizar = int(input("Cantidad de crema a usar (en cm3): "))
        tipo_envase = int(input("Tipo de envase a usar (en cm3): "))
    
        if (dic_productos[crema_utilizada][1] < cant_a_utilizar):
            print ("Cantidad de crema a usar mayor que la disponible, ingrese los datos de nuevo")
            produccion (dic_productos)
        
        dic_productos[crema_utilizada][1] -= cant_a_utilizar
        dic_productos[crema_utilizada][2] = cant_a_utilizar
        
        cant_envases_producida = int(cant_a_utilizar/tipo_envase)
        
        if (tipo_envase == 200):
            envases_200cm3 += cant_envases_producida
        elif (tipo_envase == 500):
            envases_500cm3 += cant_envases_producida
        else:
            envases_1000cm3 += cant_envases_producida
        
        seguir = input ("Desea producir otro producto? (si/no): ")
    
    conclusiones (dic_productos, envases_200cm3, envases_500cm3, envases_1000cm3)

#----------------------------------------------------------------------------------------------------------------------------#
   
def conclusiones (dic_productos, envases_200cm3, envases_500cm3, envases_1000cm3):    
    
    cant_mas_producida = 0
    
    for cod_producto in dic_productos:
        if (dic_productos[cod_producto][2] > cant_mas_producida):
            codigo_mas_producido = cod_producto
            nombre_mas_producido = dic_productos[cod_producto][0]
            cant_mas_producida = dic_productos[cod_producto][2]
            
    print("\n\nCrema mas producida:", codigo_mas_producido, "-", nombre_mas_producido)
    
    if (envases_200cm3 >= envases_500cm3 and envases_200cm3 >= envases_1000cm3):
        print ("Envase mas producido: 200 cm3\n")
    elif (envases_500cm3 >= envases_200cm3 and envases_500cm3 >= envases_1000cm3):
        print ("Envase mas producido: 500 cm3\n")
    else:
        print ("Envase mas producido: 1000 cm3\n")
    
    for cod_producto in dic_productos:
        print ("Sobrante de", dic_productos[cod_producto][0], "=", dic_productos[cod_producto][1], "cm3")

#----------------------------------------------------------------------------------------------------------------------------#

ingreso_cm3(dic_productos)
    
"""
#----------------------------------------------------------------------------------------------------------------------------#

"""
Recuperatorio n1
5) 
MAX_PALABRAS = 5

def ingresar_palabras ():
    
    lista_palabras = []
    
    palabra_clave = input("Palabra Clave: ")
    print ("Ingrese sus otras 5 palabras:")
    
    for num_palabra in range(MAX_PALABRAS):
        lista_palabras.append(input ())
        
    comparar_palabras(lista_palabras, palabra_clave)

#----------------------------------------------------------------------------------------------------------------------------#

def comparar_palabras (lista_palabras, palabra_clave):
    
    for palabra_comparar in lista_palabras:
        
        letras_palabra_comparar = []
        
        for letra in palabra_comparar:
            letras_palabra_comparar.append(letra)
            
        if len(palabra_clave) == len(palabra_comparar):
            #print(palabra_comparar, "se puede utilizar") 
            
            for letra in palabra_clave:
                if letras_palabra_comparar.count(letra) > 0:
                    letras_palabra_comparar.remove(letra)
                
            if letras_palabra_comparar == []:
                print(palabra_comparar,"se puede utilizar")                
        #else:
            #print(palabra_comparar, "no se puede utilizar")
 
ingresar_palabras()
    
#----------------------------------------------------------------------------------------------------------------------------# 
"""
#----------------------------------------------------------------------------------------------------------------------------# 
 
"""
Recuperaorio n2
2) 

def descomponer_dinero():
    
    Lista_valores = [10,20,50,100,200,500,1000]
    Diccionario_valores = {10:0, 20:0, 50:0, 100:0, 200:0, 500:0, 1000:0}
    
    print ("Lista =", Lista_valores)
    Valor = int(input("Valor: "))
    
    if Valor%2 != 0:
        print("No se puede descomponer este valor, ingrese otro\n")
        descomponer_dinero()
    
    Lista_valores.reverse()
    
    for Valor_lista in Lista_valores:
        
        while (Valor > 0):
            Valor = Valor - Valor_lista
            Diccionario_valores[Valor_lista] += 1
            
        if (Valor < 0):
            Valor = Valor + Valor_lista
            Diccionario_valores[Valor_lista] -= 1
    
    print (Diccionario_valores)
    
    
descomponer_dinero ()    
"""