import os
import random
import pickle

import Diseño
import Chats

from time import sleep

#-----------------------------------------------------------------------------------------------------------------------------#
    
def ingresar_usuario():
### Del ingreso del usuario, vamos a extraer como dato su pseudónimo, porque nos va a servir para sacar información más adelante
    
    diccionario_usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))

    print('|------------------------------------------------|')
    print("Para regresar presione Enter")
    
    pseudonimo_ingreso = input(" Pseudonimo: ")
    if(pseudonimo_ingreso == ""): menu_principal()
        
    contraseña_ingreso = input (" Contraseña: ")
    if(contraseña_ingreso == ""): menu_principal()

    try:
        contraseña_en_diccionario = diccionario_usuarios[pseudonimo_ingreso][2]

        if (pseudonimo_ingreso not in diccionario_usuarios) or ((contraseña_en_diccionario != contraseña_ingreso) or (contraseña_ingreso == "\0" )):
            print(" Cuenta o contraseña inválida, por favor vuelva a ingresar sus datos.")
            pseudonimo_ingreso = ingresar_usuario()

        else:
            print("\n\t\tHa ingresado con éxito.")

    except KeyError:
        print(" Cuenta o contraseña inválida, por favor vuelva a ingresar sus datos.")
        pseudonimo_ingreso = ingresar_usuario()

    
    return pseudonimo_ingreso

#-----------------------------------------------------------------------------------------------------------------------------#

def menu_usuario(pseudonimo_ingreso):
    
    os.system('cls||clear')
    
    uno = ["1", "uno", "Uno", "UNO"]
    dos = ["2", "dos", "Dos", "DOS"]
    tres = ["3", "tres", "Tres", "TRES"]
    cuatro = ["4", "cuatro", "Cuatro", "CUATRO"]
    opciones_posibles = uno + dos + tres + cuatro
    opcion_funcion = ""
    
    print('|-----------------------------------------------------------|\n\n\t\tMENÚ TILDER\n')
    print("\t\t[1] Mis chats\n\t\t[2] Búsqueda de personas\n\t\t[3] Mi perfil\n\t\t[4] Cerrar sesión ")
    
    opcion = input("\n Seleccione una de las cuatro opciones mostradas: ")

    while opcion not in opciones_posibles:
        opcion = input("\n Opcion invalida, intente nuevamente: ")

    if opcion in uno:
        opcion_funcion = "Menu de chats"
                
    elif opcion in dos:
        opcion_funcion = "Menu de busqueda"
                
    elif opcion in tres:
        opcion_funcion = "Mi perfil"
    
    elif opcion in cuatro:
        opcion_funcion = "Cerrar sesion"
        
    return opcion_funcion

#-----------------------------------------------------------------------------------------------------------------------------#

def menu_principal():

    # Primero se cargan los datos de Grupo_Prueba y Matcheos
    # Al inicio del programa tenemos la opción para iniciar sesión o crear nueva cuenta, luego de ambos procesos nos manda al menu
    
    os.system('cls||clear')
    
    print(Diseño.tilder)
    
    (sleep(3))
    
    uno = ["1", "uno", "Uno", "UNO"]
    dos = ["2", "dos", "Dos", "DOS"]
    tres = ["3", "tres", "Tres", "TRES"]
    opciones_posibles = uno + dos + tres

    print('|----------------------------------------------------------------------|\n\n\t\t¡Bienvenido a Tilder!\n')
    print("\t\t[1] Iniciar Sesión\n\t\t[2] Crear una nueva cuenta\n\t\t[3] Salir del programa\n")
    opcion = input("\n   Seleccione una de las opciones mostradas: ")

    while opcion not in opciones_posibles:
        opcion = input("\n   Opcion invalida, intente nuevamente: ")

    if opcion in uno:
        pseudonimo_ingreso = ingresar_usuario()
                
    elif opcion in dos:
        from Crear_nueva_sesion import nueva_persona
            
        pseudonimo_ingreso = nueva_persona() # Acá nueva_persona debería retornar el usuario recién creado 
    
    elif opcion in tres:
        pseudonimo_ingreso = "0"
    
    return pseudonimo_ingreso
    
#menu_principal()
