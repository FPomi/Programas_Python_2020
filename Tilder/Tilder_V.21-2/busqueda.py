import pickle
import random
import math
from time import sleep
import chat


# Se calcula la distancia entre latitudes y longitudes, a partir de eso se pasa a km y se redondea

def calculo_distancia(latitud_usuario_principal,longitud_usuario_principal,latitud_usuario_prueba,longitud_usuario_prueba):

  distancia_latitud = latitud_usuario_prueba - latitud_usuario_principal
  distancia_longitud = longitud_usuario_prueba - longitud_usuario_principal

  a = math.sin(distancia_latitud/2)**2 + math.cos(latitud_usuario_principal) * math.cos(latitud_usuario_prueba) * math.sin(distancia_longitud/2)**2
  c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
  distancia_en_km = 6371 * c
  distancia_en_km = round(distancia_en_km)
  
  return distancia_en_km



def edad_min():
    edad_min = 0
    while type(edad_min) == str or int(edad_min) < 18 or int(edad_min) > 99:

        print('|-----------------------------------------------------|')
        print(" La edad mínima legal es de 18 años.\n - [A] Aleatorio")

        edad_min = input(" Seleccione la edad mínima de la persona con la que quiera contactarse: ")
        if not edad_min:
            edad_min = 0
        elif edad_min.lower() == "a":
            edad_min = random.randint(18,99)
        elif edad_min.isnumeric():
            edad_min = int(edad_min)
            if edad_min < 18 or edad_min > 99:
                edad_min = 0
    return edad_min


def edad_max():            
    edad_max = 0
    while type(edad_max) == str or int(edad_max) < 18 or int(edad_max) > 99:

        print('|------------------------------------------------------------------------------|')
        print(f" La edad máxima debe ser mayor o igual a 18 años, y menor o igual a 99 años.\n - [A] Aleatorio")

        edad_max = input(" Seleccione la edad máxima de la persona con la que quiera contactarse: ")
        if not edad_max:
            edad_max = 0
        elif edad_max.lower() == "a":
            edad_max = random.randint(18,99)
        elif edad_max.isnumeric():
            edad_max = int(edad_max)
            if edad_max < 18 or edad_max > 99:
                edad_max = 0
    return edad_max


def radio_de_busqueda():
    radio = -1
    while type(radio) == str or float(radio) < 0 or float(radio) > 23000:

        print('|-------------------------------------------------------------------------------|')
        print(' - [A] Aleatorio')

        radio = input(" Indique cual es la máxima distancia en km a la que puede vivir la persona con la que quiera contactarse: ")
        if not radio:
            radio = -1
        elif radio.lower() == "a":
            radio = random.uniform(0,23000)
        elif radio.isnumeric():
            radio = float(radio)
            if radio < 0 or radio > 23000:
                radio = -1
    return radio


def sexo_de_interes(): 
    sexo = "0"
    sexos = ["m","h","i"]
    while sexo.lower() not in sexos:

        print('|------------------------------------------------------------------------------------|')
        print(' Los sexos válidos son Hombre ("H"), Mujer ("M"), o Indefinido ("I")\n - [A] Aleatorio')

        sexo = input(" Indique su sexo de interés (H/M/I): ")
        if not sexo:
            sexo = "0"
        elif sexo.lower() == "a":
            sexo = random.choice(sexos[0:-2])
        
    return sexo


def ingresar_parametros():
    edad_minima = edad_min()
    edad_maxima = edad_max()
    radio = radio_de_busqueda()
    sexo = sexo_de_interes()

    return [edad_minima, edad_maxima, radio, sexo]
    

def buscar(usuarios, parametros, pseudonimo_usuario):
    edad_min, edad_max, radio, sexo = parametros
    for usuario in usuarios.keys():
        if usuario != pseudonimo_usuario and usuario not in usuarios[pseudonimo_usuario][-2]:
            nombre, apellido, contra, sexo_usuario, edad, ubicacion, intereses, _, _ = usuarios[usuario]
            distancia = Distancia_Calculo.calculo_distancia(ubicacion, usuarios[pseudonimo_usuario][5])

            if edad_min <= edad <= edad_max and sexo.lower() == sexo_usuario.lower() and distancia <= radio:
                resultado_intereses = calcular_porcentaje_de_interes(usuarios, pseudonimo_usuario, usuario)
                mostrar_persona(usuarios[usuario], distancia, resultado_intereses)
                likear(usuarios, pseudonimo_usuario, usuario)


def likear(usuarios, pseudonimo_usuario, pseudonimo_matcheo):
    matcheo = "0"
    while matcheo.lower() not in ["si", "no"]:
        matcheo = str(input(' ¿Te interesa esta persona? ("Si"/"No"): '))             
        if not matcheo:
            matcheo = "0"
    
    if matcheo.lower() == "si":
        usuarios[pseudonimo_usuario][-2].append(pseudonimo_matcheo)
        if pseudonimo_usuario in usuarios[pseudonimo_matcheo][-2]:
            usuarios[pseudonimo_usuario][-1][pseudonimo_matcheo] = " "
            usuarios[pseudonimo_matcheo][-1][pseudonimo_usuario] = " " 

            nombre_matcheo = usuarios[pseudonimo_matcheo][0]

            abrir_chat = str(input(f"¿Desea abrir su chat con {nombre_matcheo}?(Si/No): ").lower())

            while abrir_chat != "si" and abrir_chat !="no":
                abrir_chat = str(input("Opción inválida, por favor ingrese Si o No: ").lower())
    
            if abrir_chat == "si":
                chat.chat(usuarios, pseudonimo_usuario, pseudonimo_matcheo)

        
def mostrar_sexo(sexo_usuario):
    if sexo_usuario == "m":
        sexo = "Mujer"
    if sexo_usuario == "h":
        sexo = "Hombre"
    if sexo_usuario == "i":
        sexo == "Indefinido"
    return sexo


def mostrar_persona(datos, distancia, resultado_interes):
    nombre, apellido, contra, sexo_usuario, edad, ubicacion, intereses, likes, chats = datos

    print('|------------------------------------------------------------------------------------|')
    print(f" {apellido}, {nombre}. {mostrar_sexo(sexo_usuario)}, {edad} años. A {distancia} km.")
    print(f"  El porcentaje de interés compartido con {nombre} es del {resultado_interes}%.")


def calcular_porcentaje_de_interes(usuarios, pseudonimo_usuario, pseudonimo_matcheo):
    intereses_usuario = usuarios[pseudonimo_usuario][-3]
    intereses_matcheo = usuarios[pseudonimo_matcheo][-3]
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


def usuario_no_encontrado():
    (sleep(2))
    print("|------------------------------------------------------------------------------------|")
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


def main_busqueda(pseudonimo_usuario):
    usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    finalizar_busqueda = False

    while not finalizar_busqueda:
        parametros_de_busqueda = ingresar_parametros()
        buscar(usuarios, parametros_de_busqueda, pseudonimo_usuario)
        finalizar_busqueda = usuario_no_encontrado()

    pickle.dump(usuarios, open("Datos_Usuarios_Final.pkl", "wb"))

