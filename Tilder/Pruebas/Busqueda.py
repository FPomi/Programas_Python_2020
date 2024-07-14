import os
import pickle
import random
import math

import Chats
import Distancia_Calculo
import Diseño

from time import sleep

#-----------------------------------------------------------------------------------------------------------------------------#

def edad_min():
    
    EDAD_MIN = 18
    EDAD_MAX = 99
    
    edad_min = 0
    
    print('|------------------------------------------------------------------------------------------------------------|')
    print('|------------------------------------------------------------------------------------------------------------|')
    print("\t Puede presionar '<' en cualquier momento para volver al menú")
    print('|------------------------------------------------------------------------------------------------------------|')
    print('|------------------------------------------------------------------------------------------------------------|')
    print(" Las edades legales son de 18 años a 99 años.\n - [A] Aleatorio")

    while edad_min != "<" and (type(edad_min) == str or int(edad_min) < EDAD_MIN or int(edad_min) > EDAD_MAX):

        edad_min = input(" Seleccione la edad mínima de la persona con la que quiera contactarse: ")
        
        if not edad_min:
            edad_min = 0
            print ("\nOpcion invalida - Intenta otra vez")
        
        elif edad_min.lower() == "a":
            edad_min = random.randint(EDAD_MIN, EDAD_MAX)
        
        elif edad_min.isnumeric():
            edad_min = int(edad_min)
            if edad_min < EDAD_MIN or edad_min > EDAD_MAX:
                print ("\nOpcion invalida - Intenta otra vez")
                edad_min = 0
                
    return edad_min

#-----------------------------------------------------------------------------------------------------------------------------#

def edad_max(edad_min):
    
    EDAD_MIN = edad_min
    EDAD_MAX = 99
    
    edad_max = 0
    
    print('|------------------------------------------------------------------------------------------------------------|')
    print(f" La edad máxima debe ser mayor o igual a {edad_min} y menor o igual a 99 años.\n - [A] Aleatorio")

    while edad_max != "<" and (type(edad_max) == str or int(edad_max) < EDAD_MIN or int(edad_max) > EDAD_MAX):

        edad_max = input(" Seleccione la edad máxima de la persona con la que quiera contactarse: ")
        
        if not edad_max:
            edad_max = 0
            print ("\nOpcion invalida - Intenta otra vez")
        
        elif edad_max.lower() == "a":
            edad_max = random.randint(EDAD_MIN, EDAD_MAX)
        
        elif edad_max.isnumeric():
            edad_max = int(edad_max)
            if edad_max < EDAD_MIN or edad_max > EDAD_MAX:
                print ("\nOpcion invalida - Intenta otra vez")
                edad_max = 0
                
    return edad_max

#-----------------------------------------------------------------------------------------------------------------------------#

def radio_de_busqueda():
    
    RADIO_MIN = 0
    RADIO_MAX = 23000
    
    radio = -1
    
    print('|------------------------------------------------------------------------------------------------------------|')
    print(' - [A] Aleatorio')

    while radio != "<" and (type(radio) == str or float(radio) < RADIO_MIN or float(radio) > RADIO_MAX):

        radio = input(" Indique cual es la máxima distancia en km a la que puede vivir la persona con la que quiera contactarse: ")
        
        if not radio:
            print ("\nOpcion invalida - Intenta otra vez")
            radio = -1
        
        elif radio.lower() == "a":
            radio = random.uniform(RADIO_MIN, RADIO_MAX)
        
        elif radio.isnumeric():
            radio = float(radio)
            if radio < RADIO_MIN or radio > RADIO_MAX:
                print ("\nOpcion invalida - Intenta otra vez")
                radio = -1
                
    return radio

#-----------------------------------------------------------------------------------------------------------------------------#

def sexo_de_interes(): 
    sexos = ["m","h","i"]
    
    print('|------------------------------------------------------------------------------------------------------------|')
    print(' Los sexos válidos son Hombre [H], Mujer [M], o Indefinido [I]\n - [A] Aleatorio')
    
    sexo = input(" Indique su sexo de interés [H] / [M] / [I]: ")

    while sexo != "<" and sexo.lower() not in sexos and sexo.lower() != "a" :
        
        print ("\nOpcion invalida - Intenta otra vez")
        sexo = input(" Indique su sexo de interés [H] / [M] / [I]: ")
        
        if not sexo:
            sexo = "0"
            
    if sexo.lower() == "a":
        sexo = random.choice(sexos)
        
    return sexo

#-----------------------------------------------------------------------------------------------------------------------------#

def ingresar_parametros():
    
    os.system('cls||clear')

    edad_minima = edad_min()
    if edad_minima == "<":
        resultado = 0
    else:
        edad_maxima = edad_max(edad_minima)
        if edad_maxima == "<":
            resultado = 0
        else:
            radio = radio_de_busqueda()
            if radio == "<":
                resultado = 0
            else:
                sexo = sexo_de_interes()
                if sexo == "<":
                    resultado = 0
                else:
                    resultado = [edad_minima, edad_maxima, radio, sexo]
    return resultado
    
#-----------------------------------------------------------------------------------------------------------------------------#

