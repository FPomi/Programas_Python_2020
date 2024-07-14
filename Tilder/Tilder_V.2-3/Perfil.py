import pickle

import Menus_de_inicio
import Diseño
import Crear_nueva_sesion

from os import system
from time import sleep
from Busqueda import mostrar_sexo

#-----------------------------------------------------------------------------------------------------------------------------#

def perfil_mostrar_datos(diccionario_usuarios, pseudonimo_ingreso):
    
    datos_pseudonimo_ingreso = diccionario_usuarios[pseudonimo_ingreso]

    foto = datos_pseudonimo_ingreso[9]
    print(f"\t\t{Diseño.foto_derecha_superior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_superior}\n\t [1] \t{Diseño.marco_vertical}{foto}{Diseño.marco_vertical}\n\t\t{Diseño.foto_derecha_inferior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_inferior}")

    opcion_mostrada = 1

    for dato in datos_pseudonimo_ingreso[0:7]:

        opcion_mostrada += 1

        cambiar_contraseña = 4
        cambiar_sexo = 5
        cambiar_edad = 6
        cambiar_ubicacion = 7
        cambiar_intereses = 8

        if opcion_mostrada == cambiar_contraseña:
            dato = "Cambiar contraseña"
        
        elif opcion_mostrada == cambiar_sexo:

            dato = dato.upper()
            dato = 'Sexo: ' + mostrar_sexo(dato)
            

        elif opcion_mostrada == cambiar_edad:
            dato = "Edad: " + str(dato) + " años"

        elif opcion_mostrada == cambiar_ubicacion:

            mostrar_ubicacion = "Ubicación: "

            latitud, longitud = dato

            dato = mostrar_ubicacion + str(latitud) + "," + str(longitud)

        elif opcion_mostrada == cambiar_intereses:

            mostrar_intereses = "Intereses: "

            for interes in dato:
                
                ultimo_interes = dato[-1] 

                if interes != ultimo_interes:
                    mostrar_intereses += interes + ", "
                else: mostrar_intereses += "" + interes
            

            dato = mostrar_intereses 

        print(f"\t\t{Diseño.perfil_costado_derecha_superior}{Diseño.perfil_horizontal*len(dato)}{Diseño.perfil_costado_izquierda_superior}\n\t [{opcion_mostrada}] \t{Diseño.perfil_vertical}{dato}{Diseño.perfil_vertical}\n\t\t{Diseño.perfil_costado_derecha_inferior}{Diseño.perfil_horizontal*len(dato)}{Diseño.perfil_costado_izquierda_inferior}")

#-----------------------------------------------------------------------------------------------------------------------------#

def mi_perfil(pseudonimo_ingreso):
    
    system('cls||clear')
    
    diccionario_usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))

    uno = [1, "uno"]
    dos = [2, "dos"]
    tres = [3, "tres"]
    cuatro = [4, "cuatro"]
    cinco = [5, "cinco"]
    seis = [6, "seis"]
    siete = [7, "siete"]
    ocho = [8, "ocho"]
    volver_menu = "<"
    opciones_posibles = uno + dos + tres + cuatro + cinco + seis + siete + ocho 
    opcion = 10

    while opcion != volver_menu and opcion not in opciones_posibles:

        perfil_mostrar_datos(diccionario_usuarios, pseudonimo_ingreso)

        opcion = input('Ingrese una de las opciones mostradas si desea editar su perfil, o "<" para volver al menú: ')

        if opcion.isnumeric(): opcion = int(opcion)

        if type(opcion) == str: opcion = opcion.lower()

        while opcion != volver_menu and opcion not in opciones_posibles:
            opcion = input("ERROR. Opción invalida, vuelva a intentar: ")
            if opcion.isnumeric(): opcion = int(opcion)
            if type(opcion) == str: opcion = opcion.lower()

        if opcion in uno: 
            
            foto_de_perfil = Crear_nueva_sesion.foto()
            diccionario_usuarios[pseudonimo_ingreso][9] = foto_de_perfil  

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)
        
        elif opcion in dos: 

            nombre = Crear_nueva_sesion.ingresar_nombre()
            diccionario_usuarios[pseudonimo_ingreso][0] = nombre

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)

        elif opcion in tres: 

            apellido = Crear_nueva_sesion.ingresar_apellido()
            diccionario_usuarios[pseudonimo_ingreso][1] = apellido

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso) 

        elif opcion in cuatro: 

            largo_minimo = 5
            ingreso_contraseña_actual = ""
            contraseña_actual_en_diccionario = diccionario_usuarios[pseudonimo_ingreso][2]

            intentos = 0

            while ingreso_contraseña_actual != contraseña_actual_en_diccionario and intentos < 3:
                
                ingreso_contraseña_actual = input('Ingrese su contraseña actual para poder cambiar la contraseña: ')
                intentos += 1

                if intentos == 3 and ingreso_contraseña_actual != contraseña_actual_en_diccionario:
                    print("Lo sentimos, debe esperar para volver a intentarlo.")
                    sleep(30)
                    intentos = 0

            password = Crear_nueva_sesion.contraseña()
            while len(password) < largo_minimo and not Crear_nueva_sesion.verf_contraseña(password):
                password = Crear_nueva_sesion.contraseña_incorrecta()

            diccionario_usuarios[pseudonimo_ingreso][2] = password

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)  
        
        elif opcion in cinco: 

            sexo = Crear_nueva_sesion.sexualidad()
            diccionario_usuarios[pseudonimo_ingreso][3] = sexo

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)  

        elif opcion in seis: 
            
            edad_minima = 18
            edad_maxima = 99

            edad = Crear_nueva_sesion.ingre_edad()

            while edad < edad_minima or edad > edad_maxima:
                edad = Crear_nueva_sesion.ingre_edad()

            diccionario_usuarios[pseudonimo_ingreso][4] = edad

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)

        elif opcion in siete: 

            coordenadas = Crear_nueva_sesion.ubicacion()
            diccionario_usuarios[pseudonimo_ingreso][5] = coordenadas

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso) 

        elif opcion in ocho: 

            intereses = Crear_nueva_sesion.etiquetas_de_interes()
            diccionario_usuarios[pseudonimo_ingreso][6] = intereses

            pickle.dump(diccionario_usuarios, open("Datos_Usuarios_Final.pkl","wb"))
            mi_perfil(pseudonimo_ingreso)

#-----------------------------------------------------------------------------------------------------------------------------#
