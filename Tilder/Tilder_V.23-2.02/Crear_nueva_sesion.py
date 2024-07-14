import os
import pickle

import Diseño

#-----------------------------------------------------------------------------------------------------------------------------#

def foto():

    diccionario_usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    fotos_a_mostrar = Diseño.galeria(diccionario_usuarios)

    uno = [1, "uno"]
    dos = [2, "dos"]
    opciones = uno + dos

    opcion_mostrada = 1
    
    for foto in fotos_a_mostrar:

        print(f"\t\t{Diseño.foto_derecha_superior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_superior}\n\t [{opcion_mostrada}] \t{Diseño.marco_vertical}{foto}{Diseño.marco_vertical}\n\t\t{Diseño.foto_derecha_inferior}{Diseño.marco_horizontal*(len(foto)-2)}{Diseño.foto_izquierda_inferior}")
        opcion_mostrada += 1

    opcion = input(" ♥Elija una foto de su galeria como foto de perfil: ")

    if opcion.isnumeric(): opcion = int(opcion)
    if type(opcion) == str: opcion = opcion.lower()
    
    while opcion not in opciones:
        opcion = input(" Disculpa, esa opcion no esta disponible, intenta otra: ")
        if opcion.isnumeric(): opcion = int(opcion)
        if type(opcion) == str: opcion = opcion.lower()
        
    if opcion in uno:
        foto_elegida = fotos_a_mostrar[0]

    elif opcion in dos:
        foto_elegida = fotos_a_mostrar[1]

    return foto_elegida

#-----------------------------------------------------------------------------------------------------------------------------#

def Pseudonimo(dicc_usuarios):
    
    pseudo = input("\n ♥Ingrese un Pseudonimo/Apodo para poder identificarte [Este debe ser unico, sin mayusculas o simbolos, excepto el guion bajo]\n Pseudonimo: ")
        
    while (pseudo in dicc_usuarios):
        pseudo = input(" ERROR. Parece que el Pseudonimo esta en uso (> ~ <) - Intenta con otro: ")

    caracter = 0
    while caracter != len(pseudo):
        if len(pseudo) == 0 or not pseudo[caracter].isalnum() or pseudo[caracter].isupper():
            if len(pseudo) == 0 or pseudo[caracter] != "_" or pseudo[caracter] == "":
                pseudo=input(" ERROR. Pseudonimo invalido - Ingrese uno nuevo: ")
                caracter = 0
            else:
                caracter += 1
        else:
            caracter +=1 
    
    return pseudo


#-----------------------------------------------------------------------------------------------------------------------------#

def ingresar_nombre():
    nombre = input("\n ♥Ingrese su nombre: ")

    while len(nombre) == 0 or not nombre.isalpha():
        nombre=input(" ERROR. Nombre invalido - Ingrese uno nuevo: ")
    
    return nombre

#-----------------------------------------------------------------------------------------------------------------------------#

def ingresar_apellido():
    apellido = input(" ♥Ingrese su apellido: ")

    while len(apellido) == 0 or not apellido.isalpha():
        apellido=input(" ERROR. Apellido invalido - Ingrese uno nuevo: ")

    return apellido

#-----------------------------------------------------------------------------------------------------------------------------#

def verf_contraseña(contraseña):
    
    tien_May = False
    tien_Min = False
    tien_Num = False
        
    for caracter in contraseña:
        if caracter.isnumeric():
            tien_Num = True
        elif caracter.isupper():
            tien_May = True
        elif caracter.islower():
            tien_Min = True
    
    return tien_Num and tien_May and tien_Min

#-----------------------------------------------------------------------------------------------------------------------------#

def contraseña():
    
    LARGO_MIN_CONT = 5
    
    contraseña = input("\n ♥Ingrese su contraseña [Debe incluir una mayúscula, una minúscula, un numero, y tener mas de 5 caracteres]: ")
    
    while len(contraseña) < LARGO_MIN_CONT  or not verf_contraseña(contraseña):
        contraseña = input(" ERROR. La contraseña no cumple con los requisitos - Ingrese una nueva: ")
    
    return contraseña

#-----------------------------------------------------------------------------------------------------------------------------#