def buscar(usuarios, parametros, pseudonimo_usuario):
    edad_min, edad_max, radio, sexo = parametros
    for usuario in usuarios.keys():
        if usuario != pseudonimo_usuario and usuario not in usuarios[pseudonimo_usuario][-3]:
            nombre, apellido, contra, sexo_usuario, edad, ubicacion, intereses, _, _, _ = usuarios[usuario]
            distancia = Distancia_Calculo.calculo_distancia(ubicacion, usuarios[pseudonimo_usuario][5])

            if edad_min <= edad <= edad_max and sexo.upper() == sexo_usuario.upper() and distancia <= radio:
                resultado_intereses = calcular_porcentaje_de_interes(usuarios, pseudonimo_usuario, usuario)
                mostrar_persona(usuarios[usuario], distancia, resultado_intereses)
                likear(usuarios, pseudonimo_usuario, usuario)

#-----------------------------------------------------------------------------------------------------------------------------#

def likear(usuarios, pseudonimo_usuario, pseudonimo_matcheo):
    
    matcheo = input(' ¿Te interesa esta persona? ("Si"/"No"): ')
    
    while matcheo.lower() not in ["si", "no"]:
        matcheo = input("Opción inválida, por favor ingresa Si o No: ")
    
    if matcheo.lower() == "si":
        usuarios[pseudonimo_usuario][-3].append(pseudonimo_matcheo)
        if pseudonimo_usuario in usuarios[pseudonimo_matcheo][-3]:
            usuarios[pseudonimo_usuario][-2][pseudonimo_matcheo] = " "
            usuarios[pseudonimo_matcheo][-2][pseudonimo_usuario] = " " 

            nombre_matcheo = usuarios[pseudonimo_matcheo][0]
            
            print ("\n Parece que encontraste un match ( ͡~ ͜ʖ ͡°)")
            abrir_chat = str(input(f"¿Desea abrir tu chat con {nombre_matcheo}? (Si/No): ").lower())

            while abrir_chat != "si" and abrir_chat !="no":
                abrir_chat = str(input("Opción inválida, por favor ingresa Si o No: ").lower())
    
            if abrir_chat == "si":
                Chats.chat(usuarios, pseudonimo_usuario, pseudonimo_matcheo)

#-----------------------------------------------------------------------------------------------------------------------------#
        
def mostrar_sexo(sexo_usuario):
    if sexo_usuario in ["M","m"]:
        sexo = "Mujer"
    elif sexo_usuario in ["H","h"]:
        sexo = "Hombre"
    elif sexo_usuario in ["I", "i"]:
        sexo = "Indefinido"
    return sexo

#-----------------------------------------------------------------------------------------------------------------------------#

def mostrar_persona(datos, distancia, resultado_interes):
    nombre, apellido, contra, sexo_usuario, edad, ubicacion, intereses, likes, chats, foto = datos

    print('|----------------------------------------------------------------------------------------------------------------|')
    print(f" {Diseño.foto_derecha_superior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_superior}")
    print(f" {Diseño.marco_vertical}{foto}{Diseño.marco_vertical}")
    print(f" {Diseño.foto_derecha_inferior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_inferior}")
    print(f" {apellido}, {nombre}. {mostrar_sexo(sexo_usuario)}, {edad} años. A {distancia} km.")
    print(f"  El porcentaje de interés compartido con {nombre} es del {resultado_interes}%.")

#-----------------------------------------------------------------------------------------------------------------------------#

def calcular_porcentaje_de_interes(usuarios, pseudonimo_usuario, pseudonimo_matcheo):
    intereses_usuario = usuarios[pseudonimo_usuario][-4]
    intereses_matcheo = usuarios[pseudonimo_matcheo][-4]
    intereses_totales = len(intereses_usuario) + len(intereses_matcheo)
    intereses_en_comun = 0

    if intereses_totales == 0:
        porcentaje_de_interes = 0

    else:
        for interes in intereses_usuario:
            if interes in intereses_matcheo:
                intereses_en_comun += 1
 
        porcentaje_de_interes = round((intereses_en_comun / intereses_totales) * 100)

    return porcentaje_de_interes

#-----------------------------------------------------------------------------------------------------------------------------#

def usuario_no_encontrado():
    
    (sleep(1))
    
    print("|----------------------------------------------------------------------------------------------------------------|")
    print("¡Ups! Parece que no encontramos usuarios para mostrarle...")

    volver = ""
    volver_menu = [1, "uno", "Uno", "UNO"]
    busqueda_personas = [2, "dos", "Dos", "DOS"]
    volver_opciones = volver_menu+busqueda_personas

    while volver not in volver_opciones:

        print(" \n [1] Para volver al menú\n [2] Para volver a buscar personas\n ")
        volver = input("Ingrese una de las dos opciones: ")

        if volver.isnumeric():
            volver = int(volver)

        if volver in volver_menu:
            finalizar_busqueda = True

        elif volver in busqueda_personas:
            finalizar_busqueda = False

    return finalizar_busqueda

#-----------------------------------------------------------------------------------------------------------------------------#

def main_busqueda(pseudonimo_usuario):
    usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    finalizar_busqueda = False

    while not finalizar_busqueda:
        parametros_de_busqueda = ingresar_parametros()
        if parametros_de_busqueda == 0:
            finalizar_busqueda = True
        else:
            buscar(usuarios, parametros_de_busqueda, pseudonimo_usuario)
            finalizar_busqueda = usuario_no_encontrado()
    
    pickle.dump(usuarios, open("Datos_Usuarios_Final.pkl", "wb"))
    
#-----------------------------------------------------------------------------------------------------------------------------#