def sexualidad():
    
    sex = input("\n ♥Ingrese su sexo entre:\n\t*Mujer [M]\n\t*Hombre [H]\n\t*Indefinido [I]\n Sexo: ")
    sexo_valido = ["m", "M", "h", "H", "i", "I"]
    
    while sex not in sexo_valido:
        sex = input(" ERROR. Opcion invalida, intenta nuevamente: ")    
    
    return sex.upper()

#-----------------------------------------------------------------------------------------------------------------------------#

def ingre_edad():
    
    EDAD_MIN = 18
    EDAD_MAX = 99
    
    ed = input("\n ♥Ingrese su edad [Su edad debe de estar entre los 18 y 99 años]: ")
    
    while ed.isnumeric() == False or int(ed) < EDAD_MIN or int(ed) > EDAD_MAX:
        ed = input(" Edad fuera de los limites, intentelo de nuevo: ")
        
    return int(ed)

#-----------------------------------------------------------------------------------------------------------------------------#

def ubicacion():
    
    coord = []
    
    latitud = input(" ♥Ingrese su latitud en grados decimales [Consulte en Go*gle M*ps de no conocerla]: ")

    a = 0   
    while a == 0:
        try:
            float(latitud)
            a = 1
        except: 
            latitud = input("ERROR. Latitud invalida - vuelva a intentar: ")
            
    longitud = input(" ♥Ingrese su longitud en grados decimales [Consulte en Go*gle M*ps de no conocerla]: ")

    a = 0
    while a == 0:
        try:
            float(longitud)
            a = 1
        except:
            longitud = input("ERROR. Longitud invalida - vuelva a intentar: ")

    coord.append(float(latitud)) 
    coord.append(float(longitud))
    
    return coord

#-----------------------------------------------------------------------------------------------------------------------------#

def etiqueta_valida(interes):
    
    valido = True
    tildes = ["á","é","í","ó","ú","Á","É","Í","Ó","Ú"] 
    guion="-"
    
    if len(interes) == 0:
        valido = False
    else:
        indice = 0
        while indice < len(interes):
            if interes[indice] == " " or interes[indice] in tildes or (interes[indice].isalpha() == False and interes[indice] != guion):
                print ("Error. Interes invalido, intenta de nuevo")
                interes = input("\n\t - ")
                indice = 0
            else:
                indice += 1
    
    return valido, interes

#-----------------------------------------------------------------------------------------------------------------------------#

def etiquetas_de_interes():
    
    lista_intereses = []
    
    interes = input("\n ♥Ingresa tus intereses\n  Los intereses son etiquetas, palabras sin espacio ni tildes unidas unicamente con guiones medios\n [Para dejar de ingresar solo debe dejar el espacio en blanco]\n\n Intereses: \n\t - ")
    
    val, interes = etiqueta_valida(interes)
        
    while val and len(interes) != 0:
        lista_intereses.append(interes)
        interes = input ("\t - ")
        val, interes = etiqueta_valida(interes)         
        
    return lista_intereses

#-----------------------------------------------------------------------------------------------------------------------------#

def nueva_persona():
    
    usuarios = pickle.load(open("Datos_Usuarios_Final.pkl" , "rb"))
    
    os.system ('cls||clear')
    
    print("\n\tGracias por decidir ser un usuario nuevo! (ᵔ U ᵔ)")
    print("\tVamos a crear un perfil inigualable!")
    
    pseudo = Pseudonimo(usuarios)

    nombre = ingresar_nombre()

    apellido = ingresar_apellido()
    
    contra = contraseña()
        
    sexo = sexualidad()
    
    edad = ingre_edad()
   
    print("\n- Su siguiente paso es indicar tu ubicacion actual")

    coord = ubicacion()
    
    print("\n- Muy Bien!")
    print("  Hemos llegado a una parte importante en la creacion de tu perfil :D")
    intereses = etiquetas_de_interes() 
    
    foto_de_perfil = foto()
    
    matcheos = []

    chats = {}

    usuarios[pseudo] = [nombre, apellido, contra, sexo, edad, coord, intereses, matcheos, chats, foto_de_perfil]
    
    pickle.dump(usuarios, open("Datos_Usuarios_Final.pkl", "wb"))
    
    return pseudo    
    
#-----------------------------------------------------------------------------------------------------------------------------#
